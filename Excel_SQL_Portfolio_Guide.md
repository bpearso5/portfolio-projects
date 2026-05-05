# Portfolio Strategy Notes — Excel + SQL Projects

This is a working document of how I'm thinking about my portfolio as I move into analyst and project coordinator roles. I built it before starting Project 1 because I didn't want to put 40+ hours into the wrong project for the wrong audience.

I'm sharing it in this repo for two reasons. First, it's a record of the reasoning behind the work — why I picked this project to build first, what I think hiring managers actually want to see, and what I'd build next. Second, the format itself is useful: a hiring manager who reads it gets a fast read on how I approach a problem before I start clicking around in Excel.

The plan is 3 to 5 polished projects over the next few months. Project 1 (Project Portfolio Tracker) is built and lives in this repo. The rest are queued. Notes below.

---

## Part 1 — How I'm thinking about this

### What I think hiring managers actually want to see

From the job descriptions I've been reading and conversations I've had, I don't think the bar for a Project Analyst, Business Analyst, Operations Analyst, or Project Coordinator role is "the most advanced SQL on the internet." I think it's three more boring things:

1. **Can I take messy real-world data and make it useful?** Cleaning, joining, structuring, standardizing — that's most of the actual work. Fancy syntax is the smaller part.
2. **Can I tie a query or a chart to a business decision?** I want my work to read as "the no-show rate is highest on Mondays, so we recommend X" — not just a SELECT statement floating in space.
3. **Can I communicate the work to someone who doesn't speak SQL?** Clear titles, plain-English summaries, and a "so what" section beat a wall of code every time.

The bar I'm setting for myself: would a manager trust me to own a weekly report or clean up a tracker without supervision? That's what I'm trying to prove with this portfolio.

### What I'm aiming for vs. what I'm avoiding

What I want to be true about my projects:

- A messy CSV that I cleaned with a documented step-by-step process.
- A SQL query that answers a real business question, not "show all customers."
- A pivot table or dashboard with a one-paragraph narrative explaining what changed and why it matters.
- A "Recommendations" section written like a manager would write it.
- Before/after artifacts showing improvement (raw data → cleaned data → insight).

What I'm trying to avoid:

- Ten different chart types on one dashboard with no story.
- SQL queries that are technically correct but answer nothing useful.
- Generic Kaggle datasets (Titanic, Iris) that thousands of other applicants have used.
- "Made a dashboard with KPIs" with no business context.
- Buzzwords ("synergy," "leveraged data-driven insights") without specifics.

### How many projects I'm planning

I've decided on 3 to 5 polished projects. One excellent project beats five mediocre ones. The pattern I'm following:

- **Project 1:** my strongest project, with full documentation. The one I'll point to in interviews.
- **Project 2:** different domain to show range (Project 1 is project tracking; Project 2 will be healthcare).
- **Project 3:** something that shows process improvement or before/after thinking.
- **Optional 4 & 5:** smaller, focused pieces — a dashboard, a SQL exercise notebook, a one-pager.

### What I think makes a portfolio look credible

- Consistent structure across every project (same headings, same flow).
- A README at the top explaining who I am, what roles I'm targeting, and what skills each project shows.
- Real screenshots of my Excel dashboards and SQL output, not just code blocks.
- A short "About" paragraph in my voice so it doesn't sound like a course assignment.
- Plain-English summaries first, technical details second. Hiring managers skim. Engineers read deeper. Both should be able to find what they need.
- Honesty about scope. "I built this with synthetic data to demonstrate X" is more credible than implying real client work.

---

## Part 2 — The 7 projects I evaluated

I shortlisted seven projects that fit my background (project management, operations, reporting). Each one was scored Beginner / Intermediate / Stretch based on how much new ground I'd have to cover.

### 1. Project Portfolio Tracker & Status Dashboard  *(Intermediate — the one I built first)*
**Scenario:** A 50-person services company runs ~20 active projects. Status updates live across email and spreadsheets. Leadership wants a single view of project health, budget burn, and at-risk work.

**Problem to solve:** Replace scattered status reports with one dashboard that shows which projects are on track, over budget, or behind schedule.

**Excel skills it would show:** Tables, XLOOKUP, SUMIFS, pivot tables, conditional formatting, dashboard layout, slicers, basic forecasting (% complete vs. % budget burned).

**SQL skills it would show:** Joins across projects/tasks/time entries/employees, GROUP BY with aggregations, CASE for status logic, CTEs for week-over-week comparisons, date functions.

**Why I picked it:** It mirrors exactly what a Project Analyst or PMO Coordinator does, which matches my background. Hiring managers in PMO, ops, and consulting recognize the shape of the problem instantly.

---

### 2. Patient Appointment & No-Show Analysis  *(Intermediate)*
**Scenario:** A multi-clinic outpatient practice loses revenue and capacity to no-shows. They want to know which clinics, providers, days, and patient segments drive the most missed appointments.

**Problem to solve:** Identify no-show patterns and recommend an intervention (reminder cadence, overbooking policy, scheduling rules).

**Excel skills:** Pivot tables by day-of-week and clinic, COUNTIFS for rate calculations, conditional formatting heatmaps, charts comparing before/after intervention scenarios.

**SQL skills:** Date/time functions, GROUP BY with multiple dimensions, CASE for segmentation (new vs. returning patient), window functions for rolling averages, subqueries for "patients with 3+ no-shows."

**Why it's on my list:** Healthcare operations is a domain I'm interested in, and no-show analysis is a real, recurring problem. Easy to anchor an interview answer to.

---

### 3. Employee Training & Compliance Tracker  *(Beginner-Intermediate)*
**Scenario:** HR needs to track who has completed required annual training (HIPAA, safety, security) across 200+ employees and flag who is overdue or expiring soon.

**Problem to solve:** Build a single source of truth for compliance status with automated overdue flags and a manager-facing dashboard.

**Excel skills:** XLOOKUP, conditional formatting for expiration dates, DATEDIF/EDATE, drop-down validation, dashboard for completion rate by department.

**SQL skills:** LEFT JOIN to find employees with missing courses, CASE for expiration status, date arithmetic (CURRENT_DATE - completion_date), GROUP BY department for compliance rate.

**Why it's on my list:** Shows process discipline and audit-readiness — valuable for ops, healthcare, and regulated industries.

---

### 4. Departmental Budget vs. Actual Tracker  *(Intermediate)*
**Scenario:** Finance wants department leads to see monthly budget vs. actual variance with color-coded alerts and a quarterly forecast.

**Problem to solve:** Replace a manual finance spreadsheet with a clean variance report and a forward-looking trend.

**Excel skills:** SUMIFS, variance formulas, % variance with conditional formatting, line charts for trend, basic forecasting (TREND or moving average), scenario tables.

**SQL skills:** Aggregations by month and department, joins between budget and actuals tables, CTEs for variance calculation, window functions for cumulative spend.

**Why it's on my list:** Every business has this problem. Recognizable to any hiring manager who has ever owned a P&L.

---

### 5. Customer Service Ticket Analysis  *(Intermediate)*
**Scenario:** A support team handles ~5,000 tickets per quarter. Leadership wants to know where tickets are backing up, which categories take longest, and who needs more capacity.

**Problem to solve:** Diagnose bottlenecks in the support workflow and recommend staffing or process changes.

**Excel skills:** Pivot tables, percentile calculations, average handle time, dashboard with filter slicers, charts for trend over time.

**SQL skills:** Date diffs for resolution time, GROUP BY with multiple aggregations, CASE for SLA-met/SLA-missed, window functions for ranking agents, CTEs for time-to-resolution buckets.

**Why it's on my list:** Operations and process-improvement framing. Easy to describe an intervention ("we recommended re-routing tier-1 tickets…").

---

### 6. Inventory & Reorder Analysis  *(Beginner-Intermediate)*
**Scenario:** A small distributor with 500 SKUs has stock-outs on fast movers and dead stock on slow movers. They need a reorder list and a slow-mover report.

**Problem to solve:** Surface what to reorder and what to discontinue, weekly.

**Excel skills:** SUMIFS, ABC analysis (Pareto), conditional formatting for reorder flags, pivot tables by category, charts for sell-through rate.

**SQL skills:** Joins between products, sales, and stock tables, GROUP BY product, CASE for reorder logic, subqueries to identify slow movers.

**Why it's on my list:** Concrete operational decision ("reorder these 27 SKUs") — clear, actionable output that's easy to demo.

---

### 7. Hiring Pipeline & Recruiting Funnel  *(Intermediate)*
**Scenario:** Recruiting is missing hire-by dates. Leadership wants to see funnel conversion (applied → screened → interviewed → offered → hired) and time-in-stage by role and recruiter.

**Problem to solve:** Identify where candidates are stalling and which stages drop the most.

**Excel skills:** Funnel chart, conversion rate calculations, pivot by recruiter/role, conditional formatting for stale candidates, dashboard layout.

**SQL skills:** Self-joins or stage tables, window functions for time-in-stage, GROUP BY recruiter, CASE for stage classification, CTEs for funnel rollup.

**Why it's on my list:** Clear narrative ("60% drop between screen and interview"). Translates to almost any pipeline analysis.

---

### My top 3
1. **Project Portfolio Tracker** — strongest match for my project management background.
2. **Patient Appointment & No-Show Analysis** — adds domain range (healthcare).
3. **Departmental Budget vs. Actual Tracker** — shows I can speak the language of finance and leadership.

### Why I picked Project 1 first
The Project Portfolio Tracker directly mirrors my work history, every hiring manager I want to talk to understands it instantly, and it gave me natural opportunities to use *every* core Excel and SQL skill in a single project. If I only got one project done, this is the one that would do the most work for me in interviews.

---

## Part 3 — How I structured the repo

For the Project Analyst / Business Analyst / Ops roles I'm targeting, my plan is:

- **GitHub repo (foundation, building now).** One repo as a portfolio hub, each project in its own folder with a clean README, the SQL files, the Excel file, and screenshots. Recruiters and technical screeners look here.
- **LinkedIn Featured section (next).** Pin the repo URL and a 1-page PDF case study from Project 1. This is what recruiters see in the first 10 seconds.
- **PDF case study (next).** A 2-3 page PDF with screenshots, business problem, approach, findings, and recommendations. Easy to attach to applications and email to interviewers.
- **Notion landing page (later, optional).** Could become a "front door" once I have 3+ projects. Skipping for now since the README already does a lot of this work.

I'm skipping a personal website until I have 3+ projects done — it adds cost and friction without much hiring upside at this stage.

### What's actually in this repo

```
portfolio-projects/
├── README.md                          ← project write-up + screenshots
├── project_tracker_dashboard.xlsx     ← the finished Excel workbook
├── Excel_SQL_Portfolio_Guide.md       ← this file (strategy notes)
├── GLOSSARY.md                        ← terms I'm learning as I go
├── interview_practice_prompt.md       ← coach prompt for Claude.ai
├── .gitattributes                     ← tells GitHub to count SQL in language stats
├── data/
│   └── raw/                           ← five synthetic CSVs
├── sql/
│   ├── 01_create_tables.sql           ← schema (PostgreSQL)
│   ├── 02_load_data.sql               ← \copy commands to load CSVs
│   ├── 03_analysis_queries.sql        ← 8 analysis queries
│   └── 04_sample_inserts.sql          ← INSERT statements for DB Fiddle
├── scripts/
│   ├── generate_data.py               ← rebuilds the CSVs (seed=42)
│   ├── build_workbook.py              ← rebuilds the .xlsx via openpyxl
│   └── generate_inserts.py            ← rebuilds the SQL inserts
└── images/
    ├── Dashboard_Screenshot_1.png
    ├── Dashboard_Screenshot_2.png
    ├── Dashboard_Screenshot_3.png
    ├── Database_Query.png
    ├── Exec_OnePager.png
    ├── sql_q2_portfolio_health.png
    └── sql_q5_duplicate_detection.png
```

A few notes on the choices: the .xlsx lives at the root because it's the headline deliverable — anyone who clicks "open this first" should see it without hunting. The Python scripts go in `scripts/` because they're tooling, not the work itself. The whole project is reproducible with two commands (`python3 scripts/generate_data.py` then `python3 scripts/build_workbook.py`). I'm keeping that pattern on every future project so the repos stay rebuildable.

### The structure I'm using for each project's write-up

```
1. Business Question / Problem    (2-3 sentences, plain English)
2. How to Review This Project     (where to look first)
3. Headline numbers               (the 5-bullet "what this build shows")
4. The Excel work                 (with screenshots)
5. The SQL work                   (with screenshots)
6. Business Recommendations       (what I'd tell the manager)
7. What's in this folder          (file map)
8. To regenerate from scratch     (the two commands)
9. What this project demonstrates (skills mapped to the work)
```

That's the template I used for the Project 1 README, and I'll reuse it for the rest.

---

## Part 4 — Project 1: Design choices and what I learned

The full README for Project 1 (with live numbers and screenshots) lives at the top of this repo. This section is just my notes on the design decisions and what I'd do differently next time.

### Why these five tables

I started with the business questions, not the data. The questions were: which projects are healthy, which are at risk, which are over budget, who's overworked, and is there a data-quality problem hiding under any of it. I worked backwards to figure out what tables I'd need: `projects` (the headline entity), `tasks` (to compute % complete), `time_entries` (to compute capacity), `employees` (to put names on things), `project_budget_actuals` (to compute % burned). That gave me five tables with real foreign keys between them — enough to demo joins without becoming overwhelming.

### The health flag was the most important design choice

A raw number — "actual is $48,213 vs. budget $45,000" — is just a number. A label — "Over Budget" — tells you what to do. So the headline query (Q2) doesn't just show numbers, it produces a three-way flag:

- `Over Budget` if total actual > total budget
- `At Risk` if (% budget burned) − (% complete) > 15 percentage points
- `On Track` otherwise

The 15-point threshold was the most arbitrary part. I picked it because it produces a reasonable distribution on this dataset — about half the projects are On Track, a quarter At Risk, a fifth Over Budget. In a real engagement I'd defend the threshold by tying it to historical data (e.g., "projects that crossed 15 points in our archive ended up overrun 70% of the time"). For a synthetic-data portfolio piece, "this is a tunable parameter and here's why I picked the value I did" is the answer I'd give in an interview.

### What the actual numbers came out to

After running the data generator and the queries, this is what the build produced:

- 20 projects across 5 tables (~3,000 rows total).
- 11 On Track (55%), 5 At Risk (25%), 4 Over Budget (20%).
- $95,524 total cost overrun, concentrated in 4 projects.
- 245 overdue tasks across the portfolio.
- 10 employees overallocated for ≥3 of the last 8 weeks.
- 14 duplicate time entries surfaced via the data-quality check.

The thing I'm proudest of is the duplicate-detection query. It surfaced exactly the 14 duplicates I planted in the data — proof the check works, and a clean way to demonstrate "data quality" is part of analyst work, not just a buzzword.

### The headline query (Q2)

I'm including this one inline because it's the one I'm most likely to walk through in an interview. The other seven queries live in `sql/03_analysis_queries.sql`.

```sql
WITH task_progress AS (
    SELECT
        project_id,
        COUNT(*) AS total_tasks,
        SUM(CASE WHEN status = 'Done' THEN 1 ELSE 0 END) AS done_tasks
    FROM tasks
    GROUP BY project_id
),
budget_rollup AS (
    SELECT
        project_id,
        SUM(budgeted_amount) AS total_budget,
        SUM(actual_amount)   AS total_actual
    FROM project_budget_actuals
    GROUP BY project_id
)
SELECT
    p.project_name,
    p.client_name,
    ROUND(100.0 * tp.done_tasks / NULLIF(tp.total_tasks, 0), 1) AS pct_complete,
    br.total_budget,
    br.total_actual,
    ROUND(100.0 * br.total_actual / NULLIF(br.total_budget, 0), 1) AS pct_budget_burned,
    CASE
        WHEN br.total_actual > br.total_budget THEN 'Over Budget'
        WHEN (100.0 * br.total_actual / NULLIF(br.total_budget,0))
             - (100.0 * tp.done_tasks / NULLIF(tp.total_tasks,0)) > 15 THEN 'At Risk'
        ELSE 'On Track'
    END AS health_flag
FROM projects p
LEFT JOIN task_progress tp ON tp.project_id = p.project_id
LEFT JOIN budget_rollup br ON br.project_id = p.project_id
ORDER BY pct_budget_burned DESC NULLS LAST;
```

The two CTEs (named subqueries) handle each rollup separately — task progress in one, budget in the other. Without them, the SELECT statement would have nested aggregations and become hard to read. The `NULLIF` guards protect against divide-by-zero if a project has zero tasks. The `LEFT JOIN`s mean even projects without any tasks or budget records still appear in the result.

### What I'd do differently next time

A few things I'd change on the next project:

- **Plan the screenshots before building.** I built the workbook, then realized I needed to take screenshots, then realized two of them looked confusing without a caption. Next time I'll think about the README story first and let that drive what the dashboard needs to show.
- **Write the SQL inserts script earlier.** I built the dataset using Python and CSVs, which is great for openpyxl but not for sharing the data with someone running the SQL queries online. I added the `generate_inserts.py` script late. Next project I'll plan for "anyone should be able to load this dataset into DB Fiddle in 30 seconds" from the start.
- **Don't over-engineer the data quality demo.** I planted exactly 14 duplicates, which is a perfect number for the screenshot but a slightly artificial-looking result. Next time I'd plant a more uneven number (e.g., 7 duplicates from one source, 3 from another, 2 from a third) so the data-quality query tells a richer story.

---

## How I'd talk about this project in an interview

These are the bullet points I've prepared for resume + cover letter use, and the conversational versions I've practiced for screens.

### Resume bullets

- Designed and built a project portfolio dashboard in Excel and SQL covering 20 projects and 50 staff, surfacing 4 over-budget projects and a $95K cost-overrun pattern in a single weekly view.
- Wrote 8 SQL analysis queries (PostgreSQL, with CTEs, joins across 5 tables, CASE logic) to standardize messy project-status data and calculate budget-burn vs. percent-complete health flags.
- Built an executive Excel dashboard with 1,265 formulas (XLOOKUP, COUNTIFS/SUMIFS, conditional formatting, charts) and a print-ready 1-page summary used to recommend re-baselining 4 over-budget projects.
- Identified 10 overallocated employees by analyzing 8 weeks of time entries and 14 duplicate time-tracking records via a SQL data-quality check.

### How I'd answer common interview questions

**"Tell me about a project you're proud of."**
"I built a project portfolio dashboard for a 50-person services-firm scenario — 20 projects, five tables in SQL, around 3,000 rows. The interesting part was the at-risk logic. I flagged any project where budget burn was running more than 15 points ahead of percent complete. That surfaced four projects that were technically on schedule but spending faster than the work justified. In a real engagement, that's the difference between catching an overrun in week 3 vs. at month-end close."

**"Walk me through a SQL query you wrote."**
"My headline query joins projects, tasks, and budget actuals using two CTEs. One rolls up tasks to a percent-complete number, the other rolls up monthly budget records to actual spend per project, and the outer query combines them with a CASE statement that produces an On Track / At Risk / Over Budget flag. I used `NULLIF` to guard against divide-by-zero on the percent calculations — a small detail that comes up the moment you have a project with no tasks logged yet."

**"How do you handle messy data?"**
"In this project, project status values came in with mixed case and inconsistent terms — 'In Progress', 'in-progress', 'INPROGRESS' — because real PMs update statuses by typing them differently. I wrote a CASE statement to normalize them into a clean set of values. Separately, I wrote a duplicate-detection query on time entries using `HAVING COUNT(*) > 1` that flagged 14 duplicate rows. That kind of check is what I'd want running every week before any labor-cost analysis."

**"What was the business impact?"**
"The dashboard replaces five separate PM status emails. The COO gets a same-format view every Monday, and the at-risk logic gives a 2-3 week head start on cost overruns instead of finding them at month-end close. My recommendations included re-baselining the four over-budget projects, redistributing work from overallocated staff, and opening a structured conversation with one client whose two projects accounted for half the overrun."

**"Why did you pick this project?"**
"It mirrors what I've already done in project management roles — keeping track of multiple workstreams, status, budget, and capacity — but it lets me show I can do it with SQL and Excel as a single repeatable pipeline instead of as a manually maintained spreadsheet. It was also the project that let me demonstrate every core skill — joins, CTEs, CASE, GROUP BY, conditional formatting, XLOOKUP, KPI cards — in one piece of work."

---

## What I'm doing next

1. **Project 2: Patient Appointment & No-Show Analysis.** Different domain (healthcare), same depth as Project 1. This is the queue-up.
2. **A 1-page PDF case study from Project 1** to pin to LinkedIn Featured.
3. **Resume + LinkedIn updates** using the bullets above, with a link back to this repo.
4. **Practice the interview answers above out loud** until I can deliver each one in under 90 seconds without notes.
