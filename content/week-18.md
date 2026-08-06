---
week: 18
phase: Phase 4 of 6, Depth
title: Security, and Reviewing Code You Did Not Write
standfirst: You will attack your own application, fix what you find, and then sit the review exercise that decides whether you have actually become an engineer: finding real defects in code that looks completely fine.
backend: OWASP, secure coding, dependencies
frontend: XSS, CSRF, CSP
license: Green
hours: 28 hrs
track: Capstone hardening, plus review assessment
---

## Read this first

Security is not a feature you add in week 18. It is the accumulated result of every decision you made in weeks 1 to 17. This week you find out how many of them were wrong.

The second half of this week is the most important assessment in the programme. You will be given code that compiles, passes its tests and looks professional, containing planted defects. Finding them is the job you are being hired to do, and it is the thing that separates an engineer from someone who assembles output.

## What you are learning

### The OWASP Top 10, against your own code

- Broken access control. The most common and most damaging. Test every endpoint as the wrong user
- Cryptographic failures: data in transit, data at rest, what needs encrypting and what needs hashing
- Injection: SQL, command, LDAP. Why parameterised queries fix it and string concatenation does not
- Insecure design: rate limits, business logic abuse, negative quantities, race conditions on limits
- Security misconfiguration: default credentials, verbose errors, open ports, permissive CORS
- Vulnerable dependencies: `dotnet list package --vulnerable`, `npm audit`, Dependabot
- Authentication failures: weak passwords, no lockout, session fixation, tokens that never expire
- Data integrity failures: unsigned webhooks, unverified packages
- Logging failures: no audit trail, or logging the things you must never log
- Server side request forgery

### Frontend security

- XSS: stored, reflected, DOM based. Where React protects you and where `dangerouslySetInnerHTML` removes that protection
- CSRF: what it is, why cookies make it possible, and how tokens and SameSite stop it
- Content Security Policy, and setting one that actually restricts something
- Security headers: HSTS, X-Content-Type-Options, Referrer-Policy, frame ancestors
- Secrets in the frontend bundle. There is no such thing as a secret in the frontend
- Dependency risk in the npm ecosystem, and typosquatting

### AI-specific security

- Prompt injection: untrusted content reaching a model that can act
- Never letting model output run as code or SQL without validation
- Data leakage into prompts and logs
- Over-trusting a model's output as an authorisation decision

### The review skill

- Reading a diff for correctness rather than style
- The questions that find real bugs: what happens with empty, with huge, with concurrent, with hostile, with null
- Distinguishing a defect from a preference, and writing a comment that gets fixed rather than resented

## How to run your week

| Days | Focus |
|---|---|
| 1 | OWASP Top 10 study, then a threat model of your capstone written down. |
| 2 | Attack your own app. Access control, injection, business logic. Log every attempt and result. |
| 3 | Fix everything you found. Write a regression test for each. |
| 4 | Frontend: CSP, headers, XSS review, dependency audit on both stacks. |
| 5 | **Review assessment.** A codebase with planted defects. Find them. |
| 6 | Review a classmate's capstone properly and receive their review of yours. |
| 7 | Fix what the review surfaced, publish your security notes, submit. |

> **Assume you will find something.** Every student in every previous cohort has found at least one real access control hole in their own app on day two. If you find nothing, you are not attacking properly, so bring your test log and we will look at it together.

## Your AI licence: Green, and this is a genuine strength

Use AI as an attacker. It is very good at generating hostile input and enumerating failure modes.

- "Here is my endpoint and its authorization. Give me ten requests that might bypass it."
- "Review this controller as a penetration tester. Rank findings by severity with reasoning."
- "What business logic abuse is possible here? Consider negative numbers, huge numbers, concurrency and repeated submission."
- "Generate malicious payloads to test this input handling."

**The limit you must respect:** AI review supplements your review, it never replaces it. In the assessment on day five, AI is not available. That is the point.

## The build, part one: harden your capstone

1. `docs/threat-model.md`: what you are protecting, from whom, and where the valuable data is.
2. A documented penetration test of your own app. Every attempt, every result, in `docs/pentest-log.md`. Minimum 25 attempts covering:
   - Calling every endpoint with no token, a wrong-role token and another user's token
   - Changing ids in URLs and bodies to access records you do not own
   - Injection attempts on every text input
   - Negative and enormous numbers where quantities and money are involved
   - Submitting the same limited action concurrently to beat a check
   - Uploading dangerous file types and oversized files
   - XSS payloads in every field that is later rendered
3. Every finding fixed, with a regression test that fails on the old code.
4. Security headers set and verified with an external scanner. CSP present and restrictive.
5. Dependency scans clean, or every remaining item justified in writing.
6. Secrets audit: nothing sensitive in the repo, the history, the frontend bundle or the logs.
7. If your capstone uses AI features, a specific prompt injection test with the mitigation documented.

## The build, part two: the review assessment

You will receive a repository with planted defects. No AI tools. Fixed time.

Deliver a review document containing, for each finding:

- Where it is, precisely
- What is wrong
- How it would fail in production, with a concrete scenario
- Severity, with reasoning
- The fix

There will be more findings than are obvious, and at least one that only appears under concurrency. There will also be things that look wrong and are fine. Flagging those costs you.

### Acceptance criteria

- [ ] Threat model written before the testing began
- [ ] 25 or more documented attack attempts with results
- [ ] Every real finding has a fix and a regression test that fails on the old code
- [ ] An external header scanner reports no missing critical headers
- [ ] CSP is present and actually blocks something, demonstrated
- [ ] `npm audit` and `dotnet list package --vulnerable` clean or justified
- [ ] No secret in repo, history, bundle or logs, verified
- [ ] Review assessment submitted within the time limit, no AI used
- [ ] A substantive review given to a classmate, with at least one real defect found
- [ ] Their review of your code acted on, with commits showing the response

## Explain it back

1. What is the most dangerous thing an authenticated user could do to your app right now?
2. Show me an access control hole you found in your own code. Why did you write it that way?
3. Why does React protect you from most XSS, and where does it stop?
4. What does your CSP block? Prove it.
5. In the review assessment, which defect did you nearly miss, and what made you catch it?
6. What did you flag that turned out to be fine, and what does that tell you?

## Stretch

- Add automated security scanning to CI: SAST, dependency and container scanning
- Add a rate limit specifically against business logic abuse, not just request volume
- Write a disclosure policy and a security contact for your app

## Resources

- OWASP Top 10, current edition, read fully
- OWASP cheat sheets for the areas you touch
- Microsoft Learn: ASP.NET Core security. And read your own git history for secrets before someone else does
