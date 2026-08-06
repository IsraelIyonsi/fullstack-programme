---
week: 04
phase: Phase 1 of 6, Fundamentals
title: Generics, LINQ and React State
standfirst: You will learn to write code that works for any type without duplication, query collections declaratively with LINQ, and manage forms and shared state in React. By Sunday your school has full create, read, update and delete on both ends.
backend: Generics, LINQ, nullable types
frontend: Forms, lifting state, effects
license: Red closing, Yellow opens Sunday
hours: 28 to 32 hrs
track: School Management, part 2
---

## Read this first

Two things separate someone who has learned C# from someone who writes it professionally: they never duplicate a class just to change its type, and they never write a `foreach` with an `if` inside when a LINQ query says it in one line. Both are this week.

On the React side, forms are where beginners stall. Controlled inputs feel like extra work until the first time you need validation, and then they feel like the only sane option.

## What you are learning

### Backend: generics and LINQ

- The problem generics solve. Write `Repository<Student>` and `Repository<Teacher>` from one class
- Generic classes, generic methods, type parameters, `where T : class`, `where T : new()`
- `IEnumerable<T>`, `ICollection<T>`, `IList<T>`: what each one promises
- LINQ method syntax: `Where`, `Select`, `OrderBy`, `ThenBy`, `First`, `FirstOrDefault`, `Single`, `Any`, `All`, `Count`, `Sum`, `Average`, `Max`, `Min`
- `GroupBy` and `Join`. These two are what interviewers ask about
- Deferred execution. Why your query has not run yet, and what `ToList()` actually does
- Anonymous types and projections
- Nullable reference types, the `?` and `!` operators, `??` and `??=`
- Pattern matching: `is`, switch expressions over types, property patterns
- `IComparable` and custom sorting

### Frontend: state that behaves

- Controlled inputs: value plus `onChange`, and why uncontrolled inputs bite later
- Forms with multiple fields held in one state object
- Client side validation and showing field level errors
- Lifting state up: when two components need the same data
- Prop drilling, and recognising when it has gone too far
- `useEffect`: what it is for, the dependency array, cleanup, and the infinite loop you will cause at least once
- Derived state is a mistake. Compute, do not store
- `useRef` for focus and DOM access
- Simple client side routing with React Router: routes, links, URL params

## How to run your week

| Days | Focus |
|---|---|
| 1 | Generics. Build a generic `Repository<T>` with `Add`, `GetById`, `GetAll`, `Update`, `Delete`. |
| 2 | LINQ drills. Twenty queries against your school data, from simple filters to `GroupBy`. |
| 3 | Nullable reference types and pattern matching. Turn nullable warnings on and fix every one. |
| 4 | Backend build: refactor the school onto the generic repository, add a reports menu built on LINQ. |
| 5 | React forms and validation. Add and edit a person. |
| 6 | Lifting state, `useEffect`, routing. Wire up the list, the detail page and the form. |
| 7 | Polish, README, submit. |

> **Turn nullable reference types on this week and never turn them off.** Add `<Nullable>enable</Nullable>` to your csproj. You will get thirty warnings. Fix all thirty. Every one of them is a null reference exception that will not happen in production.

## Your AI licence: Red for four more days, then Yellow

Through Wednesday, stay Red. Generics and LINQ are exactly the kind of thing AI writes instantly and you therefore never learn. Write your first twenty LINQ queries by hand, wrong, repeatedly.

From Thursday you move to **Yellow**, and here is what changes:

- You may ask AI to scaffold boilerplate: a form component skeleton, a repository interface, config files.
- You may ask "give me three ways to write this query and the tradeoffs."
- You still may not accept a line you cannot explain. Every PR review starts with me pointing at a random line and asking why. One "I do not know" and the PR is rejected.

Start a file called `ai-log.md` in your repo. Every time you use AI to produce code, note what you asked for and what you changed about the answer. You will hand this in every week from now on.

## The build: School Management System, part 2

### Backend requirements

1. A generic `Repository<T>` used for students, teachers, courses and departments. One class, four uses. No duplication.
2. A constraint on `T` requiring an `Id`, using an interface like `IEntity`.
3. A reports menu, entirely built with LINQ:
   - Students in a given year group, sorted by surname
   - Teachers grouped by department with a count each
   - The three courses with the most enrolments
   - Average age of students per year group
   - Any course with no assigned teacher
   - Total salary cost per department
4. Nullable reference types enabled, zero warnings at build.
5. Pattern matching used at least twice where it genuinely reads better than an `if` chain.
6. Full update and delete, not just add and list. Deleting a teacher who heads a department is refused with a clear reason.

### Frontend requirements

1. React Router with at least three routes: the directory, a person detail page at `/people/:id`, and an add or edit form.
2. An add person form with fields for name, date of birth, role and role-specific fields that appear based on the role selected.
3. Validation: required fields, a date of birth that is in the past and produces an age between 3 and 80, a salary that is positive. Errors appear under the field, not in an alert box.
4. The form is controlled. There is exactly one state object for the form.
5. Editing an existing person reuses the same form component, prefilled.
6. Delete with a confirmation step.
7. All the data lives in one place in `App` and is passed down. When you add someone, the list updates immediately.
8. A `useEffect` that sets the document title from the current page.

### Acceptance criteria

- [ ] `Repository<T>` is used by four different types with no per-type copy
- [ ] Every report is a LINQ query, not a manual loop with counters
- [ ] `dotnet build` produces zero warnings with nullable enabled
- [ ] Deleting a department head is refused and explains why
- [ ] The React form blocks submission and shows field errors for bad input
- [ ] Selecting the Teacher role reveals the subject and salary fields
- [ ] Adding a person updates the list without a page refresh
- [ ] Navigating to `/people/999` shows a not found state rather than crashing
- [ ] `ai-log.md` exists and records every AI-assisted change from Thursday on
- [ ] At least twelve commits

## Explain it back

1. Why does `Repository<T>` need a constraint? Show me what breaks without it.
2. What is deferred execution, and when has it bitten you?
3. Write me a `GroupBy` on the whiteboard, no IDE.
4. What is the difference between `First` and `FirstOrDefault`, and when does that difference matter at 2am?
5. Why is your form state one object rather than six `useState` calls?
6. You have a `useEffect` that runs forever. Walk me through diagnosing it.

## Stretch

- Add sorting and pagination to the directory
- Add a generic `IRepository<T>` interface and a second in-memory implementation behind it
- Add optimistic UI on delete: remove the row immediately, restore it if the operation fails

## Resources

- Microsoft Learn: generics, LINQ, nullable reference types
- React docs: Managing State, and the Escape Hatches section on effects
- The "You Might Not Need an Effect" page in the React docs. Read it now, not later
