---
description: Protocol for selecting the correct model tier and the enforced workflows per tier (Bento Box, Auto-router).
trigger: model_decision
---

# 1. Model Tier Classification & Routing
# Model Tier Protocol

## 0. Tier Classification Heuristics (Read First)

> **Auto-Router**: Before choosing a tier, answer these questions in order. Stop at the first match.

| Question | Yes → Tier |
| :--- | :--- |
| Can I describe the full change in 1 sentence and it touches only 1 file? | `BUDGET` |
| Does the change require reading state from >1 file to understand impact? | `STANDARD` |
| Does it touch auth, RLS, global config, or cross-system architecture? | `PREMIUM` |
| Am I unsure which tier applies? | Escalate to `STANDARD`, declare why. |

**Golden Rule**: When defaulting to `STANDARD`, you MUST explicitly state which heuristic forced it. Silent default to STANDARD is a protocol violation.

> **Anti-Deliberation Clause**: If you need to *read a file to determine* whether the task qualifies as BUDGET, the task is already STANDARD. BUDGET classification must be immediately obvious from the task description alone — no investigation required.

---

## 1. The Three Tiers (Calibrated)

| Tier | Label | Practical Scope | When to Use |
| :--- | :--- | :--- | :--- |
| **Tier 0** | `BUDGET` | **Atomic / Stylistic** | Documentation, log updates, formatting, minor CSS/styling, single-file bug fixes (localized logic), basic boilerplate generation, basic unit test additions. |
| **Tier 1** | `STANDARD` | **Integrative / Feature** | Multi-file feature implementation, domain-specific state management, complex bug fixes spanning multiple modules, registry maintenance (`catalog.json`, `workspace_map.md`). |
| **Tier 2** | `PREMIUM` | **Architectural / Risky** | Global system refactors, security/Auth/RLS logic changes, high-risk infrastructure updates, deep performance bottleneck resolution. |

## 2. Infrastructure Special Note
- **Don't Over-Classify**: Modifying files inside `.agents/` is NOT automatically `PREMIUM`.
- If the change is purely about keeping the registry/map up to date, use `STANDARD`.
- If the change modifies the *logic* of how agents operate (e.g., changing `core-guardrails.md`), use `PREMIUM`.

## 3. Mandatory Declaration & Manual Routing (Anigravity IDE)
- Karena **Anigravity IDE** tidak memiliki fitur *auto-routing* model, pergantian model harus dilakukan secara **MANUAL** oleh pengguna.
- Sebelum memulai *Tier-1+ task* atau mengeksekusi *tools* manipulasi file, agen **WAJIB** membuat Rencana Implementasi singkat dan mendeklarasikan: `[TIER: STANDARD]` atau `[TIER: PREMIUM]` beserta model yang direkomendasikan.
- **Auto-Abort Pre-Execution (Safety Gate)**: Jika agen saat ini berjalan di model *BUDGET/Small* tapi hasil kalkulasi deterministik menuntut *PREMIUM*, agen harusk mengeluarkan sinyal `[ABORT: TIER MISMATCH - HARAP GANTI MODEL LALU ULANGI PROMPT]`.
- **In IDE/Anigravity mode**: Tuliskan ini di bagian atas `implementation_plan.md` atau pesan *Binary Oratory*. Setelah menuliskannya, **BERHENTILAH**. Jangan jalankan perbaikan file/tools apapun. Tunggu konfirmasi `[DO: YES]` (jika model sudah memadai) atau *Retry* (setelah ganti model).
- Ini memberi kesempatan kepada pengguna untuk **mengganti Chat Agent (Model) di dropdown IDE** (misalnya pindah dari Gemini Flash ke Gemini Pro/Claude Sonnet) khusus untuk eksekusi tersebut.
- **BUDGET tasks** DO NOT require Binary Oratory pre-flight. Dapat dieksekusi langsung jika model yang aktif saat ini sudah memadai.

## 4. Forced Intelligence Per Tier (Capability Harness)

The following constraints are **mandatory per tier**, not optional. They prevent lazy or "sloppy" outputs at each level.

### BUDGET: Micro-Harness Protocol
Even simple tasks MUST satisfy the following Lightweight Validation Gate before output is accepted:
1. **Scope Confirmation** (1 sentence): State what the task is in plain English. No more, no less.
2. **Constraint Declaration** (1-3 bullets): What CANNOT be changed or broken. Serves as a self-injected guardrail.
3. **Zero-Theater Execution**: Perform the action immediately. No preamble, no narrative justification.
4. **Self-Verification Micro-Check**: After execution, confirm the output satisfies the original scope (e.g., "File updated. Key: X changed to Y. No other lines modified.").
- **Token Ceiling**: BUDGET tasks MUST NOT read more than 1 file in full. Use `grep_search` for targeted extraction.
- **Prohibited Actions in BUDGET**: No Sequential Thinking calls, no multi-file reads, no architectural scope expansion.

### STANDARD: Lightweight Planning Gate
Before any execution:
1. State the implementation approach in ≤3 sentences.
2. List files to be touched.
3. Identify 1-2 risk points.

Then execute in parallel where possible (Turn Minimization).

After implementation, **before marking as done**: apply the Adversarial Twin Protocol (`reasoning-standards.md`). Declare `"Swapping to Breaker Persona."` and run at least 1 attack vector against the output.

### PREMIUM: Full Sequential Thinking Mandate
See `reasoning-standards.md` for the full protocol. Sequential Thinking with minimum 3 thought steps is **mandatory, not optional**.

## 5. Escalation & Transition Rules
- **Escalation**: If a task initially classified as `STANDARD` reveals unexpected complexity mid-execution (e.g., a simple script tweak breaks the entire graph), PAUSE and re-declare as `PREMIUM`.
- **BUDGET → STANDARD Escalation Trigger**: If a "single-file fix" requires understanding of state shared across >2 files, escalate to `STANDARD`.
- **Downgrade (Phase-Based)**: Permitted ONLY between distinct implementation phases (e.g., move to `STANDARD` for UI after a `PREMIUM` architecture phase).
- **No Silent Downgrades**: All tier changes MUST be explicitly declared.

## 6. Token Economy Rules Per Tier
| Tier | Max File Reads | Preferred Read Mode | Parallel Tool Calls |
| :--- | :--- | :--- | :--- |
| `BUDGET` | 1 (targeted grep preferred) | `grep_search` > `view_file` (header only) | Allowed |
| `STANDARD` | 3-5 (surgical sections) | `view_file` with line range | Mandatory for independent steps |
| `PREMIUM` | Unlimited (justified) | Full reads when necessary | Mandatory |

## 7. Deterministic Tier Fallback (Anti-Subjectivity)
When classification is ambiguous, use this deterministic fallback:

1. Count impacted files.
2. Count cross-domain boundaries (rules, scripts, workflows, security, deployment).
3. Select tier:
	- `BUDGET`: 1 file and 0 cross-domain boundaries.
	- `STANDARD`: 2-5 files or 1 boundary.
	- `PREMIUM`: >5 files or 2+ boundaries or any security/deployment risk.

If the declared tier is lower than this fallback result, escalation is mandatory.

## 8. Governance Evidence Block
For Tier-1+ execution, the pre-flight declaration MUST include:

- `Heuristic Match`: Which table row triggered classification.
- `Fallback Score`: File count + boundary count.
- `Escalation Check`: `PASS` or `FAIL`.

## 9. Small Model Superiority Suite
Jika bertindak menggunakan **BUDGET Model**, agen **WAJIB** mematuhi triad arsitektur berikut untuk mencegah halusinasi:
1. **Context Diet Protocol (`context-standards.md`)**: Wajib *Skeleton-First* (Grep/AST), dilarang *full-read* pada file yang panjang untuk menghindari *context poisoning*.
2. **Bento-Box Workflow (`tier-execution-protocol.md`)**: Wajib *State-Machine* tunggal. Satu target, satu evaluasi. Dilarang melakukan manipulasi multi-file secara simultan.
3. **Micro-Canons (`canons/micro/README.md`)**: Wajib membaca ringkasan domain (*framework rules*) sebelum mulai berpikir jika menangani teknologi spesifik, sebagai pengganti kelemahan *pre-trained data* dari model kecil.

# 2. Bento-Box Workflow (Anti-Multitasking for Budget Models)
# Bento-Box Workflow (Anti-Multitasking)

## 1. The Core Problem
Small models fail acutely when attempting *Zero-Shot Planning* for multiple tasks at once. Jika disuruh "Buat UI, sambungkan ke DB, dan buat tes", model akan mencampuradukkan logika, membuat sintaks yang terpotong, atau berhalusinasi parah.

## 2. The Bento-Box Law (Satu Sekat, Satu Rasa)
Ketika sebuah eksekusi dilakukan oleh **[TIER: BUDGET]**, *multitasking* secara statis adalah ILEGAL. Agen **WAJIB** menerapkan *State-Machine Berhenti Paksa*:

1. **Aturan Satu Berkas:** Agen hanya boleh memanipulasi *satu* target per iterasi (Satu file dibuat/diedit).
2. **Hard Pause (Berhenti Paksa):** Setelah satu aksi selesai, agen harus memicu evaluasi/lint/uji coba terhadap *satu* perubahan itu saja. 
3. **No Batching:** Dilarang melempar 3 *tool calls* `create_file` atau `replace_string` secara paralel jika tugas tersebut memengaruhi arsitektur logika. (Kecuali sekadar refactor nama yang deterministik).

## 3. Eksekusi Sekuensial
Bagi tugas menjadi sekat-sekat isolasi (Bento-Box):
- Kotak 1: Buat *Skeleton Interface*. Selesai. Lapor.
- Kotak 2: Isi *Business Logic*. Selesai. Lapor.
- Kotak 3: Hubungkan ke *UI*. Selesai. Lapor.

Setiap penyelesaian "Kotak" harus dipastikan bisa berjalan murni tanpa bergantung pada kotak yang belum dikerjakan. Jika model budget merasa tugasnya terlalu berlapis, wajib langsung memanggil mekanisme *Auto-Abort* dan meminta *Premium Model*.
