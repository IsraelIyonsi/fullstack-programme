---
week: 08
phase: Phase 2 of 6, Persistence and APIs
title: Clean Architecture, Patterns and Your First Tests
standfirst: You will restructure the school into clean architecture, learn the repository and unit of work patterns for real reasons rather than as vocabulary, and write your first automated tests. This is the week your code starts looking professional.
backend: Clean architecture, CQRS-lite, xUnit
frontend: Component architecture, Vitest
license: Yellow
hours: 30 hrs
track: School Management, part 5
---

## Read this first

Patterns are answers to questions. If you learn the answer without the question you get a developer who puts a repository over a repository and an interface on everything with one implementation. So for each pattern this week, write down the specific pain it removes from your code. If you cannot name the pain, do not use the pattern.

Testing starts this week and never stops. From now on, no build is accepted without tests.

## What you are learning

### Backend: structure and patterns

- Clean architecture in practice, and how it maps onto the four projects you already have
- The repository pattern: what it gives you beyond `DbContext`, and the argument that EF is already a repository
- Unit of work: making several repository operations commit or fail together
- Service layer and use cases. One class per operation as an alternative shape
- CQRS as a concept: separating the read model from the write model, without adopting a framework
- MediatR: what a request handler pipeline buys you and what it costs in readability
- The specification pattern for reusable query rules
- Mapping: hand-written mappers versus AutoMapper or Mapster, and the debugging cost of magic
- SOLID, applied to code you already wrote. Find your own violations
- Guard clauses and domain invariants: making illegal states unrepresentable

### Testing

- The test pyramid: many unit tests, some integration tests, few end to end
- xUnit: facts, theories, `InlineData`, fixtures, setup and teardown
- Arrange, act, assert. One behaviour per test
- Naming tests so a failure report reads like a sentence
- FluentAssertions for readable expectations
- Test doubles: fakes, stubs, mocks, and Moq or NSubstitute
- What is worth testing: business rules, edge cases, failure paths. Not getters
- Vitest and React Testing Library: testing behaviour, not implementation
- Testing a component that fetches, with a mocked API layer

## How to run your week

| Days | Focus |
|---|---|
| 1 | Restructure to clean architecture properly. Move code until dependencies point inward. |
| 2 | Unit of work and transactions. Make a multi-step enrolment atomic. |
| 3 | xUnit setup. Write twenty unit tests for your domain rules. |
| 4 | Mocking. Test the service layer with fake repositories. |
| 5 | Frontend component architecture: split, extract, remove duplication. |
| 6 | Vitest and React Testing Library. Test a form and a list. |
| 7 | Coverage check, README, submit. |

> **Write one test that fails first.** Break a business rule on purpose, watch the test go red, then fix it and watch it go green. A test you have never seen fail is a test you cannot trust.

## Your AI licence this week: Yellow, and this is the sweet spot

Test writing is where AI is genuinely excellent and where a junior gains the most, on one condition: **you decide what to test, AI helps write it.** If AI decides what to test, you get twelve tests that assert a constructor sets a property and zero that catch a real bug.

Workflow to follow every time:

1. You write the list of behaviours worth testing, in plain English, in the test file as comments.
2. AI turns your list into test skeletons.
3. You fill in the meaningful assertions.
4. You add at least three tests AI did not think of, covering edge cases you found.

Also useful: "Here is my service class. What edge cases am I not handling?" That question is worth asking every week for the rest of the programme.

## The build: School Management System, part 5

### Backend requirements

1. Clean architecture enforced. Add an architecture test (using NetArchTest or a simple reflection test) that fails the build if `Domain` references `Infrastructure`.
2. Unit of work implemented so enrolling a student, updating course capacity and writing an audit record either all succeed or all roll back.
3. Domain invariants moved into the entities themselves. A `Course` cannot be constructed with a negative capacity. An `Enrolment` cannot exist without both ids.
4. At least one specification or query object reused across two endpoints.
5. Explicit mapping between entities and DTOs, in one place, tested.
6. A written `docs/decisions.md` recording three architecture decisions: what you chose, what you rejected, and why. One of them must be a pattern you decided **not** to use.

### Testing requirements

Backend:

1. At least 30 unit tests covering domain rules and service logic.
2. Tests for the failure paths: full course, duplicate enrolment, deleting a department head, invalid grade.
3. Repository interfaces mocked. No test touches the database this week.
4. Theories with `InlineData` used for boundary values, for example capacity 29, 30, 31.
5. All tests pass with `dotnet test` and run in under 10 seconds.

Frontend:

1. Vitest and React Testing Library configured.
2. At least 12 component tests including the person form: required validation, successful submit calls the API layer, failed submit shows an error.
3. Tests query by role and label, not by class name or test id where a real accessible query exists.
4. The API layer is mocked. No test hits a live server.

### Acceptance criteria

- [ ] Architecture test fails when you deliberately add a bad reference, then passes when removed
- [ ] Enrolment rollback proven by a test that forces a mid-operation failure
- [ ] `new Course(capacity: -5)` throws, and a test asserts it
- [ ] `dotnet test` shows 30 or more passing tests
- [ ] Every test name describes a behaviour, for example `EnrolStudent_WhenCourseIsFull_ThrowsCourseFullException`
- [ ] `npm test` shows 12 or more passing tests
- [ ] Deleting a business rule from the code makes a specific test fail, and you can demonstrate which
- [ ] `docs/decisions.md` includes one pattern you rejected with reasoning
- [ ] `ai-log.md` shows which tests you wrote versus generated

## Explain it back

1. What pain does the repository pattern remove from your code? Be specific to your project.
2. Where would you say "no" to adding another layer, and why?
3. Which SOLID principle were you violating before this week? Show me the commit that fixed it.
4. What is unit of work protecting you from? Give me the failure it prevents.
5. Which of your tests would still pass if the feature were broken? Delete it.
6. Why test through the accessible role rather than a CSS class?

## Stretch

- Introduce MediatR for one feature only, then write up whether it was worth it
- Add mutation testing with Stryker and see how many of your tests actually catch changes
- Set a coverage threshold and make the build fail below it

## Resources

- Read a clean architecture summary, then Uncle Bob's original article. Argue with both
- xUnit docs, FluentAssertions docs
- Testing Library guiding principles. Read them before you write a single test
