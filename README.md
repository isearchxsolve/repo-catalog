# Repository Catalogue - Kunal Das (isearchxsolve)

*Private source-code catalogue. Listings only - no source code is published and
ownership is retained. Licences are non-exclusive by default.*

Generated 2026-10-06 from the live GitHub account. Every line
count below is **git-measured and reproducible**, not asserted.

| Metric | Value |
|---|---|
| Repositories in account | 122 |
| **Private** repositories | **118** |
| **Source lines, total measured** | **1,952,288** across **49** repositories |
| - original work | 879,401 |
| - on a labelled open-source base | 1,072,887 |
| Git-tracked source files | 10,845 |
| Commits | 1,488 |
| Private storage footprint | 1.3 GB |

**Languages:** Python 63, TypeScript 23, JavaScript 11, Notebook 7, PowerShell 3,
Dart 2, Kotlin 1, unclassified 8.

**Measurement method (so a buyer can verify, not believe):** only files tracked
by git count as source. Committed dependency trees (`node_modules/`,
`site-packages/`), build output and duplicate archives are excluded. Docs,
notebooks and configuration are excluded from LOC. Empty placeholder repositories
are omitted. Reproducible from the account with `git ls-files` plus a line count.

**Open-source base, labelled:** `ikon_agent-main` is built on n8n v1.72.1; our
layer is 5 files outside the base tree. The base is counted separately above and
is **not** presented as original authorship.

---
## Crown jewels - the flagship assets

Three assets carry ~38 engineer-months of original engineering between them. Each is listed with what it actually does, its honest gaps, and its value band. The gaps are stated because a buyer will find them in due diligence anyway - and two of them are cheap to close.

### 1. neon_architect_v4_7_mobile_env.py  (NEON ARCHITECT v4.6.4)

**A complete autonomous SDLC agent in one file.** Plans, architects, implements, tests, reviews, deploys and verifies without leaving the process.

| | |
|---|---|
| **Size** | 12,711 lines / 601 KB |
| **Engineering** | 16.5 engineer-months |
| **Value band** | $75,000 - 120,000 non-exclusive  |  $200,000 - 350,000 exclusive |
| **Natural buyer** | Developer-tools companies, agent-platform builders, acqui-hire. |

**Why it is worth what it is worth**

- **`generate_app` - SDLC inside a tool.** Full-stack scaffold plus a live preview, not a snippet generator. This is the product, not a feature.
- **Self-healing provider pool.** Per-`(base_url, api_key)` token bucket, 429 propagation across siblings on the same account, and dead-model persistence (404/410 cached per project) so a retired model is rediscovered once, not on every request.
- **DeployTool closes the localhost-to-production gap.** GitHub push plus Vercel / Netlify / Fly / Railway CLI.
- **17 tools with permission gates** for destructive bash and paths outside the project, plus XML interception and a malformed-streak detector so tool calls fail loudly instead of silently.
- **Smart compaction** (60k startup budget, 0.3 threshold) and per-phase model overrides - the agent uses a cheaper model to write tests and a stronger one to verify them.

**Stated gaps (fix these before a sale closes)**

- Tests exist at the workspace root (`harness_test.py`, `run_full_test.py`, `test.py`) but are **not inside the repo**. This is a packaging gap, not a missing-suite gap. Integrating them plus CI is the highest-ROI action on this asset and moves its risk discount from 30% to 10%.
- Synchronous HTTP only - no async runtime yet.
- No plugin/extension interface (`register_tool` / `register_provider`).

---

### 2. GODSHAND_src_FIX  (AI Film Kit 'THE MOMENT' v3)

**A complete AI film production pipeline that runs entirely on free tiers** - no credit card, no paid services, no filmed footage.

| | |
|---|---|
| **Size** | ~300 files / 34 MB / 12 pipeline stages |
| **Engineering** | 9.5 engineer-months |
| **Value band** | $25,000 - 40,000 non-exclusive  |  $60,000 - 150,000 exclusive |
| **Natural buyer** | AI-training corpora (code patterns), generative-video companies. |

**Why it is worth what it is worth**

- **Blueprint Path - 5-8x cheaper video.** Stills are drawn pixel-perfect per beat (99% of the perceived quality), then animated with Wan 2.2 image-to-video at low denoise (0.35) using the still as an anchor frame. Applies to any diffusion video pipeline, not just this one.
- **Identity auto-retry loop.** InsightFace cosine similarity against the character reference set after every take; below the drift threshold it re-renders with a new seed, up to 4 attempts, with no manual intervention. Closed-loop correction of face drift.
- **Cost meter + hard budget gate + dry-run default.** One sample shot is rendered, true speed measured, the full cost projected, and the run **aborts before spending** if it exceeds the budget. Spending requires an explicit flag. Cost cannot leak.
- **Resumable per-shot checkpointing** - finished shots auto-skip, so a dropped 2xT4 session resumes from the last checkpoint instead of starting over.

**Stated gaps (fix these before a sale closes)**

- **Model licence audit outstanding** (Wan 2.2, HunyuanVideo, Kokoro, Parler-TTS, MusicGen, CodeFormer, InsightFace). A commercial buyer cannot sign until each is classified.
- **Personal likeness references embedded** - must be stripped before any sale.
- A duplicate copy of this asset sits in the tree and should be deleted.

---

### 3. neon_architect.py  (NEON ARCHITECT v4.6.4 - Compact)

The interactive coding-agent core, without the mobile/env layer.

| | |
|---|---|
| **Size** | ~8,112 lines / 382 KB |
| **Engineering** | 12.0 engineer-months |
| **Value band** | $25,000 - 45,000 non-exclusive  |  $80,000 - 150,000 exclusive |
| **Natural buyer** | Interactive-agent buyers; normally bundled. |

**Why it is worth what it is worth**

- The same provider-pool resilience and tool system as the full agent, stripped to the interactive loop.
- Ships as a **bundle with v4.7** - it is a strict subset and is priced that way, not as a standalone crown.

**Stated gaps (fix these before a sale closes)**

- Same test-integration gap as v4.7.
- Strict subset of v4.7.

---

## Full inventory by domain

The complete measured list lives in `REPO-CATALOG-V2.md` and the machine-readable
`measurement.json` (per-repository LOC, file counts, commits, language, disk, and
open-source base where applicable). Both are in this repository so the numbers can
be checked rather than trusted.

## How to buy

Licensing is **non-exclusive by default** - the same asset may be licensed to
multiple buyers, and the catalogue stays ours. Exclusive transfer is a separate
conversation at audit value, and is never the default.

- Written scope first, then price against the band above.
- 50% advance to begin; balance on verified delivery.
- Written channels only.
- Sample source inspection available under mutual NDA.

**Contact:** Kunal Das - isearch.xsolve@gmail.com | +91 86172 16163 (WhatsApp
text only, no calls) | MCA DIN 10386590
