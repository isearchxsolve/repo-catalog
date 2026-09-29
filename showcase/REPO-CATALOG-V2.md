# Repository Catalog - Kunal Das (isearch.xsolve)

Private source-code catalogue, generated 2026-09-29 from the live GitHub account.
Ownership is retained by the author; no repository is sold - licences are
non-exclusive by default. Repositories built on a published open-source base
are labelled as such (base + our development layer).

**Repository totals**

| Metric | Value |
|---|---|
| Repositories in account | 122 |

**How to read this page (v2):** every repository is described by the
problem it solves and the architecture behind it, grouped by the vertical
it belongs to. Licensing is non-exclusive by default; ownership is not for
sale. Full inventory and per-repo line counts available under NDA.

Source of the architecture notes: internal deep-review documents written
2026-09-26 (security findings and valuations are withheld here on purpose).

## AI agents & autonomous systems

### `ases_v3_1`
- **Vertical:** AI agents & autonomous systems | Python | 39,318 source lines | last push 2026-09-06
- **What it does:** ASES v3.1 agent service: sandboxed multi-agent code generation (~40k LOC, 166 files)

### `emergentsh_latest`
- **Vertical:** AI agents & autonomous systems | TypeScript | 12,282 source lines | last push 2026-09-06
- **What it does:** EmergentSH multi-agent application builder (TypeScript build)

### `omniroute-monetizer`
- **Vertical:** AI agents & autonomous systems | Python | 163,115 source lines | last push 2026-09-06
- **What it does:** Master OmniRoute Monetizer - end-to-end provider onboarding and billing

### `ikon_agent-main`
- **Vertical:** AI agents & autonomous systems | TypeScript | 1,072,887 (incl. base) source lines | last push 2026-09-06
- **What it does:** IKON autonomous agent runtime - built on n8n v1.72.1

### `emergentsh`
- **Vertical:** AI agents & autonomous systems | Python | - source lines | last push 2026-09-06
- **What it does:** EmergentSH multi-agent application builder

### `convergence_framework`
- **Vertical:** AI agents & autonomous systems | Python | 3,238 source lines | last push 2026-09-06
- **What it does:** Convergence orchestration framework

### `state-omniroute-ltx-fresh-data`
- **Vertical:** AI agents & autonomous systems | - | - source lines | last push 2026-09-06
- **What it does:** OmniRoute - captured live dataset state

### `idea-terminal-engine`
- **Vertical:** AI agents & autonomous systems | Python | 11,709 source lines | last push 2026-09-06
- **What it does:** An **autonomous idea-to-prototype engine** that drives a raw natural-language idea to a **verified, running prototype (local run)** that also serves as **Go-to-Market Version 1 (GTM v1)**. The engine explicitly accepts that *technical infeasibility discovered during verification is a successful outcome for the service* — the client learns the idea doesn't hold up in weeks, not years.
- **Architecture:** ``` RECEIVED → DISTILLED → BLUEPRINTED → PLANNED → BUILDING → QA_VERIFYING → RELEASED ↓ ↓ REPAIRING ← AWAITING_APPROVAL ↓ FAILED (absorbing from any state) ```

### `state-omniroute-3.8.50-sandbox`
- **Vertical:** AI agents & autonomous systems | - | - source lines | last push 2026-09-06
- **What it does:** OmniRoute 3.8.50 - sandbox state

### `voice_agent_avatar`
- **Vertical:** AI agents & autonomous systems | Python | - source lines | last push 2026-09-06
- **What it does:** Voice agent with animated avatar

### `n8n-frellancing_advanced-ases_v3_1`
- **Vertical:** AI agents & autonomous systems | Python | - source lines | last push 2026-09-06
- **What it does:** n8n automation - ASES integration build

### `emergenttrader`
- **Vertical:** AI agents & autonomous systems | JavaScript | - source lines | last push 2026-09-06
- **What it does:** EmergentTrader - agentic trading application

### `sale-convergence_framework-convergence_project_latest`
- **Vertical:** AI agents & autonomous systems | Python | - source lines | last push 2026-09-06
- **What it does:** Convergence framework - release build

### `n8n-frellancing_advanced-agent_service`
- **Vertical:** AI agents & autonomous systems | Python | - source lines | last push 2026-09-06
- **What it does:** n8n automation - agent service integration

### `test_coding_agent`
- **Vertical:** AI agents & autonomous systems | Python | 7,518 source lines | last push 2026-09-06
- **What it does:** Coding agent evaluation harness

### `nemo_test`
- **Vertical:** AI agents & autonomous systems | Python | 5,203 source lines | last push 2026-09-06
- **What it does:** **OpenPath** — an **AI-native test automation framework** positioned as the **open-source alternative to UiPath/BluePrism for web applications**. Replaces drag-and-drop RPA with natural-language test cases. Detects stack, boots app, writes/runs test plan, produces rich HTML/JUnit/JSON reports — all from one CLI command.
- **Architecture:** ``` CLI (openpath run) → Mode: codebase | url → Stack Detector (detect/stack_detector.py) — language/framework detection → Server Manager (detect/server_manager.py) — subprocess lifecycle + health check → Plan Generator (detect/plan_generator.py) — automatic test-plan derivation → Test Execution: ├─ Playwright Runner (engine/playwright_runner.py) — deterministic sync runner └─ AI Runner (engine/ai_runner.py) — LLM computer-use loop + NL compiler → Self-healing Selectors (engine/selectors.py) — 5-tier fallback → Assertions (engine/assertions.py) — 8 assertion types → Report Writers (report/html.py, junit.py) — HTML, JUnit XML, JSON ```

### `claude_code_clone`
- **Vertical:** AI agents & autonomous systems | Python | 5,592 source lines | last push 2026-09-06
- **What it does:** Claude-style coding agent clone

### `uncensoredgeminiapp`
- **Vertical:** AI agents & autonomous systems | Python | - source lines | last push 2026-09-06
- **What it does:** Gemini-based assistant application

### `omniroute_dashboard`
- **Vertical:** AI agents & autonomous systems | TypeScript | 410 source lines | last push 2026-09-06
- **What it does:** OmniRoute operations dashboard

### `services-mcp`
- **Vertical:** AI agents & autonomous systems | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Microservice - MCP tool server

### `crypto-trading-ai-agent`
- **Vertical:** AI agents & autonomous systems | Python | 1,523 source lines | last push 2026-09-06
- **What it does:** -


## Film, video & voice generation

### `god_ai`
- **Vertical:** Film, video & voice generation | TypeScript | - source lines | last push 2026-08-22
- **What it does:** AI Film Kit v3 - full film production pipeline

### `antigravity-kandover`
- **Vertical:** Film, video & voice generation | Jupyter Notebook | 17,390 source lines | last push 2026-09-06
- **What it does:** **THE MOMENT AI Film Kit (v3: Constrained + Hardened)** — Generate a **short film ("THE MOMENT") on free GPUs (Kaggle 2x T4)** from **photos + typed dialogue only** — no filmed footage, no paid services, no voice sample. Built for three hard constraints: 1. No credit card / free-tier only 2. No driving/motion video available 3. Only photos of two people (Kunal + Gunja)
- **Architecture:** ``` preflight → cull photos → build young-Kunal set (de-age) → render pixel-perfect STILLS per beat (render_stills) → ANIMATE each still into motion with low denoise (render_motion) → identity check + auto-retry (CPU insightface) → voice (cinematic TTS with reverb bus) → score (original dramatic score) → sfx (ambience/foley) → stitch + master (ProRes 4:4:4 optional) ``` **Key Innovation:** "Blueprint-First" path — render **one pixel-perfect STILL per beat** (full resolution, full steps, rejection sampling), hold as frozen-frame video clip; then animate each still into motion with low denoise. Cuts GPU time ~5-8x vs full motion rendering.

### `god_ai_scripts`
- **Vertical:** Film, video & voice generation | Python | 9,935 source lines | last push 2026-09-06
- **What it does:** AI Film Kit - screenplay/script generation module

### `the-beholder-project`
- **Vertical:** Film, video & voice generation | Python | 10,311 source lines | last push 2026-09-06
- **What it does:** The Beholder Project - research + authoring engine

### `kdp-polished`
- **Vertical:** Film, video & voice generation | Python | 2,846 source lines | last push 2026-09-04
- **What it does:** The Beholder Project - KDP publishing workspace

### `the_last_laugh_kit-kit`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** The Last Laugh - packaged creative kit

### `the_moment_full_bundle-bundle`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** The Moment - full content bundle

### `ai_video_monetizer`
- **Vertical:** Film, video & voice generation | Python | 4,632 source lines | last push 2026-09-06
- **What it does:** AI video monetization pipeline

### `oioi`
- **Vertical:** Film, video & voice generation | Python | 66,448 source lines | last push 2026-08-31
- **What it does:** oioi is a **full-stack AI animation platform** that replicates oiioii.ai: users describe an idea → 7-agent pipeline (Scriptwriter → Art Director → Character Designer → Scene Designer → Storyboard Artist → Animator → Sound Director → Director) produces a short film. Key differentiator: **provider-agnostic media generation** with free-tier failover (Pollinations, rtst.ai, heygen, etc.) via OmniRoute video gateway (`:8189`).
- **Architecture:** | Component | Role | |-----------|------| | `frontend/` (React + Vite + Tailwind) | Infinite canvas UI (react-flow), node-based generation, real-time queue | | `backend/` (FastAPI + SQLAlchemy + SQLite) | Agent orchestrator, provider registry, job/asset stores, video pipeline | | `backend/agent_pipeline.py` | Legacy adapter → new `AnimationAgentOrchestrator` (7 agents + Director) | | `backend/services/orchestrator.py` | Core orchestration: persists `AgentExecution` rows, uses `ProviderRegistry` | | `backend/providers/` | Provider adapters (image/video/chat) with priority/cooldown/failover | | `film_kit.py` | Standalone Ken Burns film generator (NIM + Pollinations + edge-tts + ffmpeg) | | ...
- **Engineering that matters:** 1. **7-Agent Film Pipeline with Director** — Hierarchical agent crew with persistent `AgentExecution` rows; each agent has typed input/output contracts 2. **Provider-Agnostic Video Gateway (`:8189`)** — Async job API with idempotent `jobKey`, capacity polling, failure classification (`wall:`/`auth:`/transient), per-seat credit tracking 3. **Hybrid Degradation Path** — On capacity exhaustion → Ken Burns clip (Pollinations + ffmpeg) in same ordered slot → film always completes 4. **Clip-Job Graph ...

### `state-measure-oioi-shot-count`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** OiiOii - shot-count measurement state

### `the_one_full_film_kit_audio_upgraded_with_confrontation-film_kit_v3`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** Film Kit v3 - audio-upgraded full pipeline

### `film_kit_v3_confrontation_updated-kit`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** Film Kit v3 - confrontation sequence module

### `filmforge`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** FilmForge - short-form video generation tool

### `godshand_kit_final-godshand_src_fix`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** A complete, free-tier-only AI film production pipeline that generates a short film ("THE MOMENT" / "THE CONFRONTATION CLIP") from **photos + typed dialogue only** — no filmed footage, no paid services, no voice samples. Designed for three hard constraints: 1. No credit card / free-tier only (Kaggle 2x T4, Lightning AI L4) 2. No driving/motion video available 3. Only photos of two people (Kunal + Gunja)
- **Architecture:** ``` 1. preflight → Free, ~5s. Missing model/dep/GPU/disk => abort for ₹0 2. forge → Build character reference identities (idempotent) 3. cost_meter → Render ONE sample shot, measure true speed, project GPU-hrs + $ 4. BUDGET GATE → If projected > MAX_BUDGET_USD, ABORT before full render 5. HOLD GATE → Dry-run default; CONFIRM_FULL_RUN=1 required to spend 6. render → Resumable per-shot render (finished shots auto-skip) 7. voice → Dramatic VO + chorus (Kokoro/Parler TTS + cinematic chain) 8. score → Original violin-led confrontation cue (+ prelude) 9. sfx → Procedural sound design / ambience foley (free) 10. lipsync → Self-skips (all beats are VO/narration) 11. finale → Moving images ...
- **Engineering that matters:** **Blueprint Path (stills → motion)**: `render_stills.py` draws pixel-perfect stills per beat (99% of quality). `render_motion.py` animates each still via Wan 2.2 I2V with **low denoise (0.35)** as anchor frame. This is 5-8x cheaper than raw text-to-video while retaining 99% detail. **Identity Auto-Retry**: After each take, runs InsightFace (CPU) cosine similarity against character reference set. If below `identity.drift_cosine` (default 0.25), re-renders with new seed up to `identity_retry` ...
- **Who needs this:** | Value Dimension | Assessment | |-----------------|------------| | **Code Completeness** | 30+ modules, 12-stage pipeline, 3 config variants — production-grade | | **Reproducibility** | Deterministic seeds, fixed model versions, full config → identical outputs | | **Training Signal** | **High**: End-to-end diffusion video (Wan 2.2 I2V), TTS (Kokoro/Parler), MusicGen, ...

### `godshand_src_fix`
- **Vertical:** Film, video & voice generation | Python | - source lines | last push 2026-09-06
- **What it does:** A complete, free-tier-only AI film production pipeline that generates a short film ("THE MOMENT" / "THE CONFRONTATION CLIP") from **photos + typed dialogue only** — no filmed footage, no paid services, no voice samples. Designed for three hard constraints: 1. No credit card / free-tier only (Kaggle 2x T4, Lightning AI L4) 2. No driving/motion video available 3. Only photos of two people (Kunal + Gunja)
- **Architecture:** ``` 1. preflight → Free, ~5s. Missing model/dep/GPU/disk => abort for ₹0 2. forge → Build character reference identities (idempotent) 3. cost_meter → Render ONE sample shot, measure true speed, project GPU-hrs + $ 4. BUDGET GATE → If projected > MAX_BUDGET_USD, ABORT before full render 5. HOLD GATE → Dry-run default; CONFIRM_FULL_RUN=1 required to spend 6. render → Resumable per-shot render (finished shots auto-skip) 7. voice → Dramatic VO + chorus (Kokoro/Parler TTS + cinematic chain) 8. score → Original violin-led confrontation cue (+ prelude) 9. sfx → Procedural sound design / ambience foley (free) 10. lipsync → Self-skips (all beats are VO/narration) 11. finale → Moving images ...
- **Engineering that matters:** **Blueprint Path (stills → motion)**: `render_stills.py` draws pixel-perfect stills per beat (99% of quality). `render_motion.py` animates each still via Wan 2.2 I2V with **low denoise (0.35)** as anchor frame. This is 5-8x cheaper than raw text-to-video while retaining 99% detail. **Identity Auto-Retry**: After each take, runs InsightFace (CPU) cosine similarity against character reference set. If below `identity.drift_cosine` (default 0.25), re-renders with new seed up to `identity_retry` ...
- **Who needs this:** | Value Dimension | Assessment | |-----------------|------------| | **Code Completeness** | 30+ modules, 12-stage pipeline, 3 config variants — production-grade | | **Reproducibility** | Deterministic seeds, fixed model versions, full config → identical outputs | | **Training Signal** | **High**: End-to-end diffusion video (Wan 2.2 I2V), TTS (Kokoro/Parler), MusicGen, ...


## Crypto, Solana & trading

### `kunals-latest-projects-solana_ex`
- **Vertical:** Crypto, Solana & trading | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Solana trading experiment (TypeScript)

### `crypto-trader-v1`
- **Vertical:** Crypto, Solana & trading | TypeScript | - source lines | last push 2026-09-06
- **What it does:** A **production-grade Solana trading bot** with paper mode as supported default. Four-layer pipeline: Discovery → Scoring → Safety → Entry → Exit ← Risk ← Observability. **Beast-Mode tier** (opt-in) adds: 10-source alpha fusion, composite scoring (LEGENDARY/HIGH/MEDIUM), 6-surface concentric rug/honeypot/LP gate (fail-closed), asymmetric moonshot exit engine (6-tier bag, 7-step TP ladder 1.5x→1000x). Dual-signal watchdog (`failsafe.cjs` + `live-runner.js`) with `.HALT` gate and liquidator.
- **Architecture:** | Component | Role | |-----------|------| | `server/index.ts` | HTTP listener + heartbeat + DB/provider init | | `server/routes.ts` | Complete trading pipeline, paper order lifecycle, daily-loss breaker | | `server/runtime-hooks.ts` | Idempotent heartbeat, `.HALT` gate, readiness/health state | | `server/beast-scanner.ts` | 10-surface pre-valuator (GMGN, DexScreener, on-chain, ML) | | `server/beast-safety.ts` | 6-surface fail-closed safety gate (authority, LP-lock, holders, honeypot, wash, creator) | | `server/beast-exit.ts` | Asymmetric moonshot exit (6-tier bag, 7-step TP, dead-cat disabled ≥10x) | | `fast_scanner.cjs` | Candidate scanner → `candidates.csv` | | ...
- **Engineering that matters:** 1. **Beast-Mode 10-Source Alpha Fusion** — GMGN signals/clusters/trenches, DexScreener profiles/CTO/boosts, on-chain RPC, ML model → deduplication + ranking 2. **Composite Scoring with Tier Qualification** — Gold-score + ML + Beast discovery → LEGENDARY/HIGH/MEDIUM + SNIPER/EDGE/EXPLOSIVE mode 3. **6-Surface Concentric Safety Gate** — Authority + LP-lock + holder concentration + honeypot symmetry + wash trading + creator history (fail-closed by default) 4. **Asymmetric Moonshot Exit Engine** — ...

### `state-lasthelp_rescue-crypto-trader-v1_1`
- **Vertical:** Crypto, Solana & trading | TypeScript | - source lines | last push 2026-09-06
- **What it does:** A **production-grade Solana trading bot** with paper mode as supported default. Four-layer pipeline: Discovery → Scoring → Safety → Entry → Exit ← Risk ← Observability. **Beast-Mode tier** (opt-in) adds: 10-source alpha fusion, composite scoring (LEGENDARY/HIGH/MEDIUM), 6-surface concentric rug/honeypot/LP gate (fail-closed), asymmetric moonshot exit engine (6-tier bag, 7-step TP ladder 1.5x→1000x). Dual-signal watchdog (`failsafe.cjs` + `live-runner.js`) with `.HALT` gate and liquidator.
- **Architecture:** | Component | Role | |-----------|------| | `server/index.ts` | HTTP listener + heartbeat + DB/provider init | | `server/routes.ts` | Complete trading pipeline, paper order lifecycle, daily-loss breaker | | `server/runtime-hooks.ts` | Idempotent heartbeat, `.HALT` gate, readiness/health state | | `server/beast-scanner.ts` | 10-surface pre-valuator (GMGN, DexScreener, on-chain, ML) | | `server/beast-safety.ts` | 6-surface fail-closed safety gate (authority, LP-lock, holders, honeypot, wash, creator) | | `server/beast-exit.ts` | Asymmetric moonshot exit (6-tier bag, 7-step TP, dead-cat disabled ≥10x) | | `fast_scanner.cjs` | Candidate scanner → `candidates.csv` | | ...
- **Engineering that matters:** 1. **Beast-Mode 10-Source Alpha Fusion** — GMGN signals/clusters/trenches, DexScreener profiles/CTO/boosts, on-chain RPC, ML model → deduplication + ranking 2. **Composite Scoring with Tier Qualification** — Gold-score + ML + Beast discovery → LEGENDARY/HIGH/MEDIUM + SNIPER/EDGE/EXPLOSIVE mode 3. **6-Surface Concentric Safety Gate** — Authority + LP-lock + holder concentration + honeypot symmetry + wash trading + creator history (fail-closed by default) 4. **Asymmetric Moonshot Exit Engine** — ...

### `crypto-app-by-replit`
- **Vertical:** Crypto, Solana & trading | TypeScript | 10,110 source lines | last push 2026-09-06
- **What it does:** Crypto portfolio application

### `crypto-app`
- **Vertical:** Crypto, Solana & trading | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Crypto portfolio application

### `solana-auto-trader-live`
- **Vertical:** Crypto, Solana & trading | Python | 4,591 source lines | last push 2026-09-06
- **What it does:** Solana automated trading bot (live mode)

### `kunals-latest-projects-solana_lite`
- **Vertical:** Crypto, Solana & trading | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Solana trading experiment (lite build)

### `crypto-ai-auto-trader`
- **Vertical:** Crypto, Solana & trading | Python | 8,066 source lines | last push 2026-09-06
- **What it does:** AI-driven crypto trading agent

### `solana_earner`
- **Vertical:** Crypto, Solana & trading | Python | - source lines | last push 2026-09-06
- **What it does:** Solana yield automation


## Web, mobile & product apps

### `myfastx`
- **Vertical:** Web, mobile & product apps | JavaScript | - source lines | last push 2024-04-25
- **What it does:** MyFastX - hyper-local courier delivery platform (app + web)

### `neon_unified`
- **Vertical:** Web, mobile & product apps | Python | 42,557 source lines | last push 2026-09-06
- **What it does:** neon_unified is a **meta-framework** that merges multiple generations of the Neon Architect agent into a single package: interactive NIM coding agent (`neon_architect_v5.py`), multi-pass generation core (`generation_core.py`), outer SDLC loops (`sdlc_wrapper.py`, `sdlc_wrapper_full.py`), oiioii-style engineering pack (`oiioii_engineering.py`), and QA browser automation (`qa_browser.py`, `qa_self_heal.py`). It targets **real application building** (web + mobile) with engineering rigor.
- **Architecture:** 1. **Multi-Pass Generation Core (v5)** — 11 deterministic passes (scaffold → architect → tokens → primitives → backend → features → polish → tester → import check → test run → DevOps) with structural validation at each step 2. **Dual SDLC Wrappers** — Core-only (fast) vs Full-agent (complex) outer loops with acceptance criteria evaluation 3. **oiioii Engineering Pack** — Complete animation platform engineering: media service, creative workflow orchestrator, job/asset stores, scaffold bootstrap, strict goals 4. **QA Self-Heal Loop** — Browser automation → pixel diff → repair brief → agent fix → re-QA (closed loop) 5. **Problem Classification (A-F)** — Operational taxonomy: A=entity mismatch, ...
- **Engineering that matters:** 1. **Multi-Pass Generation Core (v5)** — 11 deterministic passes (scaffold → architect → tokens → primitives → backend → features → polish → tester → import check → test run → DevOps) with structural validation at each step 2. **Dual SDLC Wrappers** — Core-only (fast) vs Full-agent (complex) outer loops with acceptance criteria evaluation 3. **oiioii Engineering Pack** — Complete animation platform engineering: media service, creative workflow orchestrator, job/asset stores, scaffold bootstrap, ...

### `lateststablecode`
- **Vertical:** Web, mobile & product apps | TypeScript | 3,872 source lines | last push 2026-09-06
- **What it does:** Stable-channel release snapshot

### `guardian_app`
- **Vertical:** Web, mobile & product apps | Dart | 5,063 source lines | last push 2026-09-06
- **What it does:** Guardian - Flutter mobile application

### `stabletcode`
- **Vertical:** Web, mobile & product apps | TypeScript | 3,426 source lines | last push 2026-09-06
- **What it does:** Stable-channel release snapshot

### `oiioii_clone_final2`
- **Vertical:** Web, mobile & product apps | Python | 3,364 source lines | last push 2026-09-06
- **What it does:** -


## Publishing, content & commerce

### `gumroad-products`
- **Vertical:** Publishing, content & commerce | - | - source lines | last push 2026-09-06
- **What it does:** Gumroad product catalogue and delivery assets


## Data, crawling & infrastructure

### `lasthelp`
- **Vertical:** Data, crawling & infrastructure | Python | 305,190 source lines | last push 2026-08-10
- **What it does:** LastHelp - large Python application (124 MB)

### `screen_guard_final`
- **Vertical:** Data, crawling & infrastructure | Kotlin | 4,197 source lines | last push 2026-09-06
- **What it does:** ScreenGuard - Android screen-protection app (Kotlin)

### `war-pipe`
- **Vertical:** Data, crawling & infrastructure | Python | 426 source lines | last push 2026-09-23
- **What it does:** Kaggle <-> laptop live message pipeline broker

### `anonym-family-archive`
- **Vertical:** Data, crawling & infrastructure | Python | - source lines | last push 2026-09-25
- **What it does:** The **operational nervous system** for the 101-son Kilo Army. Provides: permanent ngrok door (`retrain-schnapps-upbeat.ngrok-free.dev`), relay gateway (port 8777), SYSTEM watchdog (zombie-aware, 15s resurrection), awareness sentinel (5-min cycles, self-heal), phone health monitor (adb), sudo hands (elevated admin), Kaggle worker protocol, voice corpus pipeline, vault (local secrets), session persistence. **Designed for unattended forever operation.**
- **Architecture:** | Component | Role | |-----------|------| | `war-log/son-relay.js` | Relay v4.1: gate (port 8777), `/say` `/hear` `/tool` `/health` `/keys` `/agent`, adb passthrough, title-probe cache, 2-lane queue, CPU>70% drops to 1 lane | | `war-log/relay-watchdog.ps1` + `KILO-RELAY-WATCHDOG` | Watchdog v2: SYSTEM task (boot+logon), resurrects relay+ngrok every 15s, zombie-aware, public probe every 20th cycle (5m) | | `war-log/awareness.js` | AWARENESS v1.1: 5-min cycles sensing relay/watchdog/ngrok/sudo/kernels + hardware (disk/cpu/mem), self-heal (session backup 15min, bank autosave) | | `war-log/phone-health.js` | PHONE-HEALTH: 60s cycles adb presence, battery, storage, stay-awake; alerts → Didi + Ma ...
- **Engineering that matters:** 1. **Permanent Ngrok Door with Watchdog v2** — Free static domain + SYSTEM watchdog + zombie-aware resurrection + cloudflared fallback + 20th-cycle public probe 2. **Relay v4.1 with Adb Passthrough** — `/tool adb` + `/tool browser-MCP` + `/tool otp_queue` + `/agent` (5 CLI builders) + `/keys` (provider pool) — single gateway for all sons 3. **Two-Entity Voice Architecture** — Pure bytes → Kaggle CPU → base64 → soldier → base64 → Kaggle bytes → relay → ridged phone (no external TTS) 4. **DEVA ...

### `services-vfs`
- **Vertical:** Data, crawling & infrastructure | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Microservice - virtual file system

### `services-sandbox`
- **Vertical:** Data, crawling & infrastructure | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Microservice - code sandbox

### `crawlee-engine`
- **Vertical:** Data, crawling & infrastructure | JavaScript | - source lines | last push 2026-09-06
- **What it does:** Crawlee-based web crawling engine

### `services-streamer`
- **Vertical:** Data, crawling & infrastructure | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Microservice - streaming layer

### `services-deploy`
- **Vertical:** Data, crawling & infrastructure | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Microservice - deployment controller

### `services-qa-runner`
- **Vertical:** Data, crawling & infrastructure | TypeScript | - source lines | last push 2026-09-06
- **What it does:** Microservice - QA test runner


## Other engineering work

### `timeofmylife`
- **Vertical:** Other engineering work | Python | 11,422 source lines | last push 2026-09-06
- **What it does:** A **digital life archiving platform** that ingests data from multiple channels (GitHub, Git, Google Takeout, WhatsApp, LinkedIn, local files), stores with cryptographic provenance (SHA-256 + xxHash), tracks via append-only manifest (JSONL), and publishes curated deliverables (LinkedIn handbooks/playbooks). Vision: lifelong immutable digital twin.
- **Architecture:** | Component | Role | |-----------|------| | `build_all.py`, `build_playbook.py`, `build_vol1-3.py` | Volume construction (Vol I: Beyond Parameter Scaling, Vol II: Joker Corpus, Vol III: Beholder) | | `extract_all.py` | DOCX → text extraction (XML parsing) for key research documents | | `life_archive/` (package) | Core library: `connectors/`, `hash/`, `manifest/`, `indexing/`, `storage/`, `schemas/`, `db/` | | `connectors/` | Local files, Git, GitHub, Google Takeout, WhatsApp, LinkedIn | | `hash/` | Streaming SHA-256 + xxHash64 (large file support) | | `manifest/` | Append-only JSONL with forensic evidence, privacy classification | | `indexing/` | Meilisearch integration for search | | ...
- **Engineering that matters:** 1. **Multi-Connector Ingestion Pipeline** — Unified `discover→acquire→verify→hash→store→index→normalize→log` across 6+ sources 2. **Cryptographic Provenance Manifest** — Append-only JSONL with SHA-256 + xxHash64, privacy classification, forensic evidence 3. **Content-Addressed Storage** — SHA-256 prefix sharding (`sha256[:2]/sha256[2:4]/sha256`) for deduplication 4. **Privacy-by-Design Classification** — PUBLIC/PRIVATE/SENSITIVE/THIRD_PARTY_PRIVATE with default PRIVATE 5. **Idempotent Connector ...

### `api_money_bot_complete`
- **Vertical:** Other engineering work | Python | 25,254 source lines | last push 2026-09-06
- **What it does:** Revenue bot - complete API build

### `_fleet_flutter_release_attempt2_20260817`
- **Vertical:** Other engineering work | Python | 3,177 source lines | last push 2026-09-06
- **What it does:** Flutter fleet release build (attempt 2)

### `_fleet_flutter_release_20260817`
- **Vertical:** Other engineering work | Python | 9 source lines | last push 2026-09-06
- **What it does:** Flutter fleet release build

### `_live_proof_fastapi_react_20260822`
- **Vertical:** Other engineering work | TypeScript | 119 source lines | last push 2026-09-06
- **What it does:** FastAPI + React proof-of-concept

### `for-zipping`
- **Vertical:** Other engineering work | TypeScript | - source lines | last push 2026-09-06
- **What it does:** -

### `omega`
- **Vertical:** Other engineering work | Jupyter Notebook | 3,504 source lines | last push 2026-09-06
- **What it does:** OMEGA is an AI-driven software development agent that takes a user goal (e.g., "Build a React app"), plans it as a DAG of tasks, executes via tool calls (file ops, shell, web search), verifies deliverables by running install/build/test in a sandbox, iteratively fixes failures, and zips the working project. It targets **production-ready deliverables**, not advice.
- **Architecture:** | Component | Role | |-----------|------| | `omega_agent_core.py` | Backward-compat shim re-exporting `omega_agent` package symbols | | `omega_agent/` (package) | Core logic: planner (DAG), executor, MOE router, RAG, verification loop, UI (Gradio/FastAPI), tenant isolation | | `omega_agent.ui.gradio_app` | Gradio web UI for interactive use | | `omega_agent.api` | FastAPI server for programmatic access | | `omega_agent.cli` | CLI entry point | | `scripts/run_deliverable_verify_smoke.py` | End-to-end smoke test with real LLM + npm verification | | `docs/CONVERGENCE.md` | Architecture of verify→fix→converge loop | | `docs/SCALING.md` | Multitenancy and production deployment guide |
- **Engineering that matters:** 1. **Deliverable Verification Loop** — Build → verify (npm) → LLM reads stderr → patch → re-verify → converge. Rare in open-source agents. 2. **DAG Planner with Verify/ZIP Injection** — Planner generates task graph; agent injects verification/zipping tasks at runtime. 3. **MOE Router + RAG** — Mixture-of-Experts routing with retrieval-augmented context (FAISS-backed). 4. **Tenant-Isolated Workspaces** — Multi-tenancy with path-based isolation (when secured).

### `omega_sota`
- **Vertical:** Other engineering work | Jupyter Notebook | - source lines | last push 2026-09-06
- **What it does:** -

### `_live_flutter_verification_20260817`
- **Vertical:** Other engineering work | Dart | 87 source lines | last push 2026-09-06
- **What it does:** -


## Development activity

