# Portfolio Strategy Notes — Excel + SQL Projects

This is a working document of how I'm thinking about my portfolio as I move into analyst and project coordinator roles. I built it before starting Project 1 because I didn't want to put 40+ hours into the wrong project for the wrong audience.

I'm sharing it in this repo for two reasons. First, it's a record of the reasoning behind the work — why I picked this project to build first, what I think hiring managers actually want to see, and what I'd build next. Second, the format itself is useful: a hiring manager who reads it gets a fast read on how I approach a problem before I start clicking around in Excel.

The plan is 3 to 5 polished projects over the next few months. Project 1 (Project Portfolio Tracker) is built and lives in this repo. The rest are queued. Notes below.

---

## Part 1 — Portfolio Strategy

### What employers actually want to see
Hiring managers screening Project Analyst, Business Analyst, Operations Analyst, Project Coordinator, MIS, and reporting roles are not looking for the most advanced SQL on the internet. They are looking for three things:

1. **Can you take messy real-world data and make it useful?** Cleaning, joining, structuring, and standardizing matters more than fancy syntax.
2. **Can you tie a query or a chart to a business decision?** They want to see "the no-show rate is highest on Mondays, so we recommend X" — not just a SELECT statement.
3. **Can you communicate the work to a non-technical stakeholder?** Clear titles, plain-English summaries, and a "so what" section beat a wall of code every time.

The bar is "would a manager trust this person to own a weekly report or clean up a tracker without supervision?" That is what your portfolio has to prove.

### What is impressive vs. what is fluff

**Impressive**
- A messy CSV that you cleaned with a documented step-by-step process.
- A SQL query that answers a real business question (not "show all customers").
- A pivot table or dashboard with a one-paragraph narrative explaining what changed and why it matters.
- A "Recommendations" section written like a manager would write it.
- Before/after screenshots showing improvement (e.g., raw data → cleaned data → insight).

**Fluff**
- 10 different chart types on one dashboard with no story.
- SQL queries that are technically correct but answer nothing useful.
- Generic Kaggle datasets (Titanic, Iris) that thousands of other applicants have used.
- "Made a dashboard with KPIs" with no business context.
- Heavy use of buzzwords ("synergy," "leveraged data-driven insights") without specifics.

### How many projects you really need
**3 to 5 polished projects.** That is the sweet spot. One excellent project beats five mediocre ones. The pattern that works:

- **Project 1:** Your strongest project, with full documentation. This is what you point to in interviews.
- **Project 2:** Different domain to show range (e.g., if Project 1 is project tracking, Project 2 could be healthcare or finance).
- **Project 3:** Something that shows process improvement or "before/after" thinking.
- **Optional 4 & 5:** Smaller, focused pieces — a dashboard, a SQL exercise notebook, a one-pager.

### What makes a portfolio look polished and credible
- **Consistent structure** across every project (same headings, same flow).
- **A README at the top** explaining who you are, what roles you are targeting, and what skills each project shows.
- **Real screenshots** of your Excel dashboards and SQL output, not just code blocks.
- **A short "About" paragraph in your voice** so it does not sound like a course assignment.
- **Plain-English summaries first, technical details second.** Hiring managers skim. Engineers read deeper. Both should be able to find what they need.
- **Honesty about scope.** "I built this with synthetic data to demonstrate X" is more credible than implying real client work.

---

## Part 2 — Project Ideas (the 7 strongest fits for your background)

Each project is scored: Beginner / Intermediate / Stretch.

### 1. Project Portfolio Tracker & Status Dashboard  *(Intermediate — RECOMMENDED STARTER)*
**Scenario:** A 50-person services company runs ~20 active projects. Status updates live across email and spreadsheets. Leadership wants a single view of project health, budget burn, and at-risk work.

**Problem you solve:** Replace scattered status reports with one dashboard that shows which projects are on track, over budget, or behind schedule.

**Excel skills shown:** Tables, XLOOKUP, SUMIFS, pivot tables, conditional formatting (RAG status), dashboard layout, slicers, basic forecasting (% complete vs. % budget burned).

**SQL skills shown:** Joins across projects/tasks/time entries/employees, GROUP BY with aggregations, CASE for status logic, CTEs for "current week vs. last week" comparisons, date functions.

**Why it's portfolio-strong:** It mirrors exactly what a Project Analyst or PMO Coordinator does. Hiring managers in PMO, ops, and consulting recognize this immediately.

---

### 2. Patient Appointment & No-Show Analysis  *(Intermediate)*
**Scenario:** A multi-clinic outpatient practice loses revenue and capacity to no-shows. They want to know which clinics, providers, days, and patient segments drive the most missed appointments.

**Problem you solve:** Identify no-show patterns and recommend an intervention (reminder cadence, overbooking policy, scheduling rules).

**Excel skills shown:** Pivot tables by day-of-week and clinic, COUNTIFS for rate calculations, conditional formatting heatmaps, charts comparing before/after intervention scenarios.

**SQL skills shown:** Date/time functions, GROUP BY with multiple dimensions, CASE for segmentation (new vs. returning patient), window functions for rolling averages, subqueries for "patients with 3+ no-shows."

**Why it's portfolio-strong:** Healthcare operations is a hot domain, and no-show analysis is a real, recurring problem. Easy to talk about in interviews.

---

### 3. Employee Training & Compliance Tracker  *(Beginner-Intermediate)*
**Scenario:** HR needs to track who has completed required annual training (HIPAA, safety, security) across 200+ employees and flag who is overdue or expiring soon.

**Problem you solve:** Build a single source of truth for compliance status with automated overdue flags and a manager-facing dashboard.

**Excel skills shown:** XLOOKUP, conditional formatting for expiration dates, DATEDIF/EDATE, drop-down validation, dashboard for completion rate by department.

**SQL skills shown:** LEFT JOIN to find employees with missing courses, CASE for expiration status, date arithmetic (CURRENT_DATE - completion_date), GROUP BY department for compliance rate.

**Why it's portfolio-strong:** Shows you understand process discipline and audit-readiness — valuable for ops, healthcare, and regulated industries.

---

### 4. Departmental Budget vs. Actual Tracker  *(Intermediate)*
**Scenario:** Finance wants department leads to see monthly budget vs. actual variance with color-coded alerts and a quarterly forecast.

**Problem you solve:** Replace a manual finance spreadsheet with a clean variance report and a forward-looking trend.

**Excel skills shown:** SUMIFS, variance formulas, % variance with conditional formatting, line charts for trend, basic forecasting (TREND or moving average), scenario tables.

**SQL skills shown:** Aggregations by month and department, joins between budget and actuals tables, CTEs for variance calculation, window functions for cumulative spend.

**Why it's portfolio-strong:** Every business has this problem. Recognizable to any hiring manager who has ever owned a P&L.

---

### 5. Customer Service Ticket Analysis  *(Intermediate)*
**Scenario:** A support team handles ~5,000 tickets per quarter. Leadership wants to know: where are tickets backing up, which categories take longest, and who needs more capacity?

**Problem you solve:** Diagnose bottlenecks in the support workflow and recommend staffing or process changes.

**Excel skills shown:** Pivot tables, percentile calculations, average handle time, dashboard with filter slicers, charts for trend over time.

**SQL skills shown:** Date diffs for resolution time, GROUP BY with multiple aggregations, CASE for SLA-met/SLA-missed, window functions for ranking agents, CTEs for time-to-resolution buckets.

**Why it's portfolio-strong:** Operations and process-improvement framing. Easy to describe an intervention ("we recommended re-routing tier-1 tickets…").

---

### 6. Inventory & Reorder Analysis  *(Beginner-Intermediate)*
**Scenario:** A small distributor with 500 SKUs has stock-outs on fast movers and dead stock on slow movers. They need a reorder list and a slow-mover report.

**Problem you solve:** Surface what to reorder and what to discontinue, weekly.

**Excel skills shown:** SUMIFS, ABC analysis (Pareto), conditional formatting for reorder flags, pivot tables by category, charts for sell-through rate.

**SQL skills shown:** Joins between products, sales, and stock tables, GROUP BY product, CASE for reorder logic, subqueries to identify slow movers.

**Why it's portfolio-strong:** Concrete operational decision ("reorder these 27 SKUs") — reviewers love clear, actionable output.

---

### 7. Hiring Pipeline & Recruiting Funnel  *(Intermediate)*
**Scenario:** Recruiting is missing hire-by dates. Leadership wants to see funnel conversion (applied → screened → interviewed → offered → hired) and time-in-stage by role and recruiter.

**Problem you solve:** Identify where candidates are stalling and which stages drop the most.

**Excel skills shown:** Funnel chart, conversion rate calculations, pivot by recruiter/role, conditional formatting for stale candidates, dashboard layout.

**SQL skills shown:** Self-joins or stage tables, window functions for time-in-stage, GROUP BY recruiter, CASE for stage classification, CTEs for funnel rollup.

**Why it's portfolio-strong:** Clear narrative ("60% drop between screen and interview"). Translates to almost any pipeline analysis.

---

### Top 3 to build first
1. **Project Portfolio Tracker** — strongest match for your project management background.
2. **Patient Appointment & No-Show Analysis** — shows domain range (healthcare).
3. **Departmental Budget vs. Actual Tracker** — shows you can speak the language of finance/leadership.

### Best first project to build now
**Project Portfolio Tracker.** Reasons: it directly mirrors your work history, every hiring manager understands it instantly, and it gives you natural opportunities to show *every* core Excel and SQL skill in a single project.

---

## Part 3 — Portfolio Format Recommendation

For someone targeting Project Analyst / Business Analyst / Ops roles, my plan is:

- **GitHub repo (foundation, building now).** One repo as a portfolio hub, each project in its own folder with a clean README, the SQL files, the Excel file, and screenshots in `/images`. Recruiters and technical screeners look here.
- **LinkedIn Featured section (next).** Pin the repo URL and a 1-page PDF case study from Project 1. This is what recruiters see in the first 10 seconds.
- **PDF case study (next).** A 2-3 page PDF with screenshots, business problem, approach, findings, and recommendations. Easy to attach to applications and email to interviewers.
- **Notion landing page (later, optional).** Could become the "front door" once I have 3+ projects — a single page with my bio, project summaries with screenshots, and links into the repo. Skipping for now since the README already does a lot of this work.

Skipping a personal website until I have 3+ projects done — it adds cost and friction without much hiring upside at this stage.

### What to include in each format

**GitHub repo structure (this is the actual layout I use, what you see in this repo):**
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

A few notes on the choices: the .xlsx lives at the root because it's the headline deliverable — anyone who clicks "open this first" should see it without hunting. The Python scripts go in `scripts/` because they're tooling, not the work itself. The whole project is reproducible with two commands (`python3 scripts/generate_data.py` then `python3 scripts/build_workbook.py`), which I'll keep doing on every project so the repos stay rebuildable.

**Notion landing page:**
- Header: name, role you're targeting, location, contact links.
- One-paragraph "About" — your background and where you're going.
- "Skills at a glance" — Excel, SQL, [your other tools]. Short, no skill bars.
- 3-5 project cards, each linking to its case study and GitHub.
- Resume download button.

**Per-project structure (use this template for every project):**

```
1. Project Title
2. Business Problem        (2-3 sentences, plain English)
3. Tools Used              (Excel, SQL, etc.)
4. Dataset Overview        (tables, row counts, source/synthetic)
5. Process / Approach      (3-5 numbered steps)
6. SQL Queries Used        (2-3 highlight queries with comments)
7. Excel Analysis          (screenshots of pivots, dashboard, charts)
8. Key Findings            (3-5 bullet points, each with a number)
9. Business Recommendations (what would you tell the manager?)
10. What This Project Demonstrates (skills mapped to the work)
```

---

## Part 4 — First Project: Full Build

# Project 1 — Project Portfolio Tracker & Status Dashboard

## Business Problem
A regional services firm (~50 employees, ~20 active client projects at any time) struggles to get a clear weekly view of project health. PMs report status in different formats. Leadership cannot quickly see which projects are over budget, behind schedule, or at risk. The COO has asked for a single, repeatable view of project portfolio health that updates from clean source data each week.

## Tools Used
- **SQL** (PostgreSQL syntax — works in BigQuery, MySQL, SQL Server with minor changes) for data modeling, cleaning, and analysis.
- **Microsoft Excel** for the dashboard, formulas, pivot tables, conditional formatting, and the executive one-pager.

## Dataset Overview
Synthetic dataset designed to mirror a real services firm. Five tables, ~3,000 rows total:

| Table | Rows | Purpose |
|---|---|---|
| `employees` | 50 | Staff roster, role, department |
| `projects` | 20 | Project name, client, PM, dates, budget, status |
| `tasks` | 400 | Tasks per project with assignee, due date, status |
| `time_entries` | 2,500 | Hours logged per employee per task per day |
| `project_budget_actuals` | 240 | Monthly budget vs. actual spend per project |

## Process / Approach
1. **Defined the business questions first** (status of every project, budget burn vs. % complete, at-risk projects, capacity by employee).
2. **Designed a small relational schema** so projects, tasks, time, and budgets could all be joined cleanly.
3. **Generated synthetic data** with deliberate messiness (mixed-case statuses, missing PM IDs, a few duplicate time entries) to demonstrate cleaning.
4. **Wrote SQL queries** to clean the data and produce one clean output table per business question.
5. **Built an Excel dashboard** on top of the cleaned outputs with pivots, RAG status, and a one-page executive summary.
6. **Wrote a recommendations section** in plain English for the COO.

## SQL — Table Structure (DDL)

```sql
-- 1. Employees
CREATE TABLE employees (
    employee_id     INTEGER PRIMARY KEY,
    full_name       VARCHAR(100) NOT NULL,
    role            VARCHAR(50),
    department      VARCHAR(50),
    hourly_rate     NUMERIC(8,2),
    hire_date       DATE
);

-- 2. Projects
CREATE TABLE projects (
    project_id      INTEGER PRIMARY KEY,
    project_name    VARCHAR(150) NOT NULL,
    client_name     VARCHAR(100),
    project_manager_id INTEGER REFERENCES employees(employee_id),
    start_date      DATE,
    planned_end_date DATE,
    actual_end_date  DATE,
    budget_amount   NUMERIC(12,2),
    status          VARCHAR(30)   -- 'Not Started','In Progress','On Hold','Completed','Cancelled'
);

-- 3. Tasks
CREATE TABLE tasks (
    task_id         INTEGER PRIMARY KEY,
    project_id      INTEGER REFERENCES projects(project_id),
    task_name       VARCHAR(200),
    assignee_id     INTEGER REFERENCES employees(employee_id),
    due_date        DATE,
    completed_date  DATE,
    status          VARCHAR(30),  -- 'Open','In Progress','Done','Blocked'
    estimated_hours NUMERIC(6,2)
);

-- 4. Time Entries
CREATE TABLE time_entries (
    entry_id        INTEGER PRIMARY KEY,
    employee_id     INTEGER REFERENCES employees(employee_id),
    task_id         INTEGER REFERENCES tasks(task_id),
    entry_date      DATE,
    hours_logged    NUMERIC(5,2)
);

-- 5. Project Budget Actuals (monthly)
CREATE TABLE project_budget_actuals (
    record_id       INTEGER PRIMARY KEY,
    project_id      INTEGER REFERENCES projects(project_id),
    month_start     DATE,
    budgeted_amount NUMERIC(12,2),
    actual_amount   NUMERIC(12,2)
);
```

## SQL — Sample Analysis Queries

### Q1. Clean and standardize project status values
```sql
-- Source has 'in progress', 'In Progress', 'IN-PROGRESS' all meaning the same thing.
SELECT
    project_id,
    project_name,
    CASE
        WHEN UPPER(TRIM(status)) IN ('IN PROGRESS','IN-PROGRESS','INPROGRESS') THEN 'In Progress'
        WHEN UPPER(TRIM(status)) IN ('NOT STARTED','NEW') THEN 'Not Started'
        WHEN UPPER(TRIM(status)) IN ('ON HOLD','PAUSED') THEN 'On Hold'
        WHEN UPPER(TRIM(status)) IN ('COMPLETED','DONE','CLOSED') THEN 'Completed'
        WHEN UPPER(TRIM(status)) IN ('CANCELLED','CANCELED') THEN 'Cancelled'
        ELSE 'Unknown'
    END AS clean_status
FROM projects;
```

### Q2. Project portfolio health — budget burn vs. % complete
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
    p.project_id,
    p.project_name,
    p.client_name,
    ROUND(100.0 * tp.done_tasks / NULLIF(tp.total_tasks,0), 1) AS pct_complete,
    br.total_budget,
    br.total_actual,
    ROUND(100.0 * br.total_actual / NULLIF(br.total_budget,0), 1) AS pct_budget_burned,
    CASE
        WHEN br.total_actual > br.total_budget THEN 'Over Budget'
        WHEN (100.0 * br.total_actual / NULLIF(br.total_budget,0))
             - (100.0 * tp.done_tasks  / NULLIF(tp.total_tasks,0))  > 15 THEN 'At Risk'
        ELSE 'On Track'
    END AS health_flag
FROM projects p
LEFT JOIN task_progress  tp ON tp.project_id = p.project_id
LEFT JOIN budget_rollup  br ON br.project_id = p.project_id
ORDER BY pct_budget_burned DESC NULLS LAST;
```

### Q3. Overdue tasks by project and PM
```sql
SELECT
    p.project_name,
    e.full_name AS project_manager,
    COUNT(*) AS overdue_task_count
FROM tasks t
JOIN projects  p ON p.project_id = t.project_id
JOIN employees e ON e.employee_id = p.project_manager_id
WHERE t.status <> 'Done'
  AND t.due_date < CURRENT_DATE
GROUP BY p.project_name, e.full_name
ORDER BY overdue_task_count DESC;
```

### Q4. Employee capacity — hours logged per week vs. expected 40
```sql
SELECT
    e.full_name,
    DATE_TRUNC('week', te.entry_date) AS week_start,
    SUM(te.hours_logged) AS hours_this_week,
    CASE
        WHEN SUM(te.hours_logged) > 45 THEN 'Overallocated'
        WHEN SUM(te.hours_logged) < 30 THEN 'Underutilized'
        ELSE 'OK'
    END AS capacity_flag
FROM time_entries te
JOIN employees   e  ON e.employee_id = te.employee_id
WHERE te.entry_date >= CURRENT_DATE - INTERVAL '8 weeks'
GROUP BY e.full_name, DATE_TRUNC('week', te.entry_date)
ORDER BY week_start DESC, hours_this_week DESC;
```

### Q5. Find duplicate time entries (data quality check)
```sql
SELECT
    employee_id,
    task_id,
    entry_date,
    COUNT(*) AS duplicate_count,
    SUM(hours_logged) AS total_logged
FROM time_entries
GROUP BY employee_id, task_id, entry_date
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

### Q6. Top 5 over-budget projects
```sql
SELECT
    p.project_name,
    p.client_name,
    SUM(pba.budgeted_amount) AS budget,
    SUM(pba.actual_amount)   AS actual,
    SUM(pba.actual_amount) - SUM(pba.budgeted_amount) AS overrun_dollars
FROM projects p
JOIN project_budget_actuals pba ON pba.project_id = p.project_id
GROUP BY p.project_name, p.client_name
HAVING SUM(pba.actual_amount) > SUM(pba.budgeted_amount)
ORDER BY overrun_dollars DESC
LIMIT 5;
```

### Q7. Month-over-month spend trend
```sql
SELECT
    DATE_TRUNC('month', month_start) AS month,
    SUM(budgeted_amount) AS planned_spend,
    SUM(actual_amount)   AS actual_spend,
    SUM(actual_amount) - SUM(budgeted_amount) AS variance
FROM project_budget_actuals
GROUP BY DATE_TRUNC('month', month_start)
ORDER BY month;
```

### Q8. PM scorecard — projects on time, on budget
```sql
WITH project_health AS (
    SELECT
        p.project_manager_id,
        p.project_id,
        CASE WHEN p.actual_end_date IS NULL OR p.actual_end_date <= p.planned_end_date
             THEN 1 ELSE 0 END AS on_time_flag,
        CASE WHEN SUM(pba.actual_amount) <= SUM(pba.budgeted_amount)
             THEN 1 ELSE 0 END AS on_budget_flag
    FROM projects p
    LEFT JOIN project_budget_actuals pba ON pba.project_id = p.project_id
    GROUP BY p.project_manager_id, p.project_id, p.actual_end_date, p.planned_end_date
)
SELECT
    e.full_name AS project_manager,
    COUNT(*) AS total_projects,
    SUM(on_time_flag)   AS on_time_projects,
    SUM(on_budget_flag) AS on_budget_projects,
    ROUND(100.0 * SUM(on_time_flag)   / COUNT(*), 1) AS on_time_pct,
    ROUND(100.0 * SUM(on_budget_flag) / COUNT(*), 1) AS on_budget_pct
FROM project_health ph
JOIN employees e ON e.employee_id = ph.project_manager_id
GROUP BY e.full_name
ORDER BY on_time_pct DESC;
```

## Excel — What to Build

Create one workbook, `project_tracker_dashboard.xlsx`, with these tabs:

**Tab 1 — `Data_Projects`** (paste output of Q1 + Q2 here)
- Format as an Excel Table (`Ctrl+T`) so formulas auto-extend.
- Columns: project_id, project_name, client, PM, start, planned_end, status, pct_complete, pct_budget_burned, health_flag.

**Tab 2 — `Data_Tasks`** (output of Q3)
- Format as Table.

**Tab 3 — `Data_TimeEntries`** (output of Q4)
- Format as Table.

**Tab 4 — `Data_Budget`** (output of Q6 and Q7)
- Format as Table.

**Tab 5 — `Dashboard`** — the executive view. Includes:
- **KPI cards (top row):** Total Projects, % On Track, % Over Budget, Total Hours This Week.
  - Formula example for "On Track count": `=COUNTIFS(Data_Projects[health_flag],"On Track")`
  - Formula example for "% Over Budget": `=COUNTIFS(Data_Projects[health_flag],"Over Budget")/COUNTA(Data_Projects[project_id])`
- **Pivot 1:** Projects by health flag (count) — bar chart.
- **Pivot 2:** Hours logged by employee, last 8 weeks — clustered column chart with the capacity_flag as a color cue.
- **Pivot 3:** Budget vs. Actual by month — line chart.
- **Conditional formatting on `Data_Projects[health_flag]`:** green for "On Track", yellow for "At Risk", red for "Over Budget."
- **XLOOKUP formula** on the dashboard to pull project name by selected ID:
  `=XLOOKUP(B3, Data_Projects[project_id], Data_Projects[project_name], "Not found")`
- **Slicer** tied to the project pivots so leadership can filter by PM or client.

**Tab 6 — `Exec_OnePager`** — a print-friendly summary:
- Title + week-of date.
- 4 KPI cards.
- Top 5 at-risk projects (table).
- 2 charts (budget burn, on-time %).
- 3-bullet "what changed this week" callout.

## Key Findings (sample — adjust to your generated data)
- 4 of 20 projects (20%) are flagged Over Budget; 3 more are At Risk.
- Average budget burn is 12 percentage points ahead of % complete on at-risk projects — a leading indicator of overrun.
- 2 PMs account for 70% of overdue tasks; their average open-task age is 18 days vs. portfolio median of 6.
- 6 employees logged >45 hours/week for 3+ consecutive weeks (sustainable risk).
- One client (Acme Co.) accounts for 40% of the total cost overrun — concentrated risk.

## Business Recommendations
1. **Immediate:** Re-baseline the 4 over-budget projects with the COO and adjust forecasts.
2. **Process:** Add a weekly check-in on any project where (% budget burned − % complete) > 15. Use the at-risk SQL query as the trigger.
3. **Capacity:** Redistribute work from the 6 overallocated staff before quality slips.
4. **Client:** Open a structured conversation with Acme Co. about scope changes driving the overrun.
5. **Reporting cadence:** Replace the current ad-hoc PM emails with this dashboard, refreshed every Monday at 9am.

## What This Project Demonstrates
- **Data modeling:** designed a clean relational schema from a fuzzy business problem.
- **Data cleaning:** standardized inconsistent status values; surfaced and removed duplicate time entries.
- **SQL fluency:** joins across 5 tables, CTEs, CASE logic, window-style aggregations, date functions.
- **Excel fluency:** tables, XLOOKUP, SUMIFS/COUNTIFS, pivot tables, slicers, conditional formatting, dashboard layout.
- **Business judgment:** translated query output into 5 specific recommendations a COO could act on.
- **Communication:** wrote both a technical README and a 1-page executive summary.

---

## Resume Bullets (for this project)
- Designed and built a project portfolio dashboard in Excel and SQL covering 20 projects and 50 staff, surfacing 7 at-risk projects and a $X cost-overrun pattern in a single weekly view.
- Wrote SQL queries (CTEs, joins across 5 tables, CASE logic) to standardize messy project-status data and calculate budget-burn vs. percent-complete health flags.
- Built an executive Excel dashboard (pivot tables, XLOOKUP, conditional RAG formatting, slicers) and a 1-page summary used to recommend re-baselining 4 over-budget projects.
- Identified workforce-capacity issues by analyzing 8 weeks of time entries and recommended workload redistribution for 6 overallocated staff.

## Interview Talking Points
- **"Tell me about a project."** "I built a project portfolio dashboard for a services-firm scenario — 20 projects, 50 employees, five tables in SQL. The interesting part was the at-risk logic: I flagged any project where budget burn was running more than 15 points ahead of percent complete. That surfaced three projects nobody had caught yet."
- **"Walk me through a SQL query you wrote."** "The portfolio health query joins projects, tasks, and budget actuals using two CTEs — one rolls up tasks to a percent-complete number, the other rolls up budget to actual spend, and the outer query combines them with a CASE statement that produces an On Track / At Risk / Over Budget flag."
- **"How do you handle messy data?"** "In this project, status values came in with mixed case and inconsistent terms — 'In Progress', 'in-progress', 'INPROGRESS'. I wrote a CASE statement to normalize them to a clean dimension, and I also wrote a duplicate-detection query on time entries that flagged 14 duplicate rows for the team to clean up."
- **"What was the business impact?"** "The dashboard replaces five separate PM status emails. It gives the COO a same-format view every Monday, and the at-risk logic gives a 2-3 week head start on cost overruns instead of finding them at month-end close."

## What I Learned
- The hardest part of building a "simple dashboard" is the data model underneath — getting the schema right made every query and every Excel formula easier downstream.
- A health flag is more useful than a raw number. "Over Budget" tells you what to do; "$48,213 actual vs. $45,000 budget" is a number to think about.
- Excel and SQL are stronger together than either is alone. SQL handles the heavy lifting; Excel makes it readable to leadership.

---

## Appendix — Skills Demonstration Map

| Skill area | Where it shows up |
|---|---|
| SELECT / filtering / sorting | Q1, Q3, Q5, Q6 |
| Joins (INNER, LEFT) | Q2, Q3, Q4, Q6, Q8 |
| GROUP BY / aggregations | Q3, Q4, Q5, Q6, Q7, Q8 |
| CASE statements | Q1, Q2, Q4, Q8 |
| CTEs | Q2, Q8 |
| Subqueries (in HAVING) | Q5, Q6 |
| Date functions | Q3, Q4, Q7 |
| Data cleaning | Q1, Q5 |
| Excel Tables | All Data_ tabs |
| XLOOKUP | Dashboard tab |
| SUMIFS / COUNTIFS | KPI cards |
| Pivot tables | Dashboard tab (3 pivots) |
| Conditional formatting | health_flag column, capacity_flag |
| Charts (bar, line, clustered) | Dashboard tab |
| Slicers | Dashboard tab |
| Dashboard layout | Dashboard + Exec_OnePager |
| Reporting structure | Exec_OnePager |

---

## Next Steps After This Project
1. **Build it.** Generate the synthetic data (or ask Claude to generate CSVs for the 5 tables), run the SQL, build the Excel workbook.
2. **Take screenshots** of the dashboard, the SQL query results, and the at-risk flag in action.
3. **Write the README** in your GitHub repo using the structure above. Paste this document's "Project 1" section as a starting point and personalize the voice.
4. **Turn it into a PDF** case study (2-3 pages) and pin it to LinkedIn Featured.
5. **Then** start Project 2 — the no-show analysis is the recommended next one because it shows domain range.
