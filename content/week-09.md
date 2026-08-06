---
week: 09
phase: Phase 3 of 6, Production Concerns
title: Integration Testing and End to End Confidence
standfirst: Unit tests prove your logic. They do not prove your app works. This week you test against a real database in a container, test your API through actual HTTP, and drive your Next.js app in a real browser with Playwright.
backend: Integration tests, Testcontainers
frontend: Playwright end to end
license: Yellow
hours: 28 hrs
track: School Management, part 6
---

## Read this first

Every developer has shipped a change with a green test suite and broken production. The gap is almost always at a boundary: the database, the HTTP layer, the browser. This week you close that gap.

There is a second reason this week matters more now than it did five years ago. When AI writes a large share of your code, your test suite is the thing that tells you the code is right. A weak suite plus fast generation is how teams ship bugs at speed.

## What you are learning

### Backend integration testing

- The difference between a unit test, an integration test and an end to end test, and what each is allowed to touch
- `WebApplicationFactory<T>`: spinning your entire API up in memory and calling it over HTTP
- Overriding services in the test host, for example swapping the real clock or an email sender
- Testcontainers: starting a real SQL Server in Docker for the test run, then throwing it away
- Database per test versus transaction rollback per test, and the tradeoff
- Seeding known data for a test, and why shared mutable test data causes flaky suites
- Asserting on status codes, headers and response bodies
- Testing the failure paths through the full stack: bad payload, missing resource, conflict
- Test isolation, ordering, and why a test that only passes when run second is broken

### Frontend end to end testing

- Playwright setup, projects, browsers, the test runner
- Locators: role, label, text. Why brittle CSS selectors are the reason people give up on end to end tests
- Auto-waiting, and why you should almost never write a fixed sleep
- Testing a full user journey: land, search, open a record, edit it, see the change
- Network interception for the cases you cannot easily produce
- Traces, screenshots and video on failure, and reading them
- Running the API, the database and the frontend together for a test run

### Cross-cutting

- What is worth an end to end test: the money paths only. Everything else is cheaper lower down
- Flakiness: causes, detection, and the rule that a flaky test is deleted or fixed within a week

## How to run your week

| Days | Focus |
|---|---|
| 1 | Integration test setup with `WebApplicationFactory`. First test hits `GET /api/students` and asserts 200. |
| 2 | Testcontainers with real SQL Server. Migrations run on start, data seeded per test. |
| 3 | Write the API integration suite: happy paths and failure paths for every controller. |
| 4 | Playwright setup, first journey test. |
| 5 | Three full user journeys, running against your real API. |
| 6 | Deliberately break three things and confirm the suite catches all three. |
| 7 | Document how to run the whole suite from a clean clone, submit. |

> **The clean clone test.** Delete your local repo copy, clone it fresh, and run one documented command. If the tests do not run, your setup is not finished. Do this for real, not in your head.

## Your AI licence this week: Yellow

Strong week for AI, with the same rule as week 8: you choose the cases, AI writes the plumbing.

- "Set up Testcontainers with SQL Server for xUnit. Explain the fixture lifetime you chose."
- "Here are my controllers. List every failure path that should have an integration test."
- "Convert this manual test script into a Playwright test using role-based locators."
- "This Playwright test is flaky. Here is the trace. What is the race condition?"

Ask this once, seriously: **"What would still be broken in my app even if every one of these tests passed?"** Write the answer in your README. That question is the difference between having tests and having confidence.

## The build: a suite you would trust before a Friday deploy

### Integration test requirements

1. A test project using `WebApplicationFactory` that starts the real API.
2. Testcontainers starting a real SQL Server instance for the suite. No mocking the database.
3. Migrations applied automatically at test start. Known seed data per test class.
4. Tests are isolated. Running the suite twice in a row gives identical results. Running a single test in isolation passes.
5. At least 25 integration tests covering:
   - Every list endpoint returns 200 with correct paging metadata
   - Get by id returns 200 for existing, 404 for missing
   - Create returns 201 and the resource can then be fetched
   - Create with invalid body returns 400 with field detail
   - Update, then read back, reflects the change
   - Delete returns 204 and a subsequent get returns 404
   - Enrolling into a full course returns 409 and does not partially write
   - Enrolling a student twice on the same course is rejected
6. One test proves a rollback: force a failure mid transaction and assert the database is unchanged.

### End to end requirements

1. Playwright configured against your local stack.
2. Three journeys, minimum:
   - **Directory journey:** open the app, search for a student, open their detail page, confirm their courses are listed
   - **Admin journey:** create a new teacher through the form, see them appear in the list, edit their subject, delete them, confirm they are gone
   - **Enrolment journey:** open a course, enrol a student, see the enrolment count rise, attempt to enrol into a full course and see the error message
3. Zero fixed sleeps. All waits are on conditions.
4. Locators use role, label or text. No `.css-1x2y3z` selectors.
5. Traces and screenshots captured on failure.
6. One documented command runs everything.

### Acceptance criteria

- [ ] `docker compose` plus one test command runs the full suite from a clean clone
- [ ] 25 or more integration tests, all green
- [ ] Deleting your enrolment capacity check makes a specific named test fail
- [ ] Changing a status code from 204 to 200 makes a specific test fail
- [ ] Renaming a form label makes a Playwright test fail with a clear message
- [ ] The suite passes three consecutive runs with no flakes
- [ ] Total suite run time documented in the README
- [ ] README answers: what would still be broken if all of these passed
- [ ] `ai-log.md` updated

## Explain it back

1. Which of your tests are unit, which integration, which end to end, and why is each at that level?
2. Why Testcontainers rather than an in-memory database provider? What does the in-memory one lie about?
3. Show me a test that fails when the app is broken but passes when it is merely refactored.
4. What causes a flaky test, and what is your policy when you find one?
5. Why is `page.waitForTimeout(2000)` a bug?
6. Where is the gap in your suite that you know about and chose to accept?

## Stretch

- Add contract testing between the frontend API client and the OpenAPI spec
- Add a smoke suite that runs in under 30 seconds for pre-commit
- Add accessibility assertions to your Playwright tests with axe

## Resources

- Microsoft Learn: integration tests in ASP.NET Core
- Testcontainers for .NET docs
- Playwright docs: Writing tests, Locators, Trace viewer
