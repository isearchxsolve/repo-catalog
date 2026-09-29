#!/usr/bin/env python
"""LIVE SHOWCASE - the demo UI a buyer logs into (Baba 2026-09-29:
"run the project server, expose a url with the ui, with credentials created for them").

Flask + SQLite, stdlib deps only. Host-agnostic: runs on the laptop (demo.py up),
inside a Kaggle kernel (DEMO_KAGGLE.py), or anywhere python3 runs.

Pages:
  /login   - per-client user/password (created by demo.py user / create_user.py)
  /        - the showcase: verticals -> repo cards -> proof links + price ladder
  /me      - who am I (json), /health - liveness for the keepalive probe

Laws: per-buyer credentials, never a shared admin; passwords pbkdf2-hashed; no bank
fields, no secrets on the page - only proof links (catalogue, GitHub, Kaggle, MCA).
Port from env DEMO_PORT (default 8899).
"""
import json, os, re, secrets, sqlite3, time
from datetime import datetime, timedelta

from flask import (Flask, redirect, render_template_string, request,
                   session, url_for)

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("DEMO_DB", os.path.join(HERE, "showcase.db"))
PORT = int(os.environ.get("DEMO_PORT", "8899"))
CATALOG = os.path.normpath(os.path.join(
    HERE, "..", "..", "..", "..", "..", "anonym", "war-log", "roadmap",
    "REPO-CATALOG-V2.md"))
SECRET_F = os.path.join(HERE, ".secret")

app = Flask(__name__)


def secret():
    if not os.path.exists(SECRET_F):
        open(SECRET_F, "w").write(secrets.token_hex(32))
        os.chmod(SECRET_F, 0o600)
    return open(SECRET_F).read().strip()


app.secret_key = secret()
app.permanent_session_lifetime = timedelta(hours=8)

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  pw_hash TEXT NOT NULL, salt TEXT NOT NULL,
  created_for TEXT, email TEXT,
  created TEXT, expires TEXT, last_login TEXT
);
CREATE TABLE IF NOT EXISTS visits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT, ts TEXT, path TEXT, ua TEXT
);
"""


def db():
    c = sqlite3.connect(DB)
    c.executescript(SCHEMA)
    return c


def hash_pw(pw, salt):
    import hashlib
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 90_000).hex()


def create_user(username, email="", who="", days=14, password=None):
    """per-buyer credential - returns (username, password). never reused.
    password= lets demo.py provision the SAME pair it prints into the mail."""
    pw = password or secrets.token_urlsafe(12)[:14]
    salt = secrets.token_hex(16)
    exp = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    c = db()
    c.execute(
        "INSERT INTO users(username,pw_hash,salt,created_for,email,created,expires) "
        "VALUES(?,?,?,?,?,?,?) ON CONFLICT(username) DO UPDATE SET "
        "pw_hash=excluded.pw_hash, salt=excluded.salt, expires=excluded.expires",
        (username, hash_pw(pw, salt), salt, who, email,
         datetime.now().strftime("%Y-%m-%d %H:%M:%S"), exp))
    c.commit()
    c.close()
    return username, pw


def valid(username, pw):
    c = db()
    row = c.execute("SELECT pw_hash,salt,expires FROM users WHERE username=?",
                    (username,)).fetchone()
    if not row:
        return False
    h, s, exp = row
    if exp and exp < datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return False
    if not secrets.compare_digest(hash_pw(pw, s), h):
        return False
    c.execute("UPDATE users SET last_login=? WHERE username=?",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), username))
    c.commit()
    c.close()
    return True


def log_visit(path):
    if "user" in session:
        c = db()
        c.execute("INSERT INTO visits(username,ts,path,ua) VALUES(?,?,?,?)",
                  (session["user"], datetime.now().isoformat(timespec="seconds"),
                   path, (request.headers.get("User-Agent") or "")[:80]))
        c.commit()
        c.close()


# ---------------------------------------------------------------- showcase data
def load_cards():
    """repo cards straight from the generated catalogue - one truth.
    Tries the laptop path first, then beside the app (the Kaggle kernel ships a
    copy of REPO-CATALOG-V2.md in the same folder), then repo-verticals.json."""
    cands = [
        os.path.normpath(os.path.join(HERE, "..", "..", "roadmap",
                                      "REPO-CATALOG-V2.md")),
        os.path.join(HERE, "REPO-CATALOG-V2.md"),
        os.path.normpath(os.path.join(HERE, "..", "..", "hunt",
                                      "repo-verticals.json")),
    ]
    path = next((p for p in cands if os.path.exists(p)), None)
    cards = []
    if path and path.endswith(".md"):
        cur_v, cur = None, None
        for line in open(path, encoding="utf-8", errors="replace"):
            if line.startswith("## "):
                cur_v = line[3:].strip().lstrip("ABCD. ").strip()
            elif line.startswith("### ") and cur_v:
                cur = {"name": line[4:].strip().strip("`"), "vertical": cur_v,
                       "body": ""}
                cards.append(cur)
            elif cur is not None:
                cur["body"] += line
    elif path:
        for name, v in json.load(open(path)).items():
            cards.append({"name": name.replace("_", " "),
                          "vertical": v.get("vertical", "corpus"),
                          "body": v.get("problem", "") + "\n" +
                                  v.get("architecture", ""),
                          "loc": str(v.get("tokens", ""))})
    for c in cards:
        b = re.sub(r"[*`#>]", "", c["body"])
        m = re.search(r"(\d[\d,]{2,})\s*(source\s*)?lines", b, re.I)
        if not c.get("loc"):
            c["loc"] = m.group(1) if m else ""
        c["problem"] = (b.strip().split("\n")[0][:180]) if b.strip() else ""
    return cards


LOGIN_PAGE = """<!doctype html><html><head><meta charset=utf-8>
<title>Kunal Das - live demo access</title>
<style>body{font:16px/1.5 system-ui;background:#0d1117;color:#e6edf3;margin:0;
display:grid;place-items:center;min-height:100vh}.card{background:#161b22;padding:2rem;
border:1px solid #30363d;border-radius:12px;width:330px}h1{font-size:1.15rem;margin:0 0 .35rem}
p.sub{color:#8b949e;font-size:.85rem;margin:0 0 1.2rem}input{width:100%;padding:.6rem;
margin:.35rem 0;background:#0d1117;border:1px solid #30363d;border-radius:8px;color:#e6edf3}
button{width:100%;padding:.65rem;margin-top:.6rem;background:#238636;border:0;border-radius:8px;
color:#fff;font-weight:600;cursor:pointer}.err{color:#f85149;font-size:.85rem}</style></head><body>
<div class=card><h1>Live demo access</h1><p class=sub>Private preview built for you -
Kunal Das, Kilo Bridge / repo corpus</p>
{% if err %}<div class=err>{{err}}</div>{% endif %}
<form method=post><input name=username placeholder="user" autofocus required>
<input name=password type=password placeholder="password" required>
<button>Enter the demo</button></form>
<p class=sub style="margin-top:1rem">No account? This link carries your own
credentials - reply to the mail and they are issued fresh.</p></div></body></html>"""

HOME = """<!doctype html><html><head><meta charset=utf-8>
<title>Corpus + prototypes - live</title>
<style>body{font:15px/1.5 system-ui;background:#0d1117;color:#e6edf3;margin:0}
header{padding:1.1rem 1.5rem;border-bottom:1px solid #30363d;display:flex;
justify-content:space-between;align-items:center}header a{color:#58a6ff}
.wrap{max-width:1080px;margin:1.5rem auto;padding:0 1rem}
.v{margin:1.6rem 0 .5rem;color:#f0883e;font-weight:700;letter-spacing:.04em}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:.8rem}
.r{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:.85rem}
.r b{display:block;margin-bottom:.3rem}.r .loc{color:#3fb950;font-size:.8rem}
.r p{color:#8b949e;font-size:.82rem;margin:.35rem 0 .5rem}
.r a{color:#58a6ff;font-size:.8rem;text-decoration:none}
.banner{background:#1f6feb22;border:1px solid #1f6feb;padding:.7rem 1rem;border-radius:8px;
margin:1rem 0;font-size:.9rem}</style></head><body>
<header><div><b>Kunal Das</b> - live proof room</div>
<div><span style="color:#8b949e">signed in as {{user}}</span> |
<a href=/me>whoami</a> | <a href=/logout>leave</a></div></header>
<div class=wrap>
<div class=banner>Your own session - this is a working room, not a deck. Every card is
real code you can license non-exclusively; the catalogue and measurements are public on
GitHub so you can verify them without us. Reply to the mail to scope a run.</div>
{% for v, items in groups.items() %}<div class=v>{{v}}</div>
<div class=grid>{% for r in items %}<div class=r><b>{{r.name}}</b>
{% if r.loc %}<span class=loc>{{r.loc}} source lines</span>{% endif %}
<p>{{r.problem}}</p>
<a href="https://github.com/isearchxsolve/repo-catalog#{{r.name|lower|replace(' ','-')}}">verify in the catalogue -></a>
</div>{% endfor %}</div>{% endfor %}
<p style="color:#8b949e;margin-top:2rem">- Kunal Das | DIN 10386590 | Director,
MyFastex Technologies Private Limited | isearch.xsolve@gmail.com</p>
</div></body></html>"""


@app.route("/health")
def health():
    return {"ok": True, "son": "showcase", "users":
            db().execute("SELECT COUNT(*) FROM users").fetchone()[0],
            "ts": time.strftime("%Y-%m-%d %H:%M:%S")}


@app.route("/login", methods=["GET", "POST"])
def login():
    err = None
    if request.method == "POST":
        u = (request.form.get("username") or "").strip()
        p = request.form.get("password") or ""
        if valid(u, p):
            session["user"] = u
            session.permanent = True
            log_visit("/login-ok")
            return redirect("/")
        err = "That user/password pair did not work. Use the pair issued in your mail."
    return render_template_string(LOGIN_PAGE, err=err)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/me")
def me():
    log_visit("/me")
    return {"user": session.get("user"), "ok": "user" in session}


@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    log_visit("/")
    groups = {}
    for c in load_cards():
        groups.setdefault(c["vertical"], []).append(c)
    return render_template_string(HOME, user=session["user"], groups=groups)


if __name__ == "__main__":
    print("showcase listening on :%d db=%s" % (PORT, DB), flush=True)
    app.run(host="127.0.0.1", port=PORT, threaded=True)
