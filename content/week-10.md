---
week: 10
phase: Phase 3 of 6, Production Concerns
title: Authentication and Authorization
standfirst: Who are you, and what are you allowed to do. You will implement identity, JWT access and refresh tokens, and role and policy based authorization on the API, then wire session handling and protected routes into Next.js.
backend: Identity, JWT, policies
frontend: Auth.js, protected routes
license: Yellow
hours: 30 to 34 hrs
track: School Management, part 7
---

## Read this first

Authentication is who you are. Authorization is what you may do. Most security bugs juniors ship are authorization bugs: the endpoint checks that you are logged in and forgets to check that the record belongs to you. Build the habit this week of asking, on every single endpoint, "whose data is this and who is asking."

Never roll your own password hashing, token format or crypto. Use the framework. The only thing you should invent here is your policy model.

## What you are learning

### Backend

- Authentication versus authorization, in one sentence each, from memory
- Password storage: hashing, salting, why bcrypt/PBKDF2/Argon2 and never plain SHA256
- ASP.NET Core Identity: user store, password rules, lockout, email confirmation flow
- JWT structure: header, payload, signature. Decode one by hand at jwt.io and understand every claim
- Signing keys, expiry, issuer and audience validation
- Access tokens versus refresh tokens. Why access tokens are short lived
- Refresh token rotation and revocation, and storing refresh tokens server side
- Where tokens live in the browser: httpOnly cookies versus localStorage, and the XSS tradeoff
- `[Authorize]`, roles, claims, and policy based authorization with requirements and handlers
- Resource based authorization: this teacher may edit this course because they teach it
- Getting the current user in a service without leaking `HttpContext` through your layers
- Common failures: missing authorization on one endpoint, IDOR, token in a URL, no expiry

### Frontend

- Auth.js (NextAuth) with a credentials provider against your API
- Sessions, the session callback, and typing the session object
- Middleware for route protection in Next.js
- Server side auth checks versus client side hiding. Client side hiding is cosmetic, never a control
- Conditional UI by role, done from a single source of truth
- Handling token expiry: silent refresh, and a clean redirect to login when it fails
- Login, logout, and a redirect back to the page the user wanted

## How to run your week

| Days | Focus |
|---|---|
| 1 | Auth theory. Decode JWTs by hand. Read the OWASP authentication cheat sheet. |
| 2 | Identity setup, register and login endpoints, password rules, token issuing. |
| 3 | Refresh tokens with rotation and revocation. Logout that actually invalidates. |
| 4 | Roles and policies across the API. Resource based checks. |
| 5 | Auth.js in Next.js, login page, session, middleware. |
| 6 | Role-aware UI, protected routes, expiry handling. |
| 7 | Try to break your own auth. Document what you tried. Submit. |

> **Attack your own app on day seven.** Call an admin endpoint with a student token. Change the id in the URL to someone else's record. Send an expired token. Send a token signed with a different key. Remove the Authorization header entirely. Write down what happened for each. If any of them succeeded, you have found the most valuable bug of your week.

## Your AI licence this week: Yellow, with a hard rule

AI is a good teacher for auth concepts and a dangerous author of auth code, because auth code that looks right and is wrong still compiles and still passes a happy path test.

**Do:**

- "Explain refresh token rotation and what attack it prevents."
- "Review my JWT validation configuration. What am I not validating?"
- "Here is my authorization policy. Give me five requests that would bypass it."
- "What are the OWASP top authorization failures and how would each look in ASP.NET Core?"

**Do not:** paste in a generated auth setup and move on. Every line of your auth configuration must be one you can defend. This is the one area where "it works" is not evidence of anything.

## The build: School Management System, part 7

### Backend requirements

1. ASP.NET Core Identity wired to your existing database, with a `User` linked to a `Student`, `Teacher` or `Principal` record.
2. `POST /api/auth/register` and `POST /api/auth/login` returning an access token and a refresh token.
3. Access token expires in 15 minutes. Refresh token expires in 7 days, is stored server side, and rotates on every use.
4. `POST /api/auth/refresh` and `POST /api/auth/logout`. Logout revokes the refresh token so it cannot be reused. Prove this with a test.
5. Three roles: Admin, Teacher, Student. Every endpoint has an explicit authorization decision, including the ones that are deliberately public.
6. Policy examples that must exist:
   - Only Admin can create or delete teachers and departments
   - A Teacher can edit grades only for courses they teach
   - A Student can read only their own enrolments and grades
7. Resource based authorization implemented with a handler, not with an `if` inside the controller.
8. Password rules enforced, and account lockout after repeated failures.
9. Integration tests covering: no token gives 401, wrong role gives 403, other user's resource gives 403 or 404, expired token gives 401, revoked refresh token gives 401.

### Frontend requirements

1. Auth.js configured against your API with a credentials provider.
2. A login page with proper error handling for wrong credentials and for a locked account.
3. Middleware protecting `/people`, `/courses` and everything under `/admin`.
4. Session available on both server and client, and correctly typed.
5. Navigation and actions change by role. A Student never sees a Delete button, and the API would refuse it anyway.
6. Token expiry handled: the user is refreshed silently, or sent to login with a return URL if refresh fails.
7. A visible logged-in state with the user's name and a working logout.

### Acceptance criteria

- [ ] Passwords are never stored or logged in plain text, verified by inspecting the database
- [ ] A student token calling `DELETE /api/teachers/1` returns 403
- [ ] Student A requesting Student B's grades is refused
- [ ] A logged out refresh token returns 401 on reuse
- [ ] Every controller action has an explicit `[Authorize]` or `[AllowAnonymous]`
- [ ] Removing a policy from one endpoint makes a named test fail
- [ ] The frontend never decides permissions on its own, it mirrors the API
- [ ] Expired access token triggers a refresh without the user noticing
- [ ] `docs/security-notes.md` lists the attacks you attempted and the results
- [ ] `ai-log.md` updated

## Explain it back

1. What is inside a JWT, and what stops me editing the payload and sending it back?
2. Why is the access token short lived if the refresh token is not?
3. Where did you store the tokens in the browser and what did you trade away by choosing that?
4. Show me an endpoint and tell me exactly who can call it and how that is enforced.
5. What is IDOR? Show me the code that prevents it in your app.
6. If your signing key leaked tonight, what would you do in the morning?

## Stretch

- Add Google or GitHub OAuth as a second login option
- Add two factor authentication with an authenticator app
- Add an audit log of privileged actions with the acting user and timestamp

## Resources

- Microsoft Learn: ASP.NET Core Identity, policy based authorization
- OWASP cheat sheets: Authentication, Authorization, JWT
- Auth.js docs: Credentials provider, callbacks, middleware
