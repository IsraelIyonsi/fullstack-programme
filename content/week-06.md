---
week: 06
phase: Phase 2 of 6, Persistence and APIs
title: Entity Framework Core and SQL Server
standfirst: Your data moves from a text file to a real relational database. You will learn SQL first, then Entity Framework Core on top of it, and you will learn to read the SQL your code generates so the database never becomes a black box.
backend: EF Core, SQL Server, migrations
frontend: Data tables, dynamic routes
license: Yellow
hours: 30 hrs
track: School Management, part 4
---

## Read this first

An ORM that you do not understand is a performance incident waiting to happen. So the order this week matters: SQL on days one and two, EF Core after that. If you learn EF Core first you will write code that produces a hundred queries where one would do, and you will not notice until a real user complains.

## What you are learning

### Database fundamentals, before any C#

- Tables, rows, columns, primary keys, foreign keys
- Data types and choosing them properly, including `decimal` for money again
- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`/`TOP`, `INSERT`, `UPDATE`, `DELETE`
- `JOIN`: inner, left, and why you rarely want a cross join
- `GROUP BY`, `HAVING`, aggregate functions
- Normalisation to third normal form, and when you would deliberately denormalise
- Relationships: one to many, many to many with a join table, one to one
- Indexes: what they cost, what they buy, when to add one

### Entity Framework Core

- `DbContext` and `DbSet<T>`
- Code first modelling, data annotations versus fluent API in `OnModelCreating`
- Migrations: `dotnet ef migrations add`, `dotnet ef database update`, and reading the generated file before you run it
- Configuring relationships and cascade delete behaviour
- Querying: `ToListAsync`, `FirstOrDefaultAsync`, `AnyAsync`, `Include` and `ThenInclude`
- The N+1 problem. Find it, prove it, fix it
- Change tracking, `SaveChangesAsync`, and `AsNoTracking` for read paths
- Seeding data
- Logging generated SQL to the console so you can see what EF actually sends

### Frontend

- Dynamic routes with `[id]` and route params in Next.js
- Rendering a real data table: sorting, empty states, loading skeletons
- Many-to-many data on screen: a course page listing its students
- Reusable UI pieces: `Table`, `Badge`, `EmptyState`, `Skeleton`

## How to run your week

| Days | Focus |
|---|---|
| 1 | Install SQL Server (or Docker SQL Server) and a query tool. Write thirty SQL queries by hand against a sample database. |
| 2 | Joins, grouping, indexes. Design the school schema on paper: tables, keys, relationships. |
| 3 | EF Core setup, `DbContext`, first migration, seeding. |
| 4 | Model the full school: one to many and many to many. Migrate. |
| 5 | Replace the JSON repositories with EF implementations. Nothing in Domain or Application changes. |
| 6 | Frontend: course detail page with enrolled students, sortable tables. |
| 7 | Verify, README with an ER diagram, submit. |

> **The proof that week 5 was worth it.** When you swap `FileStudentRepository` for `SqlStudentRepository`, your Domain and Application projects should not change by a single line. If they do, your layering was wrong and this is the week to fix it.

## Your AI licence this week: Yellow

Write your first thirty SQL queries by hand. No exceptions, no autocomplete. SQL is asked about in almost every backend interview and it is the thing juniors most often outsource entirely.

**Good uses:**

- "Explain this execution plan to me."
- "My query returns duplicate rows after a join. What are the usual causes?"
- "Review my schema. Where will this design hurt at a million rows?"
- "Generate seed data for 200 students as a C# seeding method."

**Required this week:** ask AI to review your schema before you migrate, and record what you accepted and rejected in `ai-log.md`.

## The build: School Management System, part 4

### Backend requirements

1. SQL Server running locally or in Docker, with a connection string in `appsettings.json` and secrets out of source control.
2. `SchoolDbContext` in Infrastructure with `DbSet`s for Students, Teachers, Departments, Courses and Enrolments.
3. Relationships modelled properly:
   - Department to Teachers is one to many
   - Course to Teacher is many to one
   - Students to Courses is many to many through an `Enrolment` entity carrying an enrolment date and a grade
4. Fluent API configuration for keys, required fields, string lengths, decimal precision on salary, and delete behaviour.
5. Migrations committed to the repo. Someone cloning your repo can run one command and get a working database.
6. Seed data: at least 3 departments, 10 teachers, 50 students, 8 courses, 150 enrolments.
7. EF implementations of your existing repository interfaces. Domain and Application untouched.
8. All queries async. All read-only queries use `AsNoTracking`.
9. At least one place where you found an N+1 problem, fixed it with `Include`, and documented the before and after query count in your README.
10. Reports from week 4 rewritten as database queries, still exposed through the same service interface.

### Frontend requirements

1. `/courses` page listing courses with teacher name, department and enrolment count.
2. `/courses/[code]` showing the course, its teacher and a table of enrolled students with grades.
3. `/people/[id]` showing a student with the courses they are enrolled on.
4. A sortable, searchable table component reused on at least two pages.
5. Loading skeletons rather than spinners for table data.
6. An empty state for a course with no students.
7. Data still read from a local JSON fixture that mirrors your database shape. The real API arrives next week.

### Acceptance criteria

- [ ] Thirty hand-written SQL queries committed in a `sql/practice.sql` file
- [ ] `dotnet ef database update` on a clean machine produces a working, seeded database
- [ ] The Enrolment table carries its own data, it is not a bare join table
- [ ] Salary column is `decimal(18,2)` in the generated migration, verified by reading it
- [ ] Deleting a department with teachers behaves the way you designed, not the way EF defaulted
- [ ] Generated SQL is logged and you can show me the query for the course detail page
- [ ] You can demonstrate an N+1 before and after, with query counts
- [ ] `School.Domain` and `School.Application` have zero EF Core references
- [ ] The courses table sorts by clicking a column header
- [ ] README contains an ER diagram
- [ ] `ai-log.md` updated

## Explain it back

1. Draw the school schema from memory. Mark the keys.
2. What does `Include` actually change about the SQL that gets sent?
3. What is `AsNoTracking` and why is it not the default?
4. Show me your N+1 and explain how you spotted it.
5. What happens on `SaveChangesAsync` if two of the three inserts fail?
6. Why is `Enrolment` an entity instead of just a many to many relationship?

## Stretch

- Add an index on a column your reports filter by and measure the difference
- Wrap a multi-step operation in a transaction and prove it rolls back
- Add soft delete with a query filter

## Resources

- Microsoft Learn: EF Core getting started, relationships, migrations
- Use The Index, Luke: the first three chapters on indexing
- Practise SQL on a site with a real query runner, not by reading
