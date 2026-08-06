# Cohort: build plan

## Architecture

**One Next.js app, Supabase for everything else.** No custom API layer. RLS is the authorisation.

```
~/cohort
  supabase/
    migrations/       0001_schema.sql, 0002_rls.sql, 0003_functions.sql
    seed.sql          25 weeks + acceptance criteria, generated from the curriculum markdown
  src/
    app/
      (auth)/login, (auth)/signup          public
      (app)/dashboard                      student: this week, submit, history
      (app)/weeks/[no]                     the brief + criteria + my submission
      (staff)/cohort                       instructor: matrix, marking queue
      (staff)/mark/[submissionId]          marking sheet
    lib/supabase/     client.ts, server.ts, middleware.ts
    components/
  middleware.ts       session refresh + route protection
```

**Why local Supabase first:** `supabase start` runs the whole stack in Docker with no cloud
credentials. Migrations are plain SQL, so moving to a hosted instance later is
`supabase link` then `supabase db push`. Nothing is thrown away.

## Auth and user management

- Email + password via Supabase Auth.
- **Signup is gated by a cohort enrolment code.** Without a valid code you cannot create an
  account, so the URL can be public without letting strangers in.
- A trigger on `auth.users` insert creates the `profiles` row and the `enrolments` row,
  reading the cohort from the signup metadata. Server-side, so it cannot be spoofed by the client.
- `profiles.role` is `student | instructor | admin`. Default student. Only an admin can change it.
- Middleware refreshes the session and blocks unauthenticated access to everything under `(app)`
  and `(staff)`; the staff group additionally checks role.

## RLS, one line each

| Table | Student | Instructor |
|---|---|---|
| profiles | read own, update own name/avatar | read all in their cohorts |
| enrolments | read own | read all in their cohorts |
| weeks, criteria | read all | read all |
| cohort_weeks | read own cohort's, only if `opens_on <= now()` | read all |
| submissions | read own, insert own, update own **until graded** | read + update in their cohorts |
| criteria_checks, marks | read own (once released) | full within their cohorts |

## Build order

1. [x] Toolchain check
2. [ ] Docker up, `supabase init`, `supabase start`
3. [ ] Migration: schema
4. [ ] Migration: RLS + signup trigger
5. [ ] Seed: 25 weeks and their acceptance criteria, generated from `content/week-*.md`
6. [ ] Next.js scaffold, Tailwind, Supabase SSR clients, middleware
7. [ ] Signup with enrolment code, login, logout
8. [ ] Student dashboard: current week, submit assignment, history
9. [ ] Verify end to end: real signup, real submission, RLS proven by trying to read someone else's
10. [ ] Instructor: cohort matrix and marking queue (next slice)

Stop point for this session: a student can sign up with a code, log in, see their current
week, submit an assignment, and cannot see anyone else's data.
