# DEMO PLAYBOOK - live demos for buyers (Baba 2026-09-29)

Baba's orders this lane:
- "we can provide them demo url during our first reachout mail with a created user
  credential..more convincing" (06:2x) -> DONE, wired into `smtp_send.py`.
- "if laptop becomes overloaded do we host on Kaggle on demand by the user for a
  demo - better approach" (06:2x) -> 3-tier host plan below.
- "we dont hide kaggle session limits we tell them" -> DISCLOSURE LAW (below).
- "make it live and unattended" -> keepalive + KILO-DEMO task.

## THE STACK (what is LIVE right now, 2026-09-29 06:44 IST)

Tier 1 - always-on static floor: the public GitHub catalogue
(`github.com/isearchxsolve/repo-catalog`) is linked in every mail, so even if every
tunnel dies the proof never 404s.
Tier 2 - interactive showcase (LIVE NOW): `demo/showcase/app.py` (Flask + SQLite,
71 repo cards from REPO-CATALOG-V2) served on 127.0.0.1:8899, tunnelled by a free
cloudflared quick tunnel. Current url lives ONLY in `demo/state/showcase.json`
(the mail re-reads it, never hardcodes).
Tier 3 - Kaggle on-demand (PLANNED, not built): a separate demo kernel runs the
heavy prototype + cloudflared inside the notebook and announces its url on the wire
(public door `/say`). Use when laptop CPU>70% or a full-project demo is asked.
Honest state: tier 3 script NOT written yet - do not promise a Kaggle demo until it
is receipted.

## DISCLOSURE LAW (Baba: we tell them)
Every mail that carries a demo block already states the hosting window plainly
("served live from my own machine through a free Cloudflare tunnel, so it has
windows"). If/when tier 3 goes live, its 12h session limit is disclosed the same
way, up front. Never hide a limit; never promise 24/7 we do not have.

## PER-BUYER CREDENTIALS
- `demo.py make_creds` files a pair; `smtp_send.demo_block()` PROVISIONS a real row
  (`showcase.create_user`) per recipient - user `demo-<org>`, random password.
- Passwords are pbkdf2-hashed in `demo/showcase/showcase.db` and SURVIVE restarts
  (the db is a file). Creds files are LOCAL ONLY (never wire, never commit).
- Wrong password is refused (E2E step 2 proves it). No shared admin login, ever.

## COMMANDS
    cd D:\anonym\war-log\demo
    python demo.py up showcase --port 8899 --cmd "python app.py" --root showcase
    python provision.py showcase          # make the printed pair actually loginable
    python e2e_login_test.py              # PASS/FAIL over the PUBLIC url -> receipts/
    python demo.py status | down showcase | creds showcase
Send path: `python war-log/smtp_send.py --test|--dry|--batch N` - the demo block is
injected automatically before the signature whenever the showcase probes healthy;
if it is down the mail still goes out WITHOUT a link (never a dead URL).

## UNATTENDED
- `demo/keepalive.ps1` (visible window, single-instance via window title): every
  10 min probes /health + cloudflared, restarts, re-runs e2e, logs to
  `demo/logs/keepalive.log`.
- Task `KILO-DEMO` every 15 min re-runs the same script (exits at once if the loop
  is alive) - the loop survives reboot and dead windows.

## RECEIPTS
- E2E PASS: `demo/receipts/e2e-20260929-063921.txt` (login 200, bad pw refused,
  good pw logged-in, 71 cards, /health 200).
- Mail with demo login: `evidence/L1/_smtp_20260929-064215_isearchxsolvegmailcom.txt`
  (code 250 + LIVE DEMO block + creds in body) + ledger row 06:42:15.
- Keepalive: `demo/logs/keepalive.log` ("healthy (app 200 + tunnel alive)").
- State: `demo/state/showcase.json`; creds: `demo/creds/*.txt`.

## TEARDOWN / HYGIENE
`python demo.py down showcase` kills the whole process tree (taskkill /T). Delete a
buyer's creds file when their deal closes. Never expose anything but our own code
on our own machines (Father's Seal, AGENTS.md section 18).
