---
week: 16
phase: Phase 4 of 6, Depth
title: Performance, Profiling and Scale
standfirst: Stop guessing. This week you measure everything, find the real bottleneck rather than the one you assumed, and fix it with evidence on both sides of the change. Then you load test until something breaks.
backend: Query tuning, profiling, load testing
frontend: Bundle, rendering, Core Web Vitals
license: Green
hours: 28 hrs
track: Capstone, sprint 4
---

## Read this first

The rule for the whole week: **no optimisation without a measurement before and after.** Developers waste enormous effort making fast things faster while a single missing index costs 800ms on every page.

The second rule: know your target. "Fast" is not a goal. "The dashboard renders in under 400ms at the 95th percentile with 100,000 records" is a goal you can succeed or fail against.

## What you are learning

### Backend performance

- Measuring first: response time percentiles, not averages. Why p95 and p99 tell the truth and the mean lies
- Finding slow queries: EF logging, SQL Server Query Store, execution plans
- Reading an execution plan enough to spot a table scan
- Indexes: covering indexes, composite index column order, included columns, and the write cost of every index you add
- The N+1 problem again, at scale, plus cartesian explosion from multiple `Include`s
- Projection: selecting only the columns you need, and why `Select` into a DTO beats loading the entity
- Split queries, `AsNoTracking`, and compiled queries
- Pagination that stays fast on page 5,000
- Async all the way down, and thread pool starvation from one blocking call
- Connection pooling, and what "timeout expired, pool exhausted" really means
- Caching layers and where each belongs: memory, distributed, HTTP, CDN
- Load testing with k6 or NBomber. Finding the point where it falls over, and how it falls over

### Frontend performance

- Measuring: Lighthouse, WebPageTest, the profiler, and real user metrics
- Bundle analysis: what is in your JavaScript and what should not be
- Code splitting by route and by interaction, dynamic imports
- Images: format, sizing, lazy loading, and layout stability
- Fonts: preloading, `font-display`, and the flash
- Server components and streaming to cut time to first byte
- Re-render elimination, and virtualising long lists
- Core Web Vitals targets: LCP under 2.5s, CLS under 0.1, INP under 200ms

## How to run your week

| Days | Focus |
|---|---|
| 1 | Instrument everything. Establish your baseline numbers and write them down. |
| 2 | Seed a realistic volume of data. Find your five slowest queries with evidence. |
| 3 | Fix them. Indexes, projections, query rewrites. Measure each fix separately. |
| 4 | Load test. Find the breaking point. Record how it fails. |
| 5 | Frontend: bundle analysis and code splitting. |
| 6 | Images, fonts, rendering, Core Web Vitals. |
| 7 | Performance report with before and after, submit. |

> **Fix one thing at a time and measure after each.** If you change five things and it gets faster, you have learned nothing about which change mattered, and you may have made something worse while something else hid it.

## Your AI licence: Green, with an evidence rule

AI is very good at explaining execution plans and suggesting index candidates. It is very bad at knowing which of your queries actually matters, because it cannot see your traffic.

**Sequence to follow:**

1. You measure and identify the real bottleneck. Yourself.
2. You bring AI the evidence: the query, the plan, the timings, the data volume.
3. AI proposes fixes with reasoning.
4. You apply one, measure, and record the result.

Good prompts:

- "Here is an execution plan showing a clustered index scan on a 2 million row table. Explain what is happening and rank three fixes by expected impact."
- "This query takes 4 seconds. Here is the schema and the plan. What index would you add and what will it cost me on writes?"
- "Here is my bundle analysis. What is likely unnecessary?"

Refuse this prompt: "make my app faster." It will produce plausible, generic, useless changes and you will have burned a day.

## The build: capstone sprint 4

### Requirements

1. Realistic data volume seeded. At minimum 100,000 rows in your largest table with proportionate related data.
2. A written baseline in `docs/performance.md`: p50, p95 and p99 for your five most important endpoints, plus Lighthouse scores and bundle size.
3. Identify the five slowest operations with evidence: the query, the plan, the timing.
4. Fix at least four of them. For each, document: the problem, the cause, the fix, the before and after numbers, and the tradeoff you accepted.
5. At least one fix must be an index, and you must state its write cost.
6. At least one fix must be a query rewrite or projection, not just an index.
7. Load test with k6 or NBomber. Report throughput, error rate and latency under load, and identify the breaking point. Describe how it fails: does it slow down, return errors, or fall over.
8. Frontend: bundle reduced measurably through code splitting, with before and after numbers.
9. Core Web Vitals: LCP under 2.5s, CLS under 0.1, INP under 200ms on your main page, measured with throttling on, not on your laptop at full speed.
10. Long lists virtualised where the row count justifies it.

### Acceptance criteria

- [ ] `docs/performance.md` has baseline and final numbers for the same five endpoints
- [ ] Each fix documented separately with its own measurement
- [ ] One index fix with the write cost stated
- [ ] One fix that is not an index
- [ ] Load test results committed, including the breaking point
- [ ] You can describe how the system behaves at 2x its breaking load
- [ ] Bundle size reduced, with the analyser output before and after
- [ ] Core Web Vitals within target under 4x CPU throttling and a slow 3G profile
- [ ] No blocking `.Result` or `.Wait()` calls anywhere in the codebase
- [ ] The app is still correct: the full test suite passes after every optimisation

## Explain it back

1. What was your slowest endpoint, and what was actually causing it? Not what you assumed.
2. Show me the execution plan before and after your index.
3. What did that index cost you on writes?
4. Why p95 rather than average?
5. At what load does your system break, and what breaks first?
6. Which optimisation did you try, measure, and then revert because it did not help?

## Stretch

- Add a read replica and route reads to it
- Add response compression and a CDN in front of static assets
- Add continuous performance checks to CI that fail the build on a regression

## Resources

- Use The Index, Luke, in full
- Microsoft Learn: EF Core performance, and SQL Server Query Store
- web.dev performance section, and the k6 documentation
