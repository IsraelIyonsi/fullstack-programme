---
week: 21
phase: Phase 5 of 6, AI Engineering
title: Capstone Sprint, Working Like a Team
standfirst: Two weeks of pure building, run the way a real engineering team runs. Standups, a groomed backlog, pull requests reviewed by peers, a demo on Friday and a retrospective. Your code stops being homework and starts being work.
backend: Feature delivery
frontend: Feature delivery
license: Green
hours: 32 hrs
track: Capstone, sprint 6
---

## Read this first

You have the skills. This week is about the professional habits that surround them: estimating, breaking work down, unblocking yourself, communicating status honestly, reviewing others, and finishing.

The single hardest habit for a junior is the last one. Ninety percent finished is not finished. Work is done when it is merged, deployed, tested and documented, not when the code exists.

## What you are learning

- Breaking a feature into tickets small enough to finish in a day
- Writing a ticket someone else could pick up: context, acceptance criteria, out of scope
- Estimating, being wrong, and communicating the revision early rather than on the deadline
- A standup that is useful: what moved, what is next, what is blocking, in ninety seconds
- Raising a blocker within an hour instead of at the end of the day
- Reviewing pull requests with substance, and receiving review without defensiveness
- Trunk based development or short lived branches, and merging daily
- Definition of done, applied strictly
- Demoing work to a non-technical audience
- Retrospectives that produce one change rather than a list of complaints

## How the two weeks run

This week and next are a single sprint, run to a schedule you will be held to.

| Day | Ritual |
|---|---|
| Monday | Sprint planning. Backlog groomed, tickets estimated, sprint goal agreed and written down. |
| Daily | Standup, 15 minutes, hard stop. Blockers raised go on the board. |
| Wednesday | Mid-sprint check. Scope adjusted honestly if the estimate was wrong. |
| Friday | Demo to the group, then retrospective producing exactly one change to try. |
| Continuous | Every change goes through a PR. Two peer approvals before merge. Nothing merges with a red build. |

> **Merge daily.** A branch that lives for five days is a conflict, a stale review and a bad merge waiting to happen. Small pieces, merged often. If a feature is too big to merge daily, put it behind a flag and merge the parts.

## Your AI licence: Green, at full professional speed

This week is the closest simulation of the job you are about to do. Use AI the way a strong engineer does.

**The workflow:**

1. Ticket in hand. You write the technical approach in three or four sentences, in the ticket, before any code.
2. You delegate implementation with a proper spec.
3. You review the output hard, run it, test the edges.
4. You write or extend the tests, and you check that they fail against the broken version.
5. You open a PR describing what you did and why, and you disclose what was generated.

**What is being assessed:** the quality of your specs, the quality of your reviews, and whether your PRs are small enough to actually be reviewed.

**The failure mode to avoid:** generating a 900 line PR that works, that nobody can review properly, and that you cannot fully explain. That PR will be rejected in this programme and it will damage your reputation in a job.

## The build: capstone sprint 6

### Requirements

1. A groomed backlog on a real board, with every ticket carrying acceptance criteria.
2. A written sprint goal that is a user outcome, not a task list.
3. Every piece of work through a PR with two peer approvals and a green build.
4. No PR over 400 lines of change without a written reason.
5. Daily standup notes recorded.
6. At least three substantive reviews given to other students, each finding something real.
7. A Friday demo of working software, five minutes, to a non-technical audience. No slides, live app, and a plan for what to do when it breaks in front of everyone.
8. A retrospective note recording one change to make next week, and next week you must show you made it.
9. All of this while your test suite, your CI and your deploy stay green. A broken main branch is a sprint failure.

### The features to land this sprint

Whatever your capstone needs, but by Friday it must be true that:

- A new user can sign up, get to the core value of your product, and complete the main journey without help
- The three headline features from your proposal are complete, not partially complete
- Everything merged is deployed and reachable at your live URL
- The app is usable on a phone

### Acceptance criteria

- [ ] Sprint goal written and visible, phrased as a user outcome
- [ ] Every ticket has acceptance criteria written before work started
- [ ] Zero direct commits to main
- [ ] Every PR has two approvals and a green build before merge
- [ ] No unexplained PR over 400 lines
- [ ] Standup notes for every day
- [ ] Three substantive reviews given, each with a real finding
- [ ] Demo delivered live, on the deployed app
- [ ] Retrospective note with exactly one committed change
- [ ] Main branch green every single day of the sprint

## Explain it back

1. What was your sprint goal and did you meet it? If not, when did you know, and who did you tell?
2. Show me your smallest PR and your largest. Why was the large one large?
3. What did you find in someone else's PR that they had missed?
4. Where did your estimate go wrong, and what did you do about it?
5. What broke in the demo, and how did you handle it?
6. What is the one change from your retrospective?

## Stretch

- Add a feature flag system and demo shipping an unfinished feature safely
- Pair program a hard feature with another student for a full day
- Add a changelog and release notes for your demo

## Resources

- Read about trunk based development
- Read one short guide on writing good pull request descriptions
- Practise your demo twice before you give it. Out loud, timed
