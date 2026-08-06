---
week: 19
phase: Phase 5 of 6, AI Engineering
title: Building With LLMs, Properly
standfirst: Until now you used AI to learn. Now you build with it. Calling models from .NET and Next.js, streaming, structured outputs, tool use, cost control, and the failure handling that separates a demo from a product.
backend: LLM APIs, streaming, tool use
frontend: Streaming UI, AI interaction design
license: Green
hours: 30 hrs
track: Capstone, AI feature
---

## Read this first

Every product you work on for the next several years will have someone asking to add an AI feature. Most of those features fail for the same three reasons: no evaluation, no failure handling, and no honest answer to whether the feature needed a model at all.

So the first question of this week is the one most teams skip: **does this feature need an LLM?** If a database query, a rule or a regex does the job, use that. It is cheaper, faster, deterministic and testable. Reserve the model for problems that are genuinely about language, ambiguity or open-ended synthesis.

## What you are learning

### The mechanics

- How an LLM API call actually works: messages, roles, system prompts, the request and response shape
- Tokens: what they are, how they are counted, how they map to cost and to the context limit
- Model selection: capability against latency against price, and why the biggest model is often the wrong default
- Temperature and other sampling parameters, and when determinism matters
- Streaming responses: server sent events, and why streaming changes perceived latency more than actual latency
- Structured output: making a model return JSON that matches a schema you can deserialise into a C# type, and validating it anyway
- Tool use and function calling: giving the model capabilities, and the security implications of every tool you expose
- Multi-turn conversation and managing a growing context window
- Prompt caching to cut cost on repeated context
- Rate limits, retries, timeouts and provider outages. The provider will be down, plan for it
- Cost control: token budgets per user, caps, monitoring, and alerting before the bill arrives

### Prompt engineering that survives contact with users

- Clear instruction, relevant context, explicit output format, worked examples
- Why "be helpful and accurate" does nothing and specific constraints do everything
- Handling refusals, truncation, hallucinated fields and malformed output
- Never trusting model output: validate, constrain, and keep a human in the loop for anything consequential
- Prompt injection when user content enters the prompt. Treat all model input as untrusted

### Frontend

- Streaming UI: token by token rendering, cancellation, and a stop button
- Designing for uncertainty: showing sources, confidence, and an easy way to correct the model
- Latency UX: what to show during a four second wait
- Failure states that keep the product usable when the model is unavailable

## How to run your week

| Days | Focus |
|---|---|
| 1 | Fundamentals. Make raw API calls with curl before any SDK. Read the response shape properly. |
| 2 | .NET integration: a service wrapping the provider, streaming, cancellation, retries. |
| 3 | Structured outputs into typed C# objects, with validation and a repair path. |
| 4 | Tool use: give the model two tools from your own API, safely. |
| 5 | Frontend streaming UI with cancellation. |
| 6 | Cost controls, rate limits, caching, and graceful degradation. |
| 7 | Write the honest feature assessment, submit. |

> **Build the non-AI version first.** Whatever your AI feature is, spend two hours building the dumb version: the search, the filter, the template. Compare them. Sometimes the dumb version wins, and knowing that is worth more to an employer than another chatbot.

## Your AI licence: Green

The irony of this week is real: use AI to build AI features. Where it helps most:

- "Design a JSON schema for this extraction task and explain what makes each field unambiguous."
- "Here is my prompt. Give me ten inputs that would break it."
- "Review this tool definition for prompt injection risk. What could a hostile user make it do?"
- "My model returns valid JSON 90% of the time. What are the standard techniques to get that to 99.9%?"

What you must do yourself: decide what the feature is for, what good output looks like, and what unacceptable output looks like. That is product judgement and it does not transfer.

## The build: an AI feature that survives users

### Requirements

1. One AI feature in your capstone that genuinely improves it. Written justification of why a model is the right tool, including what the non-model version looked like and why it lost.
2. A `LlmService` in your Application layer behind an interface. Your domain code never talks to a provider SDK directly, and you can swap providers by changing a registration.
3. Streaming end to end, from provider to API to browser, with a working stop button that actually cancels the upstream call.
4. Structured output: at least one call returning JSON matching a schema, deserialised into a typed object, validated, with a defined behaviour when validation fails.
5. Tool use: at least two tools exposed from your own API. Each tool validates its inputs and enforces the same authorisation as the equivalent endpoint. A tool must never be able to do something the calling user cannot do.
6. Cost controls: token limits per request, a per-user daily budget, logging of tokens and cost per call, and a dashboard or endpoint showing spend.
7. Resilience: timeouts, retry with backoff on rate limits, and a defined degraded experience when the provider is down. Test it by pointing at a dead endpoint.
8. Prompt injection defence: user content clearly separated from instructions, tools constrained, and a documented test showing an injection attempt failing.
9. `docs/ai-feature.md` covering: the problem, why a model, the prompt design, the failure modes, the cost per user per month at your expected usage, and what you would do if the price tripled.

### Acceptance criteria

- [ ] The non-AI alternative was built and compared, with the comparison written down
- [ ] Domain and Application code contains zero provider SDK references outside the adapter
- [ ] Streaming renders progressively, and stop cancels the upstream request, verified in the network tab
- [ ] Malformed model JSON is handled without a 500
- [ ] A tool cannot access data the current user is not authorised to see, proven by a test
- [ ] A per-user budget cap is enforced and produces a clear message at the limit
- [ ] Token and cost per call are logged and queryable
- [ ] Provider unavailable degrades gracefully, demonstrated
- [ ] A documented prompt injection attempt fails
- [ ] Cost per user per month is calculated with the assumptions stated

## Explain it back

1. Why does this feature need a model? What did the simple version get wrong?
2. What does one call cost, and what does 1,000 daily users cost you a month?
3. What happens when the model returns JSON missing a required field?
4. Show me a tool definition and tell me what a hostile user could try with it.
5. What is prompt injection and where is your app exposed to it?
6. The provider raises prices 3x tomorrow. What do you do?

## Stretch

- Add a smaller cheaper model for easy cases with escalation to a larger one
- Add prompt caching and measure the cost reduction
- Add a feedback control so users can rate outputs, and store it for next week's evaluation work

## Resources

- Your provider's API documentation, read fully rather than skimmed
- Read about structured outputs and tool use in the official docs, not blog summaries
- The OWASP Top 10 for LLM Applications
