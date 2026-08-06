---
week: 01
phase: Phase 1 of 6, Fundamentals
title: Variables, Logic and the Debugger
standfirst: You will write your first C# program, learn how a computer actually holds your data, and learn to use a debugger before you learn to use anything else. On the web side you will build a page by hand, with no framework in sight.
backend: C# syntax and the debugger
frontend: HTML, CSS, the DOM
license: Red
hours: 25 to 30 hrs
track: Console Calculator
---

## Read this first

You are going to spend six months turning into an engineer who can build and ship a complete product on their own. This week is the smallest and the most important. Everything after it assumes you understand what happens when you write `int x = 5;`.

You have AI available. This week you are mostly not allowed to use it to write code, and that restriction is deliberate. The market is full of people who can prompt their way to a working app and cannot debug it when it breaks. That person does not get hired twice. Read the licence section below before you touch anything.

## What you are learning

### Backend: C# and .NET

- What .NET is, what the runtime does, what the SDK does, what a project file is
- `dotnet new`, `dotnet run`, `dotnet build` from the terminal, not just from an IDE button
- Value types and reference types: `int`, `long`, `double`, `decimal`, `bool`, `char`, `string`
- Why `decimal` exists and why you never use `double` for money
- Declarations, assignment, `var`, and when explicit types read better
- Operators, operator precedence, integer division and the traps in it
- `if`, `else if`, `switch` and switch expressions
- Loops: `for`, `while`, `do while`, `foreach`, plus `break` and `continue`
- Methods: parameters, return values, overloading, `static`
- String interpolation, `Console.ReadLine`, `Console.WriteLine`
- Parsing input safely with `int.TryParse` and `decimal.TryParse`
- The stack and the heap, at a level you can draw on paper

### Frontend: the web platform

- How a browser request actually works: URL, DNS, HTTP request, response, render
- HTML that means something: `header`, `nav`, `main`, `section`, `form`, `label`, `button`
- CSS basics: selectors, the box model, colours, typography, flexbox
- Chrome DevTools: Elements, Styles, Console, Network
- Your first JavaScript: variables, functions, `document.querySelector`, event listeners

### Cross-cutting: the skill nobody teaches you

- Setting a breakpoint, stepping over, stepping into, reading the call stack
- Inspecting a variable's live value in the watch window
- Reading an error message from the top down and finding the line number
- Git: `init`, `add`, `commit`, `push`, and writing a commit message a human can read

## How to run your week

You have roughly 25 to 30 focused hours. Spread them like this.

| Days | Focus |
|---|---|
| 1 | Install the .NET SDK, VS Code or Rider, Node, Git. Get `dotnet run` printing Hello World. Create your GitHub repo. |
| 2 | Types, variables, operators, input and parsing. Write ten tiny programs, not one big one. |
| 3 | Control flow and loops. Then methods. Refactor day 2 code into methods. |
| 4 | The debugger. Deliberately break your own code five times and find each bug with breakpoints only. No print statements. |
| 5 | HTML and CSS. Build the calculator's face with no JavaScript behind it. |
| 6 | JavaScript events. Make the buttons respond. |
| 7 | Finish the build, write the README, commit, submit. |

> **The ten tiny programs rule.** Beginners learn faster from ten fifteen-line programs than from one two-hundred-line program. Small programs fail fast and teach fast. Do not build the calculator on day two.

## Your AI licence this week: Red

Red means AI is a tutor and never a typist.

**Allowed:**

- "Explain the difference between the stack and the heap like I am new."
- "Why does this error say Object reference not set to an instance of an object?"
- "Quiz me on C# value types. Ask me ten questions and mark my answers."
- "Here is code I wrote. Do not rewrite it. Tell me what a senior engineer would flag and why."
- "Give me five practice exercises on loops. Do not give me the answers."

**Not allowed:**

- Asking for code that you then paste into your project.
- Asking it to fix your bug before you have spent twenty minutes in the debugger.
- Autocomplete that writes whole lines for you. Turn Copilot or Cursor tab completion off this week.

**The test:** if I sat you at an empty editor with no internet, could you retype the file? If no, you have not learned it yet, you have collected it.

## The build: Console Calculator v1

Build a calculator that runs in the terminal. It looks trivial. It is not, once you handle the input properly.

### Backend requirements

1. Program starts, prints a short banner, and shows a menu of operations: add, subtract, multiply, divide, quit.
2. User picks an operation, then enters two numbers.
3. Program prints the result formatted to two decimal places, then loops back to the menu.
4. Every operation lives in its own method with a clear name, parameters and a return value. Nothing but menu handling lives in `Main`.
5. Invalid input never crashes the program. Letters where a number belongs produce a clear message and a retry.
6. Dividing by zero produces a clear message, not an exception dump.
7. Use `decimal` for the numbers, not `double`.

### Frontend requirements

Build a single `index.html` page with `style.css` and `script.js`. No framework, no build tool, no npm.

1. A calculator keypad: digits 0 to 9, the four operators, equals, and clear.
2. A display area showing the current entry and the result.
3. Laid out with flexbox or grid so it looks deliberate, not like a school project.
4. Clicking buttons updates the display. Equals computes. Clear resets.
5. It works on a phone-width screen. Check it in DevTools device mode.
6. No inline styles and no inline `onclick`. CSS in the stylesheet, listeners added in JavaScript.

### Acceptance criteria

Your submission is accepted when all of these are true.

- [ ] `dotnet run` starts the console calculator with no errors
- [ ] Typing `abc` at a number prompt shows a friendly message and asks again
- [ ] Dividing by zero shows a friendly message and returns to the menu
- [ ] `Main` is under 40 lines and contains no arithmetic
- [ ] The web calculator computes 7 x 8 = 56 and 10 / 4 = 2.5 correctly
- [ ] Clear resets the display to 0 from any state
- [ ] The page has no console errors in DevTools
- [ ] Repo has at least eight commits with messages that describe the change
- [ ] `README.md` explains what it is, how to run both parts, and what you found hard

## Explain it back

Before your session, be ready to answer these out loud with your editor closed. This is the part that decides whether the week counted.

1. What is the difference between a value type and a reference type? Draw it.
2. Why `decimal` and not `double` for money?
3. What does `int.TryParse` return, and why is it better than `int.Parse` here?
4. Walk me through what happens when the user types `5`, then `/`, then `0`.
5. Show me a breakpoint you set this week and what you learned from it.
6. What does `document.querySelector` return when nothing matches?

## Stretch, only if the core is done

- Add a percent and a sign-flip button to the web calculator
- Add keyboard support so number keys and Enter work
- Add a memory feature: M+, MR, MC
- Support chained operations so `2 + 3 + 4` gives 9 without pressing equals twice

## Resources

- Microsoft Learn: C# fundamentals path, the first three modules only
- MDN: HTML elements reference, CSS box model, Introduction to events
- Your debugger's documentation. Actually read it. Twenty minutes now saves you fifty hours later.
