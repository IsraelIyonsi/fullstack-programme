---
week: 02
phase: Phase 1 of 6, Fundamentals
title: Collections, Files and Modern JavaScript
standfirst: Your programs start holding data instead of throwing it away. You will learn arrays, lists, dictionaries and file input/output on the backend, and the JavaScript language properly on the frontend, including the async model that trips up every beginner.
backend: Collections, exceptions, file I/O
frontend: Modern JavaScript and async
license: Red
hours: 25 to 30 hrs
track: Calculator with History
---

## Read this first

Last week your calculator forgot everything the moment it closed. This week it remembers. That single change forces you to learn three things at once: how to hold many values, how to handle the ways that fails, and how to talk to the disk.

On the frontend you are still not using React. Resist the urge. React is a thin layer over JavaScript, and people who skip the JavaScript spend the next two years confused about why their state updates do not appear.

## What you are learning

### Backend: holding and persisting data

- Arrays versus `List<T>`, and when the fixed size of an array actually matters
- `List<T>` operations: `Add`, `Remove`, `Contains`, `Count`, indexing, iteration
- `Dictionary<TKey, TValue>`: lookup by key, `TryGetValue`, iterating pairs
- `HashSet<T>` and why membership checks are fast
- Strings are immutable. What that means for performance and `StringBuilder`
- Exceptions: `try`, `catch`, `finally`, `throw`, exception types, and when catching is wrong
- Writing your own exception messages that a future you can act on
- `System.IO`: `File.ReadAllText`, `File.WriteAllText`, `File.AppendAllLines`, `Path.Combine`
- Why you never hardcode `C:\Users\...` or a forward slash into a path
- `using` statements and why unmanaged resources need releasing

### Frontend: JavaScript as a real language

- `let` and `const`, scope, hoisting, and why you never use `var`
- Functions, arrow functions, default parameters, rest and spread
- Objects and arrays: destructuring, `map`, `filter`, `reduce`, `find`, `sort`
- Template literals
- ES modules: `import` and `export`, and `type="module"` in your script tag
- `JSON.stringify` and `JSON.parse`
- `localStorage` for browser persistence
- The event loop, the call stack, the task queue. Draw it once by hand
- Promises, `async` and `await`, `try/catch` around await
- `fetch` against a public API, handling a non-200 response

### Cross-cutting

- Reading a stack trace to the line that actually caused the failure
- Guard clauses and early returns instead of nested `if` pyramids
- Naming things: `CalculateTotal` beats `DoStuff2`

## How to run your week

| Days | Focus |
|---|---|
| 1 | Arrays and `List<T>`. Ten small exercises: reverse a list, find the max, remove duplicates. |
| 2 | Dictionaries and sets. Word-frequency counter from a paragraph of text. |
| 3 | Exceptions and file I/O. Write a program that reads a file that does not exist and handles it well. |
| 4 | Backend build: calculator saves and loads history. |
| 5 | JavaScript array methods and destructuring. Rewrite last week's `script.js` using them. |
| 6 | Promises, async/await, `fetch`. Then `localStorage`. |
| 7 | Frontend build, README, commit, submit. |

> **Do not skip the event loop.** Spend a full hour on it. Watch one good explainer, then draw the stack, the queue and the microtask queue on paper and trace three examples through it. Ninety percent of confusing frontend bugs for the next six months come from not having done this.

## Your AI licence this week: Red

Still Red. AI explains, quizzes and reviews. It does not type.

Use it like this:

- "Give me fifteen exercises on `Dictionary<TKey,TValue>` ordered from easy to hard. No solutions."
- "Trace this code and tell me the exact output order, then explain why." (paste an async snippet you wrote)
- "I think exceptions should be caught everywhere. Argue against me."
- "Review my error handling. Where am I swallowing an exception I should let bubble up?"

Do not ask it how to write your file persistence. That is the whole assignment.

## The build: Calculator with History

### Backend requirements

1. Every calculation is recorded as a history entry with the expression, the result and a timestamp.
2. History is held in a `List<T>` while the app runs.
3. Menu gains three options: view history, clear history, and export history.
4. On exit, history is written to `history.txt` in the app folder. On start, it is read back in.
5. If the file is missing, corrupt, or contains a bad line, the app starts with an empty history and tells the user what happened. It never crashes.
6. Add a stats option: total calculations, most used operation, largest result. Use a `Dictionary` for the operation counts.
7. All file paths built with `Path.Combine`, never string concatenation.

### Frontend requirements

1. Refactor `script.js` into ES modules: at least `calculator.js` (the logic) and `ui.js` (the DOM work). No calculation logic touches the DOM.
2. Add a history panel beside the keypad showing the last ten calculations.
3. History survives a page refresh using `localStorage`.
4. Clicking a history entry loads that result back into the display.
5. Add a Clear History button.
6. Add one async touch: a currency conversion button that fetches a live rate from a free public API and converts the current display value, with a visible loading state and a visible error state.

### Acceptance criteria

- [ ] Closing and reopening the console app shows the previous history
- [ ] Deleting `history.txt` while the app is closed does not break the next launch
- [ ] Putting garbage text into `history.txt` shows a warning, not a stack trace
- [ ] Stats correctly report the most used operation
- [ ] `calculator.js` contains zero references to `document`
- [ ] Refreshing the web page keeps the history panel populated
- [ ] The fetch button shows a spinner or Loading text while in flight
- [ ] Killing your wifi and clicking fetch shows a friendly error, not a blank screen
- [ ] At least ten commits, each one a single logical change

## Explain it back

1. When would you choose a `Dictionary` over a `List`? Give me a real example from your build.
2. What does `finally` guarantee and what does it not guarantee?
3. Why is catching `Exception` and doing nothing considered a bug?
4. What is the output order of a `console.log` before, inside and after an `await`? Why?
5. What does `fetch` do when the server returns 404? Does it throw?
6. Show me where you separated logic from the DOM and explain why that mattered.

## Stretch

- Store history as JSON instead of plain text lines
- Add a search box that filters the history panel as you type
- Add keyboard shortcuts and an undo for the last entry

## Resources

- Microsoft Learn: collections in C#, exception handling
- MDN: Array methods, Using promises, Working with JSON
- One good visual explainer on the JavaScript event loop, watched twice
