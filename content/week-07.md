---
week: 07
phase: Phase 2 of 6, Persistence and APIs
title: Building Real APIs with ASP.NET Core
standfirst: The week everything connects. You will learn HTTP properly, build a Todo API as a teaching device, then expose your school over the network and consume it from Next.js. By Sunday you have a genuine full stack application.
backend: ASP.NET Core Web API, DTOs, Swagger
frontend: TanStack Query, real data
license: Yellow
hours: 30 to 34 hrs
track: Todo API, then School API
---

## Read this first

Two projects this week, deliberately. The Todo API is small enough that nothing distracts you from HTTP itself: verbs, status codes, routing, model binding, validation, content negotiation. Build it in two days. Then apply everything you learned to the school, which is big enough to teach you why DTOs exist.

If you only take one thing from this week: your API is a contract with strangers. Design it as if you will never get to explain it in person, because you will not.

## What you are learning

### HTTP, properly

- Request and response anatomy: method, path, headers, body, status
- Verbs and their meaning: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and idempotency
- Status codes that matter: 200, 201, 204, 400, 401, 403, 404, 409, 422, 500
- Where `201 Created` puts the new resource's URL and why
- Content types, JSON serialisation, and case conventions between C# and JavaScript
- CORS: what the browser is actually blocking and why your API must opt in
- Query strings versus route parameters versus body

### ASP.NET Core Web API

- Project setup, `Program.cs`, the middleware pipeline and the order it runs in
- Controllers versus minimal APIs. Build with controllers, understand both
- Attribute routing, route constraints, model binding from route, query and body
- DTOs: request models and response models, and why you never return an entity
- Mapping between entities and DTOs, by hand first
- Validation with data annotations and `FluentValidation`, returning a useful 400
- `ActionResult<T>` and returning the right status from every path
- `ProblemDetails` for consistent error responses
- Swagger and OpenAPI: annotate your endpoints so the docs are actually usable
- Dependency injection of your existing services into controllers. Nothing new to write

### Frontend

- TanStack Query: `useQuery`, `useMutation`, cache keys, invalidation
- Loading, error and empty states as first class UI, not afterthoughts
- A typed API client layer so components never call `fetch` directly
- Optimistic updates and rolling back a failed mutation
- Environment variables and pointing at a local API

## How to run your week

| Days | Focus |
|---|---|
| 1 | HTTP theory, then a Todo API: list, get, create, update, complete, delete. Test entirely in Swagger. |
| 2 | Add validation, correct status codes, `ProblemDetails`, and a filter query. Break it deliberately and fix the responses. |
| 3 | School API: controllers for students, teachers, courses, enrolments. |
| 4 | DTOs, validation, pagination, and Swagger annotations for the school API. CORS. |
| 5 | Frontend: typed API client, TanStack Query, replace the JSON fixtures with real calls. |
| 6 | Mutations: create, edit and delete a person against the live API, with proper states. |
| 7 | End to end check, README, submit. |

> **Test with Swagger before you touch the frontend.** If an endpoint is awkward to call in Swagger it will be worse in React. Fix the API design while it is still cheap.

## Your AI licence this week: Yellow

You will feel real temptation this week because AI writes CRUD controllers beautifully. Set the boundary here:

- **Write the Todo API entirely by hand.** All of it. This is your HTTP gym.
- For the school API, you may use AI for repetitive controller scaffolding and DTO mapping, after you have written the first controller yourself.
- Use it hard for review: "Here are my endpoints. Which ones return the wrong status code? Which are not RESTful? What would a client developer complain about?"
- Use it for test data and for generating a Postman collection.

Record every generated file in `ai-log.md` with a note on what you changed.

## The build, part one: Todo API

A small API you write from scratch, by hand.

1. `GET /api/todos` with optional `?completed=true` and `?search=` filters
2. `GET /api/todos/{id}` returning 404 when missing
3. `POST /api/todos` returning 201 with a Location header
4. `PUT /api/todos/{id}` for a full update
5. `PATCH /api/todos/{id}/complete` toggling completion
6. `DELETE /api/todos/{id}` returning 204
7. Validation: title required, 1 to 200 characters, due date not in the past. Failures return 400 with field level detail
8. Swagger UI documenting every endpoint, with example requests
9. In-memory storage is fine here. This project is about HTTP, not persistence

## The build, part two: School API and live frontend

### Backend requirements

1. Controllers for students, teachers, courses, departments and enrolments, all backed by the services you already wrote.
2. Separate request and response DTOs. No EF entity ever crosses the wire.
3. Pagination on all list endpoints: `?page=` and `?pageSize=`, with total count returned.
4. Filtering and sorting on the students and courses lists.
5. Validation on every write endpoint.
6. A global exception handling middleware returning `ProblemDetails`, never a stack trace.
7. CORS configured for your Next.js origin only, not `AllowAnyOrigin`.
8. Enrolment endpoint that returns 409 when the course is full and 404 when either id does not exist.
9. Swagger with descriptions, response types and examples.

### Frontend requirements

1. A typed API client in `lib/api/` with one function per endpoint. Components never call `fetch` directly.
2. TanStack Query for all reads, with sensible cache keys.
3. Every list page has a real loading state, a real error state with a retry button, and a real empty state.
4. Create, edit and delete a person against the live API, with the list invalidating and refreshing on success.
5. Enrol a student on a course from the course page, with the 409 full-course case shown as a clear message.
6. A visible error toast or banner when the API is down. Stop your API and check.
7. API base URL from an environment variable.

### Acceptance criteria

- [ ] Todo API written with no AI generated code, and you can say so honestly
- [ ] `POST` returns 201 and a `Location` header pointing at the new resource
- [ ] `DELETE` returns 204 with an empty body
- [ ] Requesting a missing id returns 404 with a `ProblemDetails` body, not HTML
- [ ] Posting an invalid body returns 400 listing the specific fields
- [ ] Enrolling into a full course returns 409 with a readable message
- [ ] No EF entity appears in any API response, verified by searching the controllers
- [ ] `GET /api/students?page=2&pageSize=10` returns page 2 and a total count
- [ ] Swagger UI documents every endpoint and can execute all of them
- [ ] The frontend has zero direct `fetch` calls outside `lib/api/`
- [ ] Stopping the API produces a friendly error UI, not a white screen
- [ ] `ai-log.md` updated

## Explain it back

1. When do you return 400 versus 422 versus 409?
2. Why does `PUT` need to be idempotent and `POST` not?
3. What is CORS blocking, exactly, and where is that decision made?
4. Why not return your EF entity directly? Give me two concrete reasons.
5. What is the middleware pipeline order in your `Program.cs` and what breaks if you move authentication after routing?
6. What cache key did you use for the student list and what happens when a mutation succeeds?

## Stretch

- Add API versioning at `/api/v1/`
- Add `ETag` and conditional requests on a resource
- Generate the TypeScript client from your OpenAPI spec instead of hand-writing it

## Resources

- Microsoft Learn: build a web API with ASP.NET Core, model validation
- MDN: HTTP response status codes, CORS
- TanStack Query docs: Queries, Mutations, Query Invalidation
