---
week: 17
phase: Phase 4 of 6, Depth
title: Distributed Systems and Microservices Literacy
standfirst: You will split one service out of your monolith, connect it with messaging, put a gateway in front, and add tracing across both. Then you will write down why, for your product, you would probably not do this in real life.
backend: Messaging, gateway, resilience, tracing
frontend: Consuming a distributed backend
license: Green
hours: 30 hrs
track: Capstone, sprint 5
---

## Read this first

You are learning microservices this week so you can work in a company that has them and so you can argue competently against building them when they are not needed. Both matter, and the second one will make you unusual.

Most teams that adopted microservices too early paid for it with distributed transactions, untraceable failures and a deploy pipeline nobody understood. Your capstone almost certainly does not need them. Do the exercise, then write the honest assessment.

## What you are learning

### The concepts

- Monolith, modular monolith, service oriented, microservices. Where each is appropriate
- Service boundaries drawn around business capabilities, not around database tables
- The fallacies of distributed computing. Read the list and remember the first one: the network is reliable
- CAP in plain language, and what "eventually consistent" costs your users
- Distributed transactions and why two-phase commit is avoided. The saga pattern with compensation
- The outbox pattern for publishing an event and committing a database change atomically
- Idempotent consumers, again, because at least once delivery is again the rule
- Data ownership: one service owns its data and nobody else reads its tables

### The mechanics

- Messaging with RabbitMQ or Azure Service Bus: queues, topics, subscriptions, consumer groups
- Events versus commands, and naming them properly
- MassTransit for publish, consume, retry and the outbox
- API gateway with YARP: routing, aggregation, cross cutting concerns in one place
- Service discovery and configuration in a multi-service world
- Resilience: timeouts, retries, circuit breakers, bulkheads, and graceful degradation
- OpenTelemetry: distributed tracing across services, spans, context propagation, Jaeger or Aspire dashboard
- Correlation ids that survive a hop through a queue
- Local development for multiple services: compose, .NET Aspire, or a run script

## How to run your week

| Days | Focus |
|---|---|
| 1 | Concepts and boundary design. Draw your system as services on paper and justify every line. |
| 2 | Extract one service. Give it its own data and its own deploy. |
| 3 | Messaging between the two, with retries and idempotent consumers. |
| 4 | Outbox pattern and one saga with a compensating action. |
| 5 | Gateway in front, plus resilience policies. |
| 6 | OpenTelemetry across everything. Trace one user action end to end through the queue. |
| 7 | Write the honest assessment, submit. |

> **Extract exactly one service.** Not four. One, chosen because it has a genuinely different scaling or ownership profile: notifications, reporting, file processing, search. Then feel the cost. The cost is the lesson.

## Your AI licence: Green, and use it for the design argument

Excellent week for using AI as an opponent rather than an author.

- "Here is my domain. Propose three different service boundary designs and argue for and against each."
- "I am extracting notifications into its own service. What breaks that I have not thought about?"
- "Explain the outbox pattern and show me the race condition it prevents."
- "My trace shows a 3 second gap between two spans. What are the usual causes, ranked?"

And the one that matters most this week, asked honestly after you have built it:

**"Given this system, this team size and this traffic, argue that microservices are the wrong choice here."**

Your written assessment must engage with that argument rather than dismiss it.

## The build: capstone sprint 5

### Requirements

1. One service extracted from your capstone, running independently, with its own data store and its own deployment. It must not read the main service's tables.
2. Communication by asynchronous messaging for anything that does not need an immediate answer. Synchronous calls only where a user is waiting.
3. Consumers are idempotent. Delivering the same message three times has the same effect as delivering it once. Proven by a test.
4. Outbox pattern implemented so that publishing an event and committing your database change cannot diverge.
5. One saga with a compensating action: a multi-step flow where step three fails and steps one and two are correctly undone. Proven by a test.
6. YARP gateway in front of both services as the single entry point for the frontend. The frontend knows one base URL.
7. Resilience policies on every cross-service call: timeout, retry with backoff, and a circuit breaker. Killing the second service must degrade the app, not break it.
8. OpenTelemetry tracing across the gateway, both services and the message broker, viewable in Jaeger or the Aspire dashboard. Correlation survives the queue hop.
9. One command brings the entire system up locally.
10. `docs/architecture-assessment.md` containing:
    - Your service boundary design and the reasoning
    - What became harder after the split, specifically and honestly
    - What you would actually do for this product at your real expected scale, with the reasoning
    - The cost of this architecture in deployment, debugging and local development

### Acceptance criteria

- [ ] Two services deploy independently. One can be redeployed without touching the other
- [ ] The extracted service owns its data. No cross-service database access anywhere
- [ ] Replaying the same message three times produces one effect, proven by a test
- [ ] Killing service two leaves the app usable with a degraded feature, not an error page
- [ ] The circuit breaker opens under sustained failure and recovers, demonstrated
- [ ] One trace shows a user action crossing gateway, service one, the broker and service two
- [ ] A saga failure at step three leaves the system in a correct state, proven by a test
- [ ] One command starts everything locally
- [ ] The architecture assessment argues honestly against the thing you just built

## Explain it back

1. Why that boundary and not another one?
2. What race condition does the outbox pattern prevent? Draw the timeline.
3. Your consumer receives the same event twice. Walk me through what happens.
4. Service two is down for an hour. What does the user experience, and what happens to the messages?
5. Show me a trace and explain what each span cost.
6. Would you build this as microservices for real? Convince me either way with evidence.

## Stretch

- Add a second consumer and prove competing consumers scale throughput
- Add schema versioning for your events and handle an old consumer receiving a new event
- Add a chaos test that randomly kills a service during the suite

## Resources

- Microsoft: .NET microservices architecture ebook, free
- MassTransit documentation: consumers, retries, outbox, sagas
- OpenTelemetry .NET docs. Read the fallacies of distributed computing, all eight
