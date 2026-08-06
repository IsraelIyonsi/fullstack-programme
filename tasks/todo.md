# Full Stack 6-Month Bootcamp: Build Plan

## Deliverables
1. **Journey deck** (Artifact, shareable link): visual overview of the 24-week journey, phases, tracks, AI license tiers, capstone.
2. **24 weekly PDFs**, one per week, each containing: topics to learn, instructions, AI rules, the full-stack task, definition of done.
3. **Zip** of all PDFs, broken down by week, ready to hand to students.

## Structure
```
~/fullstack-bootcamp/
  build/           template.html, print.css, build_pdfs.py
  content/         week-01.md ... week-24.md
  dist/pdfs/       Week-01-....pdf ... Week-24-....pdf
  dist/fullstack-bootcamp-curriculum.zip
  deck/            journey deck source (published as Artifact)
```

## Tasks
- [x] Confirm PDF toolchain (weasyprint present)
- [x] Write build pipeline (markdown -> styled HTML -> PDF)
- [x] Write & render Week 01, verify layout before scaling
- [x] Write Weeks 02-04 (Phase 1: Fundamentals, Red AI license)
- [x] Write Weeks 05-08 (Phase 2: Persistence & APIs, Yellow license)
- [x] Write Weeks 09-12 (Phase 3: Production concerns)
- [x] Write Weeks 13-18 (Phase 4: Depth, Green license)
- [x] Write Weeks 19-22 (Phase 5: AI engineering + capstone)
- [x] Write Weeks 23-24 (Phase 6: Ship & get hired)
- [x] Render all 24 PDFs, spot-check
- [x] Zip
- [x] Build + publish journey deck Artifact

## Voice rules (non-negotiable)
- No em dashes or en dashes anywhere.
- No LLM tells: delve, robust, seamless, leverage, "in today's fast-paced", "it's not just X, it's Y".
- Instructor voice: direct, second person, imperative. Short sentences.
- Every task has concrete acceptance criteria, not vibes.

## Review

**Delivered**
- 25 PDFs (Week 00 handbook + Weeks 01 to 24), A4, styled, phase-coloured, running footers.
  Every week carries: topics (backend/frontend/cross-cutting), a day-by-day plan, the AI licence
  for that week, the full-stack build spec, tickable acceptance criteria, explain-it-back
  questions, stretch goals, resources.
- `dist/fullstack-programme-export.zip` (899 KB, 29 files): the PDFs plus both HTML pages,
  the dashboard plan and a README for handing it out.
- Journey deck published as an Artifact (scroll/arrow-key slides, light + dark).
- Cohort dashboard high-fidelity design published as an Artifact, plus `tasks/dashboard-plan.md`.

**Build notes**
- weasyprint needed `brew install pango`; poppler installed for page previews during layout checks.
- Checklists (`- [ ] ...`) are preprocessed into styled checkbox lists in `build_pdfs.py`.
- To regenerate: `python3 build/build_pdfs.py` (all) or `python3 build/build_pdfs.py week-07` (one).
- Verified: zero em/en dashes across all content and templates.

**Open decisions for Israel**
- Cohort size, start date and session cadence are not encoded anywhere yet.
- The week-14 "cold codebase" and week-18 "planted defect" repos still need to be written.
- Capstone approval criteria are described but not yet a form.
