---
week: 12
phase: Phase 3 of 6, Production Concerns
title: Git, Docker, CI/CD and Your First Deploy
standfirst: Halfway. This week your app leaves your laptop. Proper git workflow, code review, Docker for the whole stack, GitHub Actions running your tests on every push, and a live URL you can send to anyone. You also choose your capstone.
backend: Docker, GitHub Actions, deployment
frontend: Vercel or container deploy
license: Yellow
hours: 30 hrs
track: Ship it, plus capstone kickoff
---

## Read this first

There is a category of engineer who writes good code and cannot get it in front of a user. They are not employable at the level you are aiming for. This week fixes that permanently.

By Sunday you will have a URL. Send it to your family. Watch it break on someone's Android phone. That is the education.

## What you are learning

### Git and collaboration

- Branching: feature branches, naming, keeping them short lived
- Rebase versus merge, and what a clean history buys the person reading it in a year
- Writing a commit message: subject line under 50 characters, body explaining why not what
- Pull requests: description, screenshots, how to test, and a small diff
- Reviewing someone else's PR: what to comment on, what to let go, how to disagree without friction
- Resolving conflicts without panic
- `git bisect` to find the commit that broke something
- Tags and semantic versioning

### Containers

- What a container actually is, and how it differs from a virtual machine
- Dockerfile: base images, layers, caching, and why layer order changes build time
- Multi-stage builds so your production image does not ship the SDK
- .dockerignore, image size, and running as a non-root user
- `docker compose` for your whole stack: API, SQL Server, frontend, and later Redis
- Environment variables and configuration into containers
- Volumes and why your database data disappears without one
- Debugging inside a running container

### CI/CD

- GitHub Actions: workflows, jobs, steps, triggers, matrix builds
- A pipeline that on every push restores, builds, runs unit tests, runs integration tests, and lints
- Branch protection so nothing merges to main with a red build
- Building and pushing a container image
- Deploying: Azure App Service, Azure Container Apps, Render or Fly for the API, Vercel for the frontend
- Environment separation and configuration per environment
- What a rollback looks like and practising one before you need it

## How to run your week

| Days | Focus |
|---|---|
| 1 | Git workflow. Branches, PRs, review a classmate's PR properly. |
| 2 | Dockerfile for the API, multi-stage, small image. Dockerfile for the frontend. |
| 3 | `docker compose up` brings the whole stack up on a clean machine. |
| 4 | GitHub Actions: build, test, lint on every push. Branch protection on. |
| 5 | Deploy the API and database. Deploy the frontend. Wire them together. |
| 6 | Fix everything that only broke in production. There will be plenty. |
| 7 | Capstone proposal written and approved. Submit. |

> **Production always breaks differently.** CORS origins, environment variables, connection strings, HTTPS, cold starts, time zones and case-sensitive file systems. Keep a list of every production-only failure you hit this week. That list is worth more than the deploy itself.

## Your AI licence this week: Yellow, leaning Green

Infrastructure config is where AI saves the most time and where you should still read every line, because a wrong Dockerfile wastes an hour and a wrong CI secret leaks a key.

- "Write a multi-stage Dockerfile for a .NET 8 API. Explain each stage and why the layer order is that way."
- "My image is 1.2GB. What is in it that should not be?"
- "Here is my GitHub Actions workflow. What runs that does not need to, and what is missing?"
- "My app works locally and 500s in production. Here are the logs. What are the five most likely causes, ranked?"

That last prompt shape, ranked hypotheses rather than a single answer, is the most useful debugging prompt you will learn. Use it for the rest of your career.

## The build: ship the school

### Requirements

1. Git history that a stranger can follow. Feature branches, meaningful messages, at least six merged pull requests with descriptions.
2. You review two other students' pull requests with substantive comments. Being reviewed is part of the assessment, so is reviewing.
3. A multi-stage Dockerfile for the API producing an image under 250MB, running as non-root.
4. A Dockerfile for the Next.js app.
5. `docker-compose.yml` bringing up API, SQL Server and frontend together with one command, with a volume so data survives a restart.
6. A GitHub Actions workflow that on every push to any branch: restores, builds, runs unit tests, runs integration tests with Testcontainers, and runs linting on the frontend. Red build blocks merge.
7. Deployed API with a real database, reachable over HTTPS.
8. Deployed frontend pointing at the deployed API, with environment configuration done properly.
9. A `docs/runbook.md` with: how to deploy, how to roll back, where the logs are, what to check when it is down.
10. Practise a rollback for real and record how long it took.

### Capstone proposal, due Sunday

One page, submitted for approval. It must contain:

- The problem and who has it. A real problem, ideally one you have personally
- The core user journey in five steps or fewer
- The data model sketch: main entities and relationships
- The three features that make it worth building, and five you are deliberately not building
- What is technically interesting or hard about it
- Where an AI feature would genuinely help, and where it would be decoration

Rules: not a clone of a well-documented tutorial project. Not another school system. Something you would still want to work on in week 22, because you will be.

### Acceptance criteria

- [ ] `git clone` then `docker compose up` gives a working app on a clean machine
- [ ] API image is under 250MB and runs as a non-root user
- [ ] Pushing a commit that breaks a test produces a red build and blocks merge
- [ ] The deployed frontend talks to the deployed API over HTTPS with no CORS errors
- [ ] Restarting the database container does not lose data
- [ ] A stranger can visit your URL and use the app on a phone
- [ ] Rollback practised, with the elapsed time recorded in the runbook
- [ ] Six or more merged PRs, and two substantive reviews given to others
- [ ] `docs/production-surprises.md` lists every production-only failure you hit
- [ ] Capstone proposal submitted and approved

## Explain it back

1. What is in your final container image and what did you deliberately leave out?
2. Why multi-stage? What was the image size before and after?
3. Your CI is green but production is down. Walk me through your first five minutes.
4. How do you roll back, and how long does it take?
5. Something worked locally and failed deployed. Pick one, explain the root cause.
6. Why is your capstone worth ten weeks of your life?

## Stretch

- Add a staging environment that deploys automatically from a branch
- Add database migrations to the deploy pipeline safely, with a plan for a failed migration
- Add uptime monitoring with an alert to your phone

## Resources

- Pro Git, chapters 3 and 6
- Docker docs: multi-stage builds, compose
- GitHub Actions docs: workflow syntax, caching, secrets
