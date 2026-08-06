---
week: 14
phase: Phase 4 of 6, Depth
title: Real Time, File Uploads and Reading Other People's Code
standfirst: Two production features that every real app eventually needs, plus the skill nobody teaches and every employer needs on day one: dropping into an unfamiliar codebase and shipping a change without breaking it.
backend: SignalR, blob storage
frontend: Live updates, upload UX
license: Green
hours: 28 hrs
track: Capstone, sprint 2, plus cold codebase
---

## Read this first

Half of this week is your capstone. The other half is the exercise that most closely resembles your first month in a job: you will be handed a codebase you did not write, with a ticket, and asked to deliver.

Your first job will not be greenfield. It will be a decade-old system with three abandoned patterns in it and a test suite that half works. Reading code is the skill. Practise it here.

## What you are learning

### Real time

- Polling, long polling, server sent events and WebSockets. What each costs and when each is right
- SignalR: hubs, methods, groups, connection lifecycle
- Authenticating a SignalR connection with your existing tokens
- Scaling out: why sticky sessions or a backplane matter once there is more than one server
- Reconnection: exponential backoff, catching up on missed state, and telling the user honestly
- Handling a message that arrives twice, or out of order

### Files and storage

- Never store uploads in your application's file system. Why
- Azure Blob Storage or S3: containers, blobs, access tiers
- Direct-to-storage uploads with a pre-signed URL, and why routing files through your API does not scale
- Validating uploads properly: size, MIME type, actual content, filename sanitisation
- The security holes: unrestricted file type, path traversal, storing an executable, serving user content from your own origin
- Image processing: resizing, thumbnails, and doing it out of the request path
- Serving private files with short lived signed URLs

### Frontend

- Live updating UI: merging pushed data into a cached query without a full refetch
- Presence and typing indicators, done cheaply
- Upload UX: drag and drop, progress, cancel, retry, multiple files, the failure case
- Optimistic UI on a real time surface, and resolving conflicts when the server disagrees

### Reading unfamiliar code

- A repeatable approach: run it first, find the entry point, follow one request end to end, then read the tests
- Using search, call hierarchies and git history to understand why code is the way it is
- Making the smallest change that solves the ticket
- Knowing when to leave a mess alone and when to clean it

## How to run your week

| Days | Focus |
|---|---|
| 1 | Cold codebase day one: get it running, understand it, write your findings before changing anything. |
| 2 | Cold codebase day two: deliver the ticket with tests, and open a real PR. |
| 3 | Capstone: SignalR hub and a live updating surface. |
| 4 | Reconnection, missed messages, multi-tab behaviour. |
| 5 | File uploads with direct-to-storage and full validation. |
| 6 | Upload UX: progress, cancel, retry, failure. |
| 7 | Test the ugly paths, submit. |

> **Two hours before you type.** In the unfamiliar codebase, spend two hours reading and running before you change a line. Write a one page map: what the entry points are, where the data lives, what the three main flows are, and three things that surprised you. That map is graded.

## Your AI licence: Green, with a specific new use

AI is exceptional at the cold-codebase task and this is exactly how a professional uses it:

- "Here is a repository. Explain the architecture, the main flows and where I would add a new endpoint."
- "Trace how a request to `/api/orders` gets from the route to the database in this codebase."
- "What patterns does this codebase use consistently, so my change matches?"

Then verify by reading. AI will confidently describe a flow that does not exist. Your job is to check the map against the territory, and this week is deliberate practice at that.

For real time and uploads, the trap is different: generated upload code is very often insecure. Every generated upload handler must be reviewed specifically for file type validation, size limits, filename handling and where the file ends up.

## The build, part one: cold codebase ticket

You will be given a repository you have never seen and a ticket. Deliver:

1. `docs/codebase-map.md`: entry points, main flows, data model, three surprises, and the risky areas.
2. The feature or bug fix delivered, matching the existing conventions rather than importing your own.
3. Tests covering your change.
4. A pull request with a clear description, how to test, and any concerns you noticed but did not fix.
5. Nothing unrelated refactored. Restraint is being assessed.

## The build, part two: capstone sprint 2

### Requirements

1. One genuinely real time feature in your capstone. Not a demo. Something that is better because it is live: notifications, a shared board, live status, collaborative editing, a live queue.
2. SignalR hub authenticated with your existing tokens. Anonymous connections cannot subscribe to private groups. Prove it.
3. The client handles disconnection: shows a reconnecting state, backs off, reconnects, and reconciles what it missed.
4. Two browser tabs stay consistent with each other.
5. File upload feature: direct to blob storage using a pre-signed URL, never through your API body.
6. Upload validation: max size enforced on both ends, allowed types checked by content and not just extension, filenames sanitised, and a stored name that is not the user's name.
7. Upload UX with progress, cancel, retry on failure, and multiple files.
8. Private files served through short lived signed URLs. A copied URL stops working after expiry. Prove it.
9. Thumbnails generated outside the request path.

### Acceptance criteria

- [ ] Codebase map written before your first commit on the cold repo, with the git history proving the order
- [ ] Cold codebase ticket delivered with tests, in the house style, with no unrelated changes
- [ ] Two tabs open, an action in one appears in the other within a second
- [ ] Killing the network shows a reconnecting state, restoring it recovers without a refresh
- [ ] An anonymous socket cannot join a private group
- [ ] Uploading a 200MB file is rejected before the bytes are sent
- [ ] Renaming `virus.exe` to `photo.jpg` is still rejected
- [ ] A signed file URL returns an error after its expiry
- [ ] No file is stored on the API server's own disk
- [ ] Upload progress is accurate and cancel actually cancels

## Explain it back

1. Why SignalR here rather than polling? What did polling cost you?
2. What happens to a message sent while a client is disconnected?
3. Why is the upload not routed through your API?
4. How do you validate a file type, and why is the extension not enough?
5. In the cold codebase, what surprised you, and what did you decide not to touch?
6. Where did AI describe that codebase incorrectly, and how did you catch it?

## Stretch

- Add presence: who else is viewing this record right now
- Add resumable uploads for large files
- Add a virus scan step on upload

## Resources

- Microsoft Learn: SignalR, and scaling out with a backplane
- Azure Blob Storage or AWS S3 docs on pre-signed URLs
- OWASP file upload cheat sheet. Read it before you write the handler
