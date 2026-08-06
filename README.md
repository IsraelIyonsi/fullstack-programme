# Full Stack Engineering Programme

Twenty-four weeks, zero to intermediate full stack engineer. .NET and C# on the backend,
React and Next.js on the frontend, redesigned around the fact that students now have AI.

This repo is the **source** of the programme. The PDFs students receive are generated from it.

## What is here

| Path | What it is |
|---|---|
| `content/week-00.md` to `week-24.md` | The 25 weekly briefs. The source of truth for everything else |
| `build/build_pdfs.py` | Renders the briefs to A4 PDFs and zips them for handout |
| `build/print.css` | The print stylesheet |
| `build/gen_seed.py` | Generates the cohort tracker's database seed from the same briefs, so the tool can never drift from the paper |
| `deck/journey.html` | The programme overview deck |
| `deck/dashboard.html` | High fidelity design for the cohort tracker |
| `tasks/` | Plan, lessons, and the dashboard design notes |

`dist/` is generated and deliberately not tracked.

## Rebuilding the PDFs

```bash
python3 build/build_pdfs.py            # all 25
python3 build/build_pdfs.py week-07    # just one
```

Requires `weasyprint` (`brew install pango` first, or it fails on a missing native library).
Output lands in `dist/pdfs/` with a zip at `dist/fullstack-programme-export.zip`.

## Regenerating the tracker's seed

```bash
python3 build/gen_seed.py
```

Writes `../cohort/supabase/seed.sql`: 25 weeks and 243 acceptance criteria, taken straight
from the briefs. Run it whenever a brief changes, then `supabase db reset` in the tracker.

## The shape of the programme

Six phases: fundamentals, persistence and APIs, production concerns, depth, AI engineering,
then ship and get hired. Two projects carry it: a school management system from week 3 to 12,
then a capstone from week 13.

Two rules run through all of it.

**Nothing counts as done until you can explain it out loud with the editor closed.**

**The AI licence.** Red in weeks 1 to 4, where AI is a tutor and never a typist. Yellow in
weeks 5 to 12, where it writes boilerplate and the student writes the thinking. Green from
week 13, where it implements and the student reviews. That last tier is the actual job.

## Still to build

- The week 14 cold-codebase repository with a ticket, referenced in the brief as if it exists
- The week 18 repository with planted defects for the review assessment

The tracker that marks all of this lives at [IsraelIyonsi/cohort](https://github.com/IsraelIyonsi/cohort).
