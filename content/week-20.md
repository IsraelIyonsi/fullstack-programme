---
week: 20
phase: Phase 5 of 6, AI Engineering
title: Retrieval, Vector Search and Evaluation
standfirst: Grounding a model in your own data, and then the skill almost nobody has: proving the feature actually works. Anyone can build a RAG demo. Being able to measure it is what makes you worth hiring for AI work.
backend: Embeddings, vector search, RAG
frontend: Citations and trust UX
license: Green
hours: 30 hrs
track: Capstone, AI feature part 2
---

## Read this first

Two halves this week and the second one matters more.

Retrieval is well documented and you will get a working version in two days. Evaluation is where teams fail: they ship, users complain that "the AI is wrong sometimes", and nobody can say whether last week's prompt change made it better or worse, because nothing was ever measured.

If you leave this programme with one AI skill that others lack, make it this: you can put a number on whether an AI feature works, and you can tell whether a change improved it.

## What you are learning

### Retrieval

- Why retrieval exists: models do not know your data, and putting everything in the context window does not scale
- Embeddings: text as vectors, semantic similarity, and what "close" means
- Vector databases and extensions: pgvector, Azure AI Search, Qdrant. Pick one, understand the tradeoff
- Chunking: size, overlap, and respecting document structure. Bad chunking is the most common cause of bad RAG
- Metadata filtering, and why it is usually more valuable than a better embedding model
- Hybrid search: keyword plus vector, and why pure vector search loses on exact terms, names and codes
- Reranking a shortlist for precision
- Prompt assembly: what you actually put in the context window and in what order
- Citations: making the model point at the source, and building the UI that shows it
- Handling "I do not know". A model that admits ignorance is more valuable than one that guesses
- Keeping the index in sync as source data changes

### Evaluation

- Why manual spot checking does not scale and does not catch regressions
- Building a golden dataset: 50 or more real inputs with known-good outputs
- Retrieval metrics: was the right chunk retrieved at all, and where did it rank
- Generation metrics: faithfulness to sources, relevance, correctness, refusal when appropriate
- LLM as judge: using a model to grade outputs, its biases, and validating the judge against human ratings
- Regression testing: an eval suite that runs in CI and fails on a drop
- Tracking cost and latency alongside quality, because all three move together
- Online signals: user feedback, thumbs, edits and abandonment

## How to run your week

| Days | Focus |
|---|---|
| 1 | Embeddings and similarity by hand. Embed 100 documents, query them, look at what comes back and why. |
| 2 | Chunking strategies. Compare three on the same corpus and record the difference. |
| 3 | RAG pipeline into your capstone, with citations. |
| 4 | Hybrid search and reranking. Measure whether each actually helped. |
| 5 | Build the golden dataset. 50 questions with known-good answers and known sources. |
| 6 | Eval harness: retrieval metrics, generation grading, cost and latency. Wire into CI. |
| 7 | Run evals against three prompt variants, pick with evidence, submit. |

> **Build the eval set before you tune anything.** If you tune first, every improvement is a feeling. Once the golden set exists, every change produces a number, and you will discover that at least one thing you were sure helped actually hurt.

## Your AI licence: Green

Very strong week for delegation, with one thing reserved for you.

**Delegate freely:** the pipeline plumbing, the chunking code, the eval harness, the CI wiring.

**Do not delegate:** the golden dataset. Write those 50 questions and expected answers yourself, from your real domain, including the awkward ones: ambiguous questions, questions the data cannot answer, questions with a trap. An AI-generated eval set tests what an AI thinks is important, which is exactly the blind spot you are trying to cover.

Useful prompts:

- "My retrieval returns plausible but wrong chunks for these three queries. Here is my chunking. What is likely wrong?"
- "Design an LLM-as-judge rubric for faithfulness with a 1 to 5 scale and explicit criteria per level."
- "What are the standard failure modes of RAG systems, and how would each show up in metrics?"

## The build: grounded, measured, and provably working

### Retrieval requirements

1. A retrieval feature over your own data. Real data from your capstone, not a sample PDF corpus.
2. Embeddings generated and stored in a vector store, with a documented chunking strategy and the reasoning behind the size and overlap you chose.
3. Metadata filtering so retrieval respects permissions. A user must never receive a chunk from a record they cannot access. Prove it with a test.
4. Hybrid search combining keyword and vector, with a measurement showing whether it beat vector alone on your golden set.
5. Citations in the response, linking to the actual source record, verifiable by the user in the UI.
6. A defined behaviour when nothing relevant is retrieved: the system says so rather than inventing an answer. Test it with an out-of-scope question.
7. Index kept in sync when source data changes, with the strategy documented.

### Evaluation requirements

1. `evals/golden-set.json` with 50 or more hand-written cases including at least 10 unanswerable or out-of-scope questions.
2. Retrieval evaluation: recall at k, and mean rank of the correct chunk.
3. Generation evaluation: faithfulness, relevance and correctness, graded with an LLM judge against a written rubric, with 10 cases also graded by you by hand to check the judge agrees.
4. Cost and latency recorded per run.
5. An eval command that runs the full suite and prints a report.
6. Eval run in CI, failing the build if the score drops more than an agreed threshold.
7. `docs/evaluation.md` with the results of at least three prompt or pipeline variants and the reasoning for the one you shipped.

### Acceptance criteria

- [ ] Golden set written by hand, with 10 or more unanswerable cases
- [ ] Eval suite runs with one command and produces retrieval and generation scores
- [ ] Three variants compared with numbers, and the winner chosen on evidence
- [ ] At least one change you expected to help made things worse, and it is documented
- [ ] A user cannot retrieve a chunk from data they lack permission for, proven by a test
- [ ] An out-of-scope question produces an honest "I do not know", not an invention
- [ ] Every answer shows citations the user can click and verify
- [ ] Your manual grades on 10 cases agree with the LLM judge, with the disagreements analysed
- [ ] CI fails when you deliberately degrade the prompt
- [ ] Cost and latency per query are known and recorded

## Explain it back

1. What chunk size did you choose and what did the alternatives score?
2. Show me a query where vector search alone failed and keyword saved it.
3. How does your system stop a user retrieving data they cannot see?
4. What is your faithfulness rubric, and where does the judge disagree with you?
5. Which change did you expect to help and did not?
6. How would you know next month if quality had degraded?

## Stretch

- Add query rewriting for follow-up questions in a conversation
- Add a reranker model and measure the precision gain against its latency cost
- Add an online feedback loop feeding real user ratings back into the eval set

## Resources

- pgvector or Azure AI Search documentation
- Read up on hybrid search and reciprocal rank fusion
- Anything credible on LLM evaluation. Prefer sources with numbers over sources with opinions
