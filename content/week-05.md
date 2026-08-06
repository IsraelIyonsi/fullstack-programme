---
week: 05
phase: Phase 2 of 6, Persistence and APIs
title: Architecture, TypeScript and Saving to Disk
standfirst: You split one project into layers, learn dependency injection, and make the school survive a restart. On the frontend you move to TypeScript and Next.js, which is where you will stay for the rest of the programme.
backend: Layering, DI, JSON persistence
frontend: TypeScript and Next.js App Router
license: Yellow
hours: 28 to 32 hrs
track: School Management, part 3
---

## Read this first

Until now everything lived in one console project. That is fine for four weeks and fatal after that. This week you learn why professional codebases are split into layers, and you feel the benefit immediately: your domain logic stops knowing or caring whether data lands in a file, a database or a cloud bucket.

You also switch to TypeScript. It will slow you down for about three days and then speed you up forever.

## What you are learning

### Backend: structure

- Solutions and projects. `dotnet new sln`, adding class library projects, project references
- The layering you will use for the rest of the programme:
  - `Domain`: entities and business rules, references nothing
  - `Application`: interfaces, services, use cases
  - `Infrastructure`: file and database implementations
  - `Presentation`: the console app now, the API from week 7
- The dependency rule: dependencies point inward, never outward
- Dependency injection: what it is without a framework, then with `Microsoft.Extensions.DependencyInjection`
- Service lifetimes: transient, scoped, singleton, and the bug you get when you mix them wrong
- Programming against interfaces so you can swap `FileStudentRepository` for `SqlStudentRepository` in week 6 by changing one line
- `System.Text.Json`: serialise, deserialise, options, handling dates and enums
- Configuration with `appsettings.json` and `IOptions<T>`

### Frontend: TypeScript and Next.js

- Why TypeScript: types as documentation that cannot go stale
- Primitives, arrays, objects, unions, literal types, `type` versus `interface`
- Typing props, typing state, typing event handlers, generics in TypeScript
- `unknown` versus `any`, and why `any` is a defeat
- Next.js App Router: file based routing, `layout.tsx`, `page.tsx`, nested layouts
- Server components versus client components. When `"use client"` is required and why
- `loading.tsx`, `error.tsx`, and `not-found.tsx`
- Reading data on the server and passing it into a client component
- Tailwind CSS setup and utility-first styling

## How to run your week

| Days | Focus |
|---|---|
| 1 | Split the solution into four projects. Get it building with correct references. |
| 2 | Interfaces and DI. Register services in a container and resolve them. |
| 3 | JSON persistence in Infrastructure. Save and load the whole school. |
| 4 | TypeScript fundamentals. Convert last week's React app to `.tsx` and type everything. |
| 5 | Next.js: new project, App Router, layouts, routes, Tailwind. |
| 6 | Port the directory, detail page and form into Next.js. |
| 7 | README with an architecture diagram, submit. |

> **The dependency rule is the whole point.** Try to reference `Infrastructure` from `Domain`. Notice that nothing stops you. Then delete it, and understand that architecture is a discipline you enforce, not a feature the compiler gives you.

## Your AI licence this week: Yellow

Yellow is where most of your career will be spent, so learn to use it properly now.

**Good uses this week:**

- "Scaffold a `FileRepository<T>` that implements `IRepository<T>` using System.Text.Json. Explain each decision."
- "Convert this JavaScript component to TypeScript and tell me which types you inferred versus which you guessed."
- "What are the three most common mistakes when setting up DI service lifetimes?"

**The rule that keeps Yellow honest:** after AI writes something, close it, and rewrite the same thing yourself from a blank file. If you cannot, you have not earned the line. Note that in `ai-log.md`.

## The build: School Management System, part 3

### Backend requirements

1. Solution with four projects: `School.Domain`, `School.Application`, `School.Infrastructure`, `School.Console`.
2. `School.Domain` has zero project references and zero NuGet packages beyond the framework.
3. `IStudentRepository`, `ITeacherRepository`, `ICourseRepository` defined in Application, implemented in Infrastructure against JSON files.
4. A `SchoolService` in Application that holds the business rules (enrolment limits, department head rules) and depends only on interfaces.
5. The console app builds a DI container, registers everything and resolves the service. No `new` keyword for services in the console app.
6. Data persists to a `data/` folder as separate JSON files per entity type.
7. File paths and settings read from `appsettings.json`, not hardcoded.
8. Deleting the `data/` folder and restarting produces an empty but working school.

### Frontend requirements

1. A fresh Next.js project with TypeScript and Tailwind. This becomes your permanent frontend.
2. Routes: `/` dashboard, `/people`, `/people/[id]`, `/people/new`, `/courses`.
3. A shared root layout with navigation and a footer.
4. Types defined once in `types/index.ts` and imported everywhere. No duplicated shape definitions.
5. Data read from a local JSON file on the server side for now, matching the shape your API will return in week 7.
6. At least one server component doing the data read, passing into a client component for interactivity.
7. `loading.tsx` and `not-found.tsx` implemented and visibly working.
8. `strict: true` in `tsconfig.json`, and zero uses of `any` in your code.

### Acceptance criteria

- [ ] `School.Domain.csproj` contains no `ProjectReference` elements
- [ ] Swapping the file repository for a fake in-memory one is a one line change in the DI registration
- [ ] The console app compiles with no direct reference to `System.Text.Json`
- [ ] Killing the app mid-session and restarting loses nothing that was saved
- [ ] `npx tsc --noEmit` passes with zero errors
- [ ] Searching the frontend for `: any` returns nothing
- [ ] Navigating to `/people/does-not-exist` renders your not-found page
- [ ] A slow network shows your loading state, verified by throttling in DevTools
- [ ] README has an architecture diagram showing the four layers and the direction of dependencies
- [ ] `ai-log.md` updated

## Explain it back

1. Draw the four layers and the arrows. Why does `Domain` reference nothing?
2. What actually happens when the DI container resolves `SchoolService`?
3. Give me a scenario where registering a repository as a singleton causes a bug.
4. What is the difference between a server component and a client component, and how does the data get from one to the other?
5. Why did we type the API response shape before the API exists?
6. Show me one place TypeScript caught a bug you would have shipped.

## Stretch

- Add a second repository implementation storing CSV, and swap between them via config
- Add `Result<T>` return types instead of throwing for expected failures
- Add dark mode with Tailwind

## Resources

- Microsoft Learn: dependency injection in .NET, System.Text.Json
- TypeScript handbook: Everyday Types, and Object Types
- Next.js docs: App Router, Routing Fundamentals, Server and Client Components
