---
week: 15
phase: Phase 4 of 6, Depth
title: Background Jobs, Payments and Integrations
standfirst: Work that happens after the response is sent, and code that talks to systems you do not control. Payments are the sharpest teacher here because money makes correctness non-negotiable and forces you to learn idempotency properly.
backend: Hosted services, queues, webhooks
frontend: Checkout and async status UX
license: Green
hours: 30 hrs
track: Capstone, sprint 3
---

## Read this first

Anything slow, unreliable or not needed for the response belongs outside the request. Email, reports, image processing, third party calls, notifications. Users should never wait for work they did not ask to watch.

Then there is the other half: you are now calling systems you do not own. They will be slow. They will be down. They will return something not in their documentation. They will call you back twice for the same event. Engineering for that is what this week teaches.

## What you are learning

### Background work

- `IHostedService` and `BackgroundService` in ASP.NET Core
- Scheduled work with Quartz or Hangfire, and Hangfire's dashboard
- Queue based work: producer, consumer, and why a queue beats a database poll
- Retries with exponential backoff and jitter
- Dead letter queues and what you do with what lands in one
- At least once delivery means your handler will run twice. Design for it
- Idempotency keys, and making an operation safe to repeat
- Long running jobs: progress reporting, cancellation, and jobs that outlive a deploy

### Integrations and webhooks

- Calling an external API well: `HttpClient` via `IHttpClientFactory`, never `new HttpClient()`
- Timeouts, retries, circuit breakers with Polly
- Handling partial failure. What state is your system in when their call succeeded and yours failed
- Receiving webhooks: verifying the signature, responding fast, processing asynchronously
- Replay protection and duplicate delivery
- Sandbox credentials, and never testing against live

### Payments, as the worked example

- The payment flow: intent, confirmation, webhook, fulfilment
- Why you never trust the client's "payment succeeded" message
- Stripe or Paystack: checkout session, webhook events, refunds, failure cases
- Subscriptions: trials, renewals, upgrades, downgrades, cancellations, failed renewals
- Reconciliation, and holding an audit trail of every state change
- What you must never store, and what PCI scope actually means for you

### Frontend

- Checkout UX: clear pricing, a single obvious action, and honest error messages
- The pending state: the payment is submitted and the webhook has not landed yet. Design for it
- Polling or live updating a job status with progress
- Notifying the user when background work completes, in-app and by email

## How to run your week

| Days | Focus |
|---|---|
| 1 | Background services and scheduled jobs. Move one slow thing out of the request. |
| 2 | Queues, retries, dead letters, idempotency. |
| 3 | Transactional email through a provider, with templates and a retry path. |
| 4 | Payment integration in sandbox: checkout, redirect, webhook, fulfilment. |
| 5 | Failure paths: declined card, abandoned checkout, duplicate webhook, out of order events. |
| 6 | Frontend: checkout, pending state, job progress, completion notification. |
| 7 | Break it on purpose, prove it recovers, submit. |

> **The duplicate webhook drill.** Take a webhook you have already processed and send it again, five times. If your user gets charged twice, upgraded twice, or emailed five times, you have not learned idempotency yet. This is the single most important exercise of the week.

## Your AI licence: Green, with a money rule

The rule for this week: **AI may write the integration, you must write the failure matrix.**

Before generating anything, write out by hand every way the flow can fail, and what the correct system state is for each: card declined, user closes the tab after paying, webhook arrives before your database write commits, webhook arrives twice, webhook never arrives, your server dies mid-fulfilment, refund issued outside your app.

Then use AI: "Here is my failure matrix. Implement the handler so every row holds. Then tell me which rows you are least confident about."

Good prompts this week:

- "What are the five most common ways developers get Stripe webhooks wrong?"
- "Review this handler for idempotency. Show me a sequence of events that produces a double charge."
- "Design a retry policy for this call and explain the jitter."

## The build: capstone sprint 3

### Requirements

1. At least one thing moved out of the request path into a background job, with a written before and after response time.
2. A scheduled recurring job that does something real for your product: a digest, a cleanup, a reminder, a report.
3. Retries with exponential backoff and a dead letter path. Failures are visible somewhere a human will look, not swallowed.
4. Transactional email through a real provider, with templates, in sandbox.
5. A payment or paid third party integration in sandbox mode, complete with:
   - Checkout flow initiated from your app
   - Webhook endpoint with signature verification
   - Idempotent fulfilment keyed on the provider's event id
   - Correct handling of declined, abandoned and duplicate events
   - An immutable audit trail of every state change with timestamps
6. `docs/failure-matrix.md` listing every failure mode, the expected system state and the test that proves it.
7. Polly on every outbound call, with timeouts and a circuit breaker.
8. Frontend: checkout journey, a pending state that resolves when the webhook lands, background job progress, and a completion notification.

### Acceptance criteria

- [ ] Sending the same webhook five times produces exactly one fulfilment, proven by a test
- [ ] An unsigned or wrongly signed webhook is rejected with the correct status
- [ ] A declined card leaves the user informed and the system unchanged
- [ ] Closing the browser immediately after paying still results in correct fulfilment
- [ ] A failed background job retries with growing delays and lands in a dead letter path
- [ ] Dead letter items are visible to a human somewhere
- [ ] The external API being down does not take your app down, proven by pointing it at a dead URL
- [ ] Response time for the slow endpoint dropped measurably, with numbers in the README
- [ ] `docs/failure-matrix.md` complete, with a test referenced per row
- [ ] No card data ever touches your servers or your logs

## Explain it back

1. Walk me through every step from clicking Pay to the feature being unlocked, including who calls whom.
2. Why can you not trust the redirect back from the payment provider?
3. What is your idempotency key and why that one?
4. The webhook arrives before your own database commit. What happens?
5. What is in your dead letter queue right now, and who looks at it?
6. Your provider is down for two hours. What does your user see, and what happens when it recovers?

## Stretch

- Add subscriptions with trials, upgrades and dunning for failed renewals
- Add an admin screen to replay a dead lettered job
- Add invoice PDF generation as a background job

## Resources

- Microsoft Learn: background tasks with hosted services
- Polly documentation: retry, timeout, circuit breaker
- Your payment provider's docs on webhooks, idempotency and testing. Read all three fully
