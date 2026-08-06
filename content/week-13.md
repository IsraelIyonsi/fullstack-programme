---
week: 13
phase: Phase 4 of 6, Depth
title: Frontend Craft and the Green Licence
standfirst: The second half starts. Your AI licence changes today: you become the reviewer, not the typist. On the frontend you move from making things work to making things good, with real component architecture, a design system and performance you can measure.
backend: Redis caching, background reads
frontend: Design systems, advanced React
license: Green
hours: 28 hrs
track: Capstone, sprint 1
---

## Read this first

From this week you are working on your capstone, not the school. The school taught you the moves. The capstone proves you can do them unaccompanied.

Your AI licence goes Green today. That does not mean less rigour. It means the rigour moves from writing to reviewing, which is harder and is the actual job you are being hired for.

## Your AI licence: Green, and what it demands

Green means you may delegate implementation. In exchange you take on three obligations.

**1. Specify before you generate.** No more one-line prompts. Every non-trivial delegation starts with a written spec: what it must do, the inputs and outputs, the edge cases, the constraints, what it must not touch. If you cannot write the spec, you do not understand the task well enough to review the answer.

**2. Review like it came from a stranger.** Read every line. Ask of each: is this correct, is it necessary, does it match our patterns, what happens when the input is empty or huge or hostile. Generated code that "works" is where security and performance bugs live.

**3. Own it completely.** "The AI wrote it" is not an explanation in a code review, a post-mortem or an interview. Once you merge it, it is yours.

> **The three-strike rule.** If AI fails to solve something three times in a row, stop prompting and go read the documentation or the source. Repeated prompting on a misunderstood problem is the most expensive way to waste an afternoon that exists.

## What you are learning

### Frontend architecture

- Component design: presentational versus container, and composition over configuration
- Prop APIs that are hard to misuse. Boolean explosion and how to avoid it
- Compound components and the `children` pattern
- Custom hooks: extracting logic, naming, dependency correctness, testing them
- Design tokens: colour, spacing, typography, radius, shadow, defined once
- Building on shadcn/ui with Tailwind, and when to write your own component instead
- Dark mode without duplicated styles
- Responsive design that starts at mobile, and the layouts that break on tablet
- Loading, empty, error and success states designed for every data surface. Four states, always
- Accessibility as structure, not as a bolt-on: semantics, focus order, live regions

### Performance you can measure

- React rendering: what causes a re-render, `memo`, `useMemo`, `useCallback`, and when they are pure cost
- The React DevTools profiler. Measure first, optimise second
- List virtualisation for long tables
- Next.js: images, fonts, route level code splitting, streaming and Suspense boundaries
- Core Web Vitals: LCP, CLS, INP. What each one means and what moves it
- Lighthouse, and why a 100 score on your laptop means little

### Backend this week

- Redis caching for your capstone's read-heavy paths
- Cache invalidation strategy written down before it is implemented
- Graceful degradation when the cache is unavailable

## How to run your week

| Days | Focus |
|---|---|
| 1 | Capstone: set up the repo, solution structure, CI and deployment skeleton on day one. Deploy an empty app. |
| 2 | Design tokens, base components, layout shell, dark mode. |
| 3 | Build your first real feature end to end, backend and frontend, with all four states. |
| 4 | Custom hooks and refactoring. Remove the duplication you just created. |
| 5 | Redis caching on your heaviest read path, with measurements. |
| 6 | Performance pass: profile, then fix, then measure again. |
| 7 | Accessibility pass, demo, submit. |

## The build: capstone sprint 1

### Requirements

1. Repository set up on day one with clean architecture, CI running tests, and an automatic deploy. Deploy a blank shell before writing any feature. Never leave deployment to the end.
2. Design tokens defined once and used everywhere. No hardcoded hex values in components.
3. A component library of at least eight reusable pieces: Button, Input, Select, Card, Table, Dialog, Toast, EmptyState. Each documented with its props.
4. Dark mode working across every screen.
5. Your first real feature complete on both ends, with all four UI states implemented and screenshotted in the README.
6. At least three custom hooks extracted from real duplication, not invented for the assignment.
7. Redis caching on one path, with the invalidation strategy written in `docs/caching.md` before implementation.
8. A performance baseline recorded: Lighthouse scores, bundle size, and the profiler flame graph for your heaviest screen. Then a documented improvement.
9. `specs/` folder containing the written spec for every feature you delegated to AI, alongside your review notes on what you changed.

### Acceptance criteria

- [ ] Deployed and reachable by end of day one, before any feature exists
- [ ] Zero hardcoded colours in components, verified by search
- [ ] Every data surface has loading, empty, error and success states, all screenshotted
- [ ] Dark mode has no unreadable text anywhere, checked on every screen
- [ ] Three custom hooks with tests
- [ ] Cache invalidation documented before the code, timestamps prove it
- [ ] Stopping Redis degrades to direct database reads without an error page
- [ ] Before and after numbers for one real performance fix, with the profiler evidence
- [ ] `specs/` contains a spec for every AI-delegated piece
- [ ] Keyboard navigation works on your main journey

## Explain it back

1. Show me a spec you wrote and the code that came back. What did you change and why?
2. Which memoisation did you add, and what did the profiler say before and after?
3. Where did you decide `useMemo` was not worth it?
4. What is your cache invalidation strategy and where will it be wrong?
5. Pick a component and explain why its props are hard to misuse.
6. What did AI get wrong this week that you caught?

## Stretch

- Add Storybook for your component library
- Add visual regression tests
- Add a skeleton-to-content transition that does not shift layout

## Resources

- React docs: reusing logic with custom hooks, and the performance section
- web.dev: Core Web Vitals, and Optimize LCP
- Refactoring UI, skimmed for the spacing and hierarchy chapters
