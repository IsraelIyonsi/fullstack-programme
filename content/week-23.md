---
week: 23
phase: Phase 6 of 6, Ship and Get Hired
title: Production Readiness and Operating What You Built
standfirst: The difference between a deployed app and a production system is what happens when it breaks at 3am. Monitoring, alerting, backups, incident response and a runbook. This week you also break your own system on purpose and practise recovering.
backend: Monitoring, alerting, backup, recovery
frontend: Error tracking, real user monitoring
license: Green
hours: 26 hrs
track: Capstone, production readiness
---

## Read this first

Ask yourself one question: if your app went down right now while you were asleep, how would you know, and how long would it take to fix?

If the answer is "a user would tell me" and "I do not know", you have a project, not a product. This week closes that gap, and it is the part of your portfolio that most reliably impresses an interviewer, because almost no junior candidate has it.

## What you are learning

### Observability

- The three pillars: logs, metrics and traces, and what each answers
- Metrics that matter: request rate, error rate, duration, saturation
- Service level objectives: choosing a target, measuring against it, and error budgets
- Dashboards that answer questions rather than showing every number available
- Alerting on symptoms your users feel, not on causes. Alert on error rate, not on CPU
- Alert fatigue, and why an alert nobody acts on should be deleted
- Frontend error tracking with Sentry or similar, including source maps so stack traces are readable
- Real user monitoring, and why your laptop's numbers are not your users' numbers
- Uptime checks from outside your own infrastructure

### Operations

- Backups: automated, tested, and offsite. A backup you have never restored is not a backup
- Restore drills, with the time to restore recorded
- Disaster recovery: recovery point objective and recovery time objective, chosen deliberately
- Zero downtime deployment, and migrations that are safe to run against a live system
- The expand and contract pattern for breaking schema changes
- Rollback, including rolling back a database migration
- Incident response: detect, communicate, mitigate, then fix. Mitigation before diagnosis
- Blameless post-mortems and what makes them useful
- On-call basics and the runbook that makes it survivable

## How to run your week

| Days | Focus |
|---|---|
| 1 | Metrics and dashboards. Instrument request rate, error rate and duration. |
| 2 | Alerting. Define your SLOs, then alert on breaching them. Route to your phone. |
| 3 | Frontend error tracking with source maps, and real user monitoring. |
| 4 | Backups and a real restore drill, timed. |
| 5 | Zero downtime deploy and a safe migration using expand and contract. |
| 6 | **Chaos day.** Break your own system four ways and practise recovery. |
| 7 | Runbook, post-mortem write-up, submit. |

> **Chaos day is the point of this week.** Kill the database. Fill the disk. Make the third party API hang forever rather than fail fast, which is worse. Deploy a broken build to production. For each: how long until you noticed, how you found out, how long to recover. Those four numbers are your real operational maturity.

## Your AI licence: Green, and excellent for the runbook

Two very strong uses this week.

**Runbook generation from your real system:**

- "Here is my architecture and my dependencies. What should a runbook cover for this system?"
- "Write a diagnostic checklist for 'the site is slow' against this stack, ordered by how quickly each check rules something out."

**Incident support, which is what this looks like in a real job:**

- "Production is returning 502s. Here are the last 200 log lines and the deploy history. Give me five ranked hypotheses and the fastest check for each."

That prompt shape is genuinely valuable during a live incident. Practise it on chaos day so it is a familiar tool rather than a panicked experiment. Note what it got right and wrong in your write-up.

## The build: make it operable

### Requirements

1. Metrics collected and dashboarded for request rate, error rate, response time percentiles, and one business metric that matters for your product.
2. Two SLOs defined with reasoning, for example availability and latency, with the current numbers measured against them.
3. Alerts that reach your phone, firing on SLO breach and on the app being unreachable. Fewer than five alerts total, each with a documented action.
4. Frontend error tracking with source maps uploaded, so an error shows a readable stack trace. Verified with a deliberate error.
5. Uptime monitoring from outside your infrastructure.
6. Automated daily database backup, with retention. A restore performed for real into a clean environment, with the elapsed time recorded.
7. A stated recovery point objective and recovery time objective, with evidence that you meet them.
8. Zero downtime deployment demonstrated: a deploy performed while traffic is flowing, with no failed requests, proven by a load generator running during the deploy.
9. One breaking schema change delivered safely using expand and contract, with the steps documented.
10. `docs/runbook.md` covering: architecture, dependencies, how to deploy, how to roll back, where logs and dashboards are, the top five likely failures and their fixes, and who to contact.
11. `docs/chaos-day.md` documenting four deliberate failures with detection time, discovery method, recovery time and what you changed as a result.
12. One blameless post-mortem written properly for the worst of the four.

### Acceptance criteria

- [ ] A dashboard exists that answers "is the app healthy right now" in five seconds
- [ ] Stopping the app produces an alert on your phone within two minutes
- [ ] A deliberate frontend error appears in your error tracker with a readable stack trace
- [ ] A database restore was performed for real, with the time recorded
- [ ] A deploy under live traffic produced zero failed requests, with evidence
- [ ] A breaking schema change was shipped with no downtime, with the steps documented
- [ ] The runbook lets someone else recover your system without you
- [ ] Four chaos experiments documented with all four numbers each
- [ ] A post-mortem written with a timeline, root cause, and action items
- [ ] No alert exists that you would ignore

## Explain it back

1. Your app is down. Walk me through your first five minutes.
2. What are your SLOs and are you currently meeting them?
3. When did you last restore a backup and how long did it take?
4. What is expand and contract, and which change did you use it for?
5. On chaos day, which failure took longest to notice and why?
6. Which alert did you delete, and why was it worse than no alert?

## Stretch

- Add distributed tracing to the dashboard so a slow request is traceable end to end
- Add automated rollback triggered by an error rate spike after deploy
- Add a status page for your users

## Resources

- Google SRE Book, chapters on SLOs, monitoring and incident response. Free online
- Your hosting provider's documentation on backups, scaling and zero downtime deploys
- Read two published post-mortems from real companies. Notice they blame systems, not people
