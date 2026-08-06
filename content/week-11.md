---
week: 11
phase: Phase 3 of 6, Production Concerns
title: The Things Real APIs Have
standfirst: Pagination, filtering, caching, rate limiting, structured logging, configuration, secrets and health checks. None of it is glamorous and all of it is the difference between a portfolio project and something you can put in front of users.
backend: Logging, caching, rate limiting, config
frontend: Forms at scale, tables, a11y
license: Yellow
hours: 28 hrs
track: School Management, part 8
---

## Read this first

Every feature you have built so far assumed a cooperative user, a fast network and a small dataset. This week you remove all three assumptions.

The specific skill to develop: when something goes wrong at 2am, can you find out what happened from your logs alone, without attaching a debugger? If not, your logging is decoration.

## What you are learning

### Backend

- Structured logging with Serilog: message templates, properties, sinks, enrichers
- Log levels used correctly. Information is not for everything
- Correlation ids: tracing one request across every log line it produced
- What never goes in a log: passwords, tokens, full card numbers, personal data you do not need
- Global exception handling that returns `ProblemDetails` and logs the detail internally
- Configuration layering: appsettings, environment specific files, environment variables, user secrets
- Secrets management. Nothing sensitive in source control, ever. Check your git history too
- Response caching, output caching and `IMemoryCache`. Cache keys, expiry and invalidation
- Distributed caching with Redis, and the cache stampede problem
- Rate limiting in ASP.NET Core: fixed window, sliding window, token bucket, and per-user partitioning
- Health checks: liveness versus readiness, and checking your dependencies
- Compression, and pagination that scales past offset paging with cursors

### Frontend

- `react-hook-form` with `zod` for schema validation shared between form and API types
- Complex forms: multi-step, conditional fields, array fields, unsaved changes warnings
- Data tables at scale: server side pagination, sorting and filtering wired to your API
- URL as state: filters in the query string so a filtered view is shareable
- Debouncing search input and cancelling in-flight requests
- Accessibility: keyboard navigation, focus management, labels, `aria-live` for async results, colour contrast
- Toast notifications and inline errors, and when each is right

## How to run your week

| Days | Focus |
|---|---|
| 1 | Serilog, correlation ids, log levels. Make one request and read its full trace. |
| 2 | Configuration and secrets. Move everything sensitive out of the repo and out of history. |
| 3 | Caching and rate limiting. Measure the before and after. |
| 4 | Health checks, compression, cursor pagination on the largest list. |
| 5 | Frontend forms with react-hook-form and zod. |
| 6 | Server side table: paging, sorting and filtering through the URL. Accessibility pass. |
| 7 | Load a large dataset, find what breaks, document it, submit. |

> **Seed 50,000 students this week.** Then open the directory page. Whatever breaks, breaks in production too, just later and in front of someone who matters. Fix it now while it costs you an afternoon.

## Your AI licence this week: Yellow

This is a strong week for AI because most of it is well-trodden configuration.

- "Set up Serilog with a correlation id enricher and explain each piece."
- "Here is my logging. What sensitive data am I leaking?"
- "Design a caching strategy for these three endpoints. Where will it go stale and what invalidates it?"
- "Review this zod schema against my API contract and find mismatches."
- "Audit this component for accessibility issues and tell me which are real blockers versus nits."

The one thing to do yourself: decide **what** to cache and **when** to invalidate. AI does not know your data's staleness tolerance and will guess.

## The build: School Management System, part 8

### Backend requirements

1. Serilog writing structured logs to console and to a rolling file, with environment, request path and correlation id on every entry.
2. A correlation id created per request, returned in a response header, and shown to the user in error messages so support can trace it.
3. Zero secrets in the repository. Connection strings and signing keys from user secrets locally and environment variables elsewhere. Confirm nothing sensitive exists in git history.
4. `IMemoryCache` on at least two read-heavy endpoints, with a documented expiry and an explicit invalidation on the relevant write.
5. Rate limiting: 100 requests per minute per user on general endpoints, 5 per minute on login. Exceeding it returns 429 with a `Retry-After` header.
6. Health check endpoint reporting the API, the database and the cache. Returns unhealthy when the database is stopped. Verify by stopping it.
7. Cursor based pagination on the students endpoint, alongside the existing offset paging, with a written note on when each is appropriate.
8. Seed 50,000 students and 200,000 enrolments. Record the response time of your three slowest endpoints before and after your fixes.

### Frontend requirements

1. All forms migrated to react-hook-form with zod schemas. The schemas live in one shared place.
2. A multi-step enrolment form with a review step and the ability to go back without losing data.
3. Unsaved changes warning when navigating away from a dirty form.
4. The students table does server side paging, sorting and filtering, all reflected in the URL.
5. Search is debounced at 300ms and cancels superseded requests.
6. Full keyboard operability: you can complete the enrolment journey without a mouse. Test it for real.
7. Accessibility pass: labels on every input, focus visible, async results announced, no contrast failures on your primary flows.

### Acceptance criteria

- [ ] One request produces log lines that share a single correlation id, from entry to exit
- [ ] An error shown to the user includes a reference you can grep for in the logs
- [ ] No password, token or connection string appears anywhere in the logs
- [ ] `git log -p` search for your connection string returns nothing
- [ ] Six failed logins in a minute returns 429 with `Retry-After`
- [ ] Stopping the database makes `/health` report unhealthy within seconds
- [ ] The directory page loads in under 500ms with 50,000 students, and you can show the numbers
- [ ] Copying the URL of a filtered, sorted, page-3 table and opening it in a new tab reproduces the exact view
- [ ] The enrolment journey is completable with keyboard only
- [ ] A before and after performance table is in the README
- [ ] `ai-log.md` updated

## Explain it back

1. Walk me through everything you log for a single failed enrolment attempt.
2. What do you cache, for how long, and what invalidates it?
3. What is the failure mode when your cache and your database disagree?
4. Why rate limit login more aggressively than everything else?
5. When is cursor pagination better than offset, and what does it cost you?
6. Show me a form and tell me what a screen reader user hears when validation fails.

## Stretch

- Add Redis and move the cache to it, then handle a Redis outage gracefully
- Add OpenTelemetry traces and view them in Jaeger
- Add a feature flag system and ship one feature behind it

## Resources

- Serilog docs, and Microsoft Learn on logging in .NET
- Microsoft Learn: rate limiting middleware, health checks, caching
- react-hook-form and zod docs. WebAIM on form accessibility
