---
week: 03
phase: Phase 1 of 6, Fundamentals
title: Object Oriented Programming and Your First React
standfirst: You stop writing scripts and start designing systems. Classes, encapsulation, inheritance, interfaces and polymorphism on the backend. Components, props and state on the frontend. The school project starts here and runs for the next five weeks.
backend: Classes, interfaces, polymorphism
frontend: React components, props, state
license: Red
hours: 28 to 32 hrs
track: School Management, part 1
---

## Read this first

This is the hardest conceptual week in the first phase. Object orientation is not about syntax, it is about deciding what things exist in your system and who is allowed to change them. Most people learn the syntax in two days and the judgement in two years. This week gets you started on the judgement.

React starts today for the same reason: a React component is a small unit of state and behaviour with a public interface. It is the same idea in a different suit.

## What you are learning

### Backend: object orientation

- Classes and objects. Fields, properties, methods, constructors
- Encapsulation: private fields, public properties, `get` and `set`, and why public fields are a smell
- `this`, object initialisers, and object equality
- Inheritance: base classes, `virtual`, `override`, `base`, `abstract`
- Interfaces: what they are, how they differ from abstract classes, when to use each
- Polymorphism: one call, many behaviours. This is the point of the whole week
- Composition versus inheritance, and why "favour composition" is the standard advice
- `static` members and when a class should have none
- `enum`, `record` and `struct`, and where each fits
- `ToString` overriding, `IEquatable` awareness
- Access modifiers: `public`, `private`, `protected`, `internal`

### Frontend: React fundamentals

- Why React exists: what problem the virtual DOM and declarative rendering actually solve
- Setting up with Vite, the project structure, `npm run dev`
- JSX rules: one root, `className`, expressions in braces, no `if` statements inline
- Components as functions. Props in, UI out
- `useState`: state is a snapshot, not a variable. Why the counter bug happens
- Rendering lists with `map` and why `key` matters
- Conditional rendering with `&&` and ternaries
- Composition: children, layout components, splitting a big component into small ones
- Thinking in React: sketch the UI, draw the component tree, decide where state lives

## How to run your week

| Days | Focus |
|---|---|
| 1 | Classes, properties, constructors, encapsulation. Build `Person`, `Student`, `Teacher` in isolation. |
| 2 | Inheritance and abstract classes. Interfaces. Rewrite day 1 with a proper hierarchy. |
| 3 | Polymorphism. One loop that calls the same method on different types and gets different behaviour. |
| 4 | Design the school domain on paper before you code it. Then code it. |
| 5 | React setup, JSX, components, props. Static school directory from a hardcoded array. |
| 6 | `useState`, lists, conditional rendering, splitting components. |
| 7 | Polish, README with your class diagram, commit, submit. |

> **Design on paper first.** Before you type a single class this week, draw the boxes and arrows. Which entities exist? What does each one know? What can each one do? Who owns whom? Fifteen minutes of drawing saves a day of refactoring, and the drawing goes in your README.

## Your AI licence this week: Red, with one exception

Still no generated code. But this week AI earns its keep as a design opponent. Use it to attack your model.

- "Here is my class hierarchy for a school. Do not rewrite it. Tell me three places it will break when requirements change."
- "Argue for using an interface instead of an abstract class in this case. Then argue the other way."
- "Give me five requirement changes a real school would ask for, so I can test whether my design survives them."
- "Quiz me: give me a scenario and ask whether it needs inheritance or composition."

You may use AI to explain a React error message. You may not use it to write a component.

## The build: School Management System, part 1

This project runs from week 3 to week 12 and becomes a real deployed application. Build the foundation properly.

### Backend requirements

Model a school in memory. No files, no database yet.

1. An abstract base type for a school member holding shared data: id, first name, last name, date of birth, and a computed `FullName` and `Age`.
2. `Student`, `Teacher` and `Principal` inherit from it. Each adds its own data. `Student` has an enrolment number and a year group. `Teacher` has a subject and a salary. `Principal` has an office number and a start date.
3. Every one of them has a `Describe()` method that behaves differently per type. Prove polymorphism by looping one collection of the base type and calling `Describe()` on each.
4. A `Department` class holding a name, a head teacher and a list of teachers.
5. A `Course` class with a title, a code, a teacher and a list of enrolled students. Enrolment has a capacity limit that is enforced.
6. A `School` class that owns departments, courses and people, and exposes methods like `EnrolStudent`, `AssignTeacherToCourse`, `TransferTeacher`.
7. An interface, for example `IReportable`, implemented by at least three types, with a menu option that prints a report for anything reportable.
8. Salaries, ages and capacity are protected by encapsulation. It must be impossible to set a negative salary or enrol into a full course from outside the class.
9. Console menu to add people, list them, enrol students and print reports.

### Frontend requirements

New Vite React project. Data comes from a hardcoded array in a `data.js` file for now.

1. A school directory page listing people as cards.
2. At least five components: `App`, `Header`, `PersonCard`, `PersonList`, `FilterBar`. Each in its own file.
3. `PersonCard` takes props and renders differently for a student, teacher or principal. No copy-pasted card components.
4. A filter bar with buttons for All, Students, Teachers. Filtering uses `useState`.
5. A search input that filters by name as you type.
6. An empty state: when the filter returns nothing, the user sees a helpful message, not a blank area.
7. A count showing how many people are currently visible.
8. Styled well enough that you would show it to someone. Plain CSS or Tailwind, your choice.

### Acceptance criteria

- [ ] One `List` of the base type holds students, teachers and the principal together
- [ ] Looping that list and calling `Describe()` produces three different output shapes
- [ ] Attempting to set a negative salary from `Main` does not compile or is rejected at runtime
- [ ] Enrolling a 31st student into a 30 seat course is refused with a clear message
- [ ] No class in the project is longer than 120 lines
- [ ] `Main` contains only menu handling
- [ ] React app has at least five components in separate files
- [ ] Changing the filter re-renders without a page reload
- [ ] Search and filter work together, not one cancelling the other
- [ ] Zero React key warnings in the browser console
- [ ] README contains your hand-drawn or diagrammed class model

## Explain it back

1. Why is `SchoolMember` abstract? What breaks if I make it concrete?
2. Show me the exact line where polymorphism happens and explain what the runtime does there.
3. When did you choose an interface over inheritance and why?
4. If the school now needs a Janitor who is paid but teaches nothing, where does that class go?
5. In React, why does calling `setCount(count + 1)` twice in a row only add one?
6. Where does the filter state live and why not lower down the tree?

## Stretch

- Add a `Grade` type and record grades per student per course
- Add sorting to the React directory by name, age or role
- Add a details view when a card is clicked

## Resources

- Microsoft Learn: object oriented programming in C#
- React docs: Describing the UI, and Adding Interactivity. The official tutorial only, ignore old blog posts
- Read about the Liskov substitution principle, one page, then find where your design violates it
