---
week: 24
phase: Phase 6 of 6, Ship and Get Hired
title: Prove It, Then Go and Get the Job
standfirst: The final week. You will be assessed the way employers assess: system design on a whiteboard, live coding with AI turned off, defending your architecture under questioning, and explaining code you did not write. Then you launch.
backend: System design, defence
frontend: Portfolio and demo
license: Off for assessment, Green for portfolio
hours: 26 hrs
track: Final assessment and launch
---

## Read this first

Six months ago you could not write a loop. This week you will be asked to design a system for a million users on a whiteboard, and you will be able to hold that conversation.

Two things to understand about the assessments. First, AI is off for the technical ones, because that is how interviews work and because what remains when the tools are removed is the honest measure of what you learned. Second, none of this is a trick. Everything assessed is something you have done in the last twenty-three weeks.

## What you are learning

### System design

- The structured approach: requirements, scale estimates, API design, data model, high level design, bottlenecks, tradeoffs
- Asking clarifying questions before drawing anything, and what happens to candidates who do not
- Back of envelope estimation: users, requests per second, storage, bandwidth
- The standard building blocks: load balancer, cache, queue, database, replica, CDN, object storage
- SQL versus NoSQL, chosen for a reason you can state
- Where the system breaks first, and what you would do about it
- Stating tradeoffs out loud. Senior engineers are recognised by the tradeoffs they name, not the answers they give

### Interview performance

- Thinking out loud so an interviewer can follow you
- Handling a problem you cannot immediately solve without freezing
- Being wrong gracefully and correcting fast
- Talking about your capstone in thirty seconds, two minutes and ten minutes, depending on who is asking
- Answering "tell me about a bug you fixed" with a specific story that has a root cause in it
- Answering how you use AI in a way that reads as senior rather than dependent
- Asking questions that show you evaluate employers too

### Portfolio

- A README that sells the work in the first paragraph
- A demo video, three minutes, no dead time
- A CV that describes outcomes rather than a list of technologies
- A LinkedIn and GitHub profile that agrees with your CV
- One written technical post about something you learned deeply this programme

## How to run your week

| Days | Focus |
|---|---|
| 1 | System design study, then three practice designs on a whiteboard, timed. |
| 2 | **Assessment 1: system design.** 45 minutes, whiteboard, no AI. |
| 3 | **Assessment 2: live coding.** 90 minutes, no AI, no internet beyond official docs. |
| 4 | **Assessment 3: capstone defence.** Architecture questioned hard for 45 minutes. |
| 5 | Portfolio: README, demo video, CV, profiles. |
| 6 | Mock interviews, technical and behavioural, with feedback. |
| 7 | Launch your capstone publicly. Graduation demo. |

> **How to talk about AI in an interview.** Wrong answer: "I use AI for everything, it makes me fast." Also wrong: "I do not use it, I write everything myself." The answer that gets you hired: "I specify carefully, delegate implementation, and review hard. Here is a bug I caught in generated code last month, and here is why the tests I wrote caught it." That answer says you are the engineer and the tool is a tool.

## The three assessments

### Assessment 1: system design, 45 minutes, no AI

You will be given a system to design. Something like a ride hailing service, a ticketing system for a stadium sale, a URL shortener at scale, or a notification platform.

Assessed on:

- Do you clarify requirements before designing
- Do you estimate scale rather than guess
- Is your data model sound
- Do you identify the real bottleneck
- Do you state tradeoffs out loud
- Do you handle "now it is 100x bigger" without starting over

### Assessment 2: live coding, 90 minutes, no AI

A problem in C# and a problem in React, on a machine with the official documentation available and nothing else. Not algorithm puzzles. Realistic tasks: parse and transform data with correct edge case handling, build a component with state and validation, fix a bug in a provided file, write a test for a described behaviour.

Assessed on: correctness, edge case handling, readability, use of the debugger, and whether you talk while you work.

### Assessment 3: capstone defence, 45 minutes, no AI

Your architecture questioned by someone trying to find the weakness. Expect:

- Why this database, why this structure, why this pattern
- Walk me through a request end to end, naming every layer it touches
- Show me the code you are least happy with and tell me why
- What breaks at 100x the traffic
- Which parts were AI generated, and what did you change about them
- What would you do differently starting again
- Take a random file, and explain what it does and why it exists

Saying "I do not know, but here is how I would find out" is an acceptable answer. Bluffing is not, and is obvious.

## The final deliverables

- [ ] Capstone deployed, public, and working on a phone
- [ ] README that explains the problem, the solution, the architecture and the tradeoffs, with screenshots
- [ ] Demo video, three minutes, showing the product rather than the code
- [ ] `docs/` complete: architecture, decisions, runbook, security notes, performance report, evaluation results
- [ ] Test suite green, CI green, monitoring live
- [ ] CV rewritten around outcomes, one page
- [ ] GitHub profile tidy: pinned repositories, real READMEs, no abandoned test folders
- [ ] One written technical post published
- [ ] All 24 weeks of work in a single organised repository
- [ ] Assessment 1 passed
- [ ] Assessment 2 passed
- [ ] Assessment 3 passed

## The questions you should now be able to answer

Ask yourself these. If any answer is weak, that is your next month of study, and knowing it is a strength rather than a failure.

1. Design me a system for ten million users. Where does it break first?
2. Walk me through a request from browser to database and back, naming every layer.
3. What is the hardest bug you fixed and what was the actual root cause?
4. How do you know your code works?
5. How do you use AI, and where do you not trust it?
6. What is in your app that you know is wrong, and why did you accept it?
7. What do you want to be good at in two years?

## After this week

You are an intermediate full stack engineer. That is a real thing and you earned it. Three habits keep it:

**Keep shipping.** The gap between competent and senior is closed by building things with real users and living with the consequences.

**Keep reading code you did not write.** Contribute to open source, read your dependencies' source, review other people's work. Reading is how you get fast.

**Stay the engineer.** The tools will keep getting better at writing code. They will not get better at deciding what should be built, judging whether the answer is right, or taking responsibility when it is wrong. That is the job. Protect your ability to do it without help, and you will be employable through every wave of tooling that comes.

Now go and get hired.
