---
week: 22
phase: Phase 5 of 6, AI Engineering
title: Feature Complete, and Making It Hold
standfirst: The second half of the sprint. All features land, then you stop adding and start hardening: the edge cases, the errors, the empty states, the small ugly details that decide whether someone believes a real engineer built this.
backend: Hardening and edge cases
frontend: Polish and resilience
license: Green
hours: 32 hrs
track: Capstone, sprint 6 close
---

## Read this first

Wednesday is your feature freeze. After it, no new features, no exceptions, however good the idea. Write it in a `future.md` file and let it go.

The last twenty percent of quality lives in the parts nobody demos: what happens when the list is empty, when the name is 400 characters, when the network dies mid-save, when the same button is clicked twice, when the user opens the app in two tabs. Employers look at exactly these things because they reveal whether you have shipped anything real.

## What you are learning

- Feature freeze as a discipline, and the difference between finishing and stopping
- Edge case hunting as a systematic activity rather than luck
- Error handling that helps: what happened, what to do next, how to get help
- Data validation at every boundary, including the ones you control
- Idempotency in the UI: the double click, the double submit, the back button, the refresh mid-flow
- Concurrency: two people editing the same record, and optimistic concurrency with a version column
- Time zones, currency, locales and long names. The four things every app gets wrong
- Accessibility as a completion requirement, not a bonus
- Cross-browser and cross-device reality, including a cheap Android phone
- Writing documentation someone else could onboard from

## How to run your week

| Days | Focus |
|---|---|
| 1 to 2 | Land the remaining features. Merge everything. Feature freeze Wednesday morning. |
| 3 | Edge case hunt. Attack your own app as a hostile, careless and confused user. Log everything. |
| 4 | Fix the findings, hardest first. Regression tests for each. |
| 5 | Errors, empty states, loading states, offline behaviour, concurrency. |
| 6 | Accessibility, responsive, cross browser, real device testing. |
| 7 | Documentation, README, demo rehearsal, sprint close. |

> **Give your app to someone who has never seen it and do not help them.** Sit behind them, say nothing for ten minutes, and write down every place they hesitate, misclick or ask a question. That list is worth more than a week of your own opinions about your UI.

## Your AI licence: Green, aimed at your blind spots

The highest value AI use of the entire programme is available this week, because you are now too close to your own code to see it.

Ask these, seriously, and act on the answers:

- "Here is my feature. List thirty edge cases, ranked by how likely a real user is to hit them."
- "What happens in this flow if the user double clicks, loses connection mid-request, or hits back?"
- "Review these error messages. Which tell the user what to do next and which just say something failed?"
- "Read my README as someone who has never seen this project. What is missing to get it running?"
- "What would a senior engineer criticise in this pull request?"

Then verify each one against your actual code. AI will invent problems you do not have alongside real ones you do. Sorting the two is the skill.

## The build: capstone complete

### Requirements

1. All proposal features complete and deployed. Anything cut is documented with the reason in `docs/scope.md`.
2. Feature freeze respected from Wednesday. Git history proves it.
3. `docs/edge-cases.md` listing at least 40 tested edge cases with the result of each, covering:
   - Empty states everywhere, including first run with no data at all
   - Maximum length input in every field, and what the layout does
   - Special characters, emoji and non-Latin names throughout
   - Double submission of every mutating action
   - Network failure mid-request, and mid-file-upload
   - Browser back and forward through every multi-step flow
   - Two tabs, two users, and the same record edited simultaneously
   - Session expiry mid-action
   - Very large result sets, and pagination boundaries
4. Optimistic concurrency on at least one entity, so a stale edit is refused with a clear message rather than silently overwriting.
5. Every error message states what happened and what to do next. No "An error occurred".
6. Full keyboard operability on your main journeys, and a screen reader pass on the primary flow.
7. Tested on a real phone, not only in DevTools, and in at least three browsers.
8. Documentation complete: README with screenshots, setup that works from a clean clone, architecture overview, and the runbook.
9. Test suite green, coverage on business logic reported, CI and deploy healthy.

### Acceptance criteria

- [ ] No feature commits after Wednesday, proven by git history
- [ ] 40 or more edge cases tested and documented with results
- [ ] Every empty state is designed, none are blank areas
- [ ] Double clicking Submit creates one record, not two
- [ ] Killing the network mid-save produces a recoverable state, not lost data
- [ ] A stale edit is refused with a clear explanation
- [ ] Zero error messages that say only that something went wrong
- [ ] The main journey is completable with keyboard only
- [ ] A stranger can set up the project from your README with no help
- [ ] Tested on a real phone, with screenshots
- [ ] Main branch green, deployed, and reachable

## Explain it back

1. What did you cut, and why was that the right call?
2. Show me the ugliest edge case you found and how you fixed it.
3. What happens when two users edit the same record at the same time?
4. Pick an error message and tell me what the user does next after reading it.
5. What did the person who tested your app get stuck on?
6. What do you know is still weak, and why did you accept it?

## Stretch

- Add offline support with a service worker for the read paths
- Add internationalisation for one additional language
- Add an onboarding tour for first time users

## Resources

- Your own edge case list. It is more useful than any article this week
- WebAIM screen reader basics, enough to test your own flow
- Read three README files from well-run open source projects and copy their structure
