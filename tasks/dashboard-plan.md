# Cohort Dashboard: the simplest thing that works

## Scope discipline
This is a **marking and follow-up tool**, not an LMS. It does not host content, run video, or do forums.
The PDFs are the content. This tracks who did the work, how good it was, and who is slipping.

Four jobs only:
1. Show me where every student is, right now, at a glance.
2. Tell me what is waiting for me to mark.
3. Let me mark it fast, against the same rubric every time.
4. Tell me who is at risk before they disappear.

## Stack
- **Supabase**: Postgres + Auth + Row Level Security + Storage (the week PDFs and any attachments).
- **Next.js 15 (App Router) + TypeScript + Tailwind**, deployed on Vercel.
- Supabase client with RLS doing the authorisation. No custom API layer for v1.
- Nice side effect: the students are learning this exact stack, so the dashboard is a live reference for them.

## Data model (10 tables)

```
cohorts          id, name, starts_on, ends_on, active
profiles         id (= auth.users.id), full_name, email, role (admin|instructor|student), avatar_url
enrolments       id, cohort_id, student_id, status (active|paused|withdrawn), joined_on
weeks            id, week_no (0-24), title, phase, ai_licence (red|yellow|green), pdf_path
cohort_weeks     id, cohort_id, week_id, opens_on, due_on          -- the schedule
criteria         id, week_id, position, text                        -- acceptance criteria from the PDF
submissions      id, cohort_week_id, student_id, repo_url, ai_log_url, notes,
                 status (missing|submitted|late|returned|graded), submitted_at
criteria_checks  id, submission_id, criterion_id, met (bool), comment
marks            id, submission_id, build, explain_back, tests, review_given,   -- 0-5 each
                 total, verdict (pass|resubmit|fail), feedback, marked_by, marked_at
peer_reviews     id, submission_id (target), reviewer_id, findings, quality (0-5)
flags            id, student_id, kind (silent|missed|declining|at_risk), note, opened_at, closed_at
```

**One derived view** `v_student_progress` (student x week, status, score) powers the whole matrix. Everything else is a filter on it.

## Rubric, fixed for all 24 weeks
Four dimensions, 0 to 5, total out of 20. Same every week so trends are comparable.

| Dimension | What it measures |
|---|---|
| Build | Acceptance criteria met, code quality |
| Explain-back | The live session. Can they defend it with the editor closed |
| Tests | From week 8. Do the tests fail when the feature is broken |
| Review given | Quality of reviews they gave others that week |

Verdict is pass / resubmit / fail. Anything under 10 auto-opens an at-risk flag.

## RLS in one line each
- Student: `select` own submissions, marks, flags. `insert/update` own submission until it is graded.
- Instructor: everything within cohorts they teach.
- Admin: everything.

## Screens (four, that is all)
1. **Cohort overview** — progress matrix (students down, weeks across), KPI row, marking queue, at-risk list.
2. **Marking sheet** — one submission: repo link, criteria checklist, ai-log, 4 rubric sliders, feedback, verdict.
3. **Student detail** — 24-week timeline, score trend, flags, submission history.
4. **Student's own view** — this week's brief, submit form, my marks, my history.

## Build order
1. Supabase project, schema, RLS, seed the 25 weeks + criteria from the PDF frontmatter.
2. Auth + roles + the progress view.
3. Cohort overview (read-only) — this alone is 70% of the value.
4. Marking sheet with the rubric.
5. Student submit view.
6. Flags, then a weekly digest email of who has not submitted.

Roughly 2 to 3 weeks of evenings. It is deliberately small.
