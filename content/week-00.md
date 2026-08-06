---
week: 00
phase: Phase 1 of 6, Start Here
title: Start Here, How This Programme Works
standfirst: Read this before week one. It explains the six month arc, the one rule that decides whether you finish, how your work is assessed, and the AI licence system that governs how you are allowed to use these tools at each stage.
backend: .NET and C#
frontend: React and Next.js
license: Red to Green
hours: 25 to 32 hrs per week
track: Programme handbook
---

## What you are signing up for

Twenty-four weeks. At the end you are an intermediate full stack engineer: C#, .NET, SQL Server, React, Next.js and TypeScript, with a deployed, monitored, tested product you built and can defend.

It costs 25 to 32 focused hours a week. Focused means the phone is elsewhere. Six distracted hours are worth less than two real ones, and the difference compounds over six months.

## The shape of it

| Weeks | Phase | What happens |
|---|---|---|
| 1 to 4 | Fundamentals | C# from zero, HTML, CSS, JavaScript, then your first React. Calculator, then the school project starts |
| 5 to 8 | Persistence and APIs | Layered architecture, SQL and EF Core, ASP.NET Core Web APIs, clean architecture, first tests |
| 9 to 12 | Production concerns | Integration and end to end testing, auth, real API concerns, Docker, CI/CD, first deploy |
| 13 to 18 | Depth | Your capstone begins. Frontend craft, real time, uploads, payments, performance, distributed systems, security |
| 19 to 22 | AI engineering and build | Building with LLMs, retrieval and evaluation, then two weeks of team-style sprinting |
| 23 to 24 | Ship and get hired | Monitoring, backups, chaos day, then system design, live coding and capstone defence |

Two projects carry the whole programme. The **school management system** runs from week 3 to week 12 and teaches you every core skill. Your **capstone**, proposed in week 12 and built from week 13, is the thing you show employers.

## The one rule

**Nothing counts as done until you can explain it out loud with the editor closed.**

Every week ends with an explain-it-back session. You walk through what you built, and you answer questions about why. Code that works but that you cannot explain scores zero, every time, no exceptions.

This rule exists because of what these tools changed. It is now easy to produce working code you do not understand, and people who do that get through a bootcamp and fail in the first interview. The rule protects you from that outcome.

## The AI licence

You will use AI throughout, but how much you are allowed to delegate changes as you grow. Three tiers.

### Red, weeks 1 to 4

AI is a tutor and never a typist. Turn off tab completion.

- **Yes:** explanations, quizzes, reviewing code you already wrote, practice exercises, decoding error messages
- **No:** any generated code you paste into your project
- **The check:** can you retype the file from an empty editor

### Yellow, weeks 5 to 12

AI writes boilerplate. You write the thinking.

- **Yes:** scaffolding, config, test skeletons, mapping code, "give me three approaches and the tradeoffs"
- **No:** accepting a single line you cannot explain
- **The check:** in review, a random line is picked and you explain why it is there. One "I do not know" and the work is returned

### Green, weeks 13 to 24

AI implements. You are the reviewer, and this is the actual job.

- **Yes:** delegating implementation from a written spec
- **Required:** a written spec before generation, a line by line review after, and full ownership of the result
- **The check:** "the AI wrote it" is never an explanation, in this programme or in a job

**Every week you submit `ai-log.md`:** what you delegated, what came back, what you changed and why. It is assessed.

**The three-strike rule:** if AI fails three times in a row on the same problem, stop prompting and read the documentation. Repeat prompting on a misunderstood problem is the most expensive way to lose an afternoon.

## How you are assessed

Five mechanisms, all designed so that generated code cannot carry you.

1. **The weekly build.** Backend and frontend, against explicit acceptance criteria in each week's PDF.
2. **Explain it back.** Live, out loud, editor closed.
3. **The blank editor drill.** Thirty minutes, no AI, no internet. Rebuild something small from that week.
4. **Code review.** You review other students. You are assessed on what you find, not only on what you build.
5. **Final assessments, week 24.** System design, live coding and capstone defence, all with AI switched off.

## How to submit

Everything goes to GitHub. One repository per week's work in weeks 1 to 12, then one capstone repository from week 13.

Each submission needs:

- Working code on a branch merged through a pull request
- A README: what it is, how to run it, what you found hard
- `ai-log.md` for that week
- Tests, from week 8 onward
- The acceptance criteria checklist from the week's PDF, ticked honestly

Submit by Sunday night. Late is fine occasionally if you say so in advance. Silent and missing is not.

## What we need from you

**Ask for help after twenty minutes, not after two days.** Being stuck is normal. Staying stuck silently is the single biggest predictor of not finishing this programme.

**Be honest in your logs and checklists.** Nobody is harmed by "I did not finish this and here is where I got to." A ticked box that is not true wastes everyone's time, starting with yours.

**Do the reading.** Every week lists resources. The people who read the official documentation pull ahead of the people who only watch videos, every single cohort.

**Show up to reviews.** Reviewing other people's code is where a surprising amount of the learning happens.

## What you should expect to feel

Weeks 3 and 4 are the first wall, when object orientation and generics stop feeling like syntax and start feeling like design. Weeks 7 and 8 are the second, when the number of moving parts jumps. Week 13 is the third, when the safety of a specified project is removed and you are building your own thing.

Every cohort hits these. Hitting them is not a signal that you are behind. Going quiet when you hit them is the only real risk.

## Start

Read Week 01 now. Install the tools tonight so day one is spent learning rather than fighting your machine.

Six months from now you will be able to design a system on a whiteboard, ship it, monitor it, and defend every decision in it. That is not a small thing. Begin.
