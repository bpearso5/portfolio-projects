# Portfolio Strategy

These are my notes on the strategy behind this Excel + SQL portfolio as I move into Project Analyst, Business Analyst, Operations Analyst, and Project Coordinator roles. I built this document before I built Project 1 because I didn't want to put 40+ hours into the wrong project for the wrong audience. I'm sharing it publicly because the reasoning matters as much as the work.

---

## Executive Summary

I'm building a 3 to 5 project portfolio focused on practical business analysis — the kind of work I'd actually do as a Project Analyst, BA, or Ops Analyst. Project 1 (Project Portfolio Tracker) is built and lives in this repo. Project 2 (Patient No-Show Analysis) is queued up for healthcare domain range. Each project is reproducible from a single command, has real screenshots in the README, and ends in business recommendations a manager could act on.

The standard I'm holding myself to: would a manager trust me to own this weekly report or clean up this tracker without supervision? That's the bar.

---

## Portfolio Philosophy

For the roles I'm targeting, I don't need to prove I can write the most advanced SQL on the internet. I need to prove I can take messy operational data, clean it, analyze it, explain it, and turn it into a decision-ready view.

The three things I think hiring managers actually look for:

1. **Can I clean and structure messy real-world data?** Cleaning, joining, standardizing — that's most of the actual work.
2. **Can I tie a query or a chart to a business decision?** "The no-show rate is highest on Mondays, so we recommend X" beats a SELECT statement floating in space.
3. **Can I communicate the work to someone who doesn't speak SQL?** Plain-English summaries first, technical depth second.

What I'm avoiding: ten chart types on one dashboard with no story, generic Kaggle datasets, "made a dashboard with KPIs" framing, and buzzwords like "synergy" or "leveraged data-driven insights."

---

## Project 1 (Built) — Project Portfolio Tracker

A weekly executive dashboard for a 50-person services firm running 20 active client projects. Replaces five separate PM status emails with a single view of project health, budget burn, overdue work, and team capacity.

**Headline numbers from the build:**

- 20 projects across 5 tables (~3,000 rows total)
- 11 On Track (55%), 5 At Risk (25%), 4 Over Budget (20%)
- $95,524 total cost overrun, concentrated in 4 projects
- 245 overdue tasks
- 10 employees overallocated for ≥3 of the last 8 weeks
- 14 duplicate time entries surfaced via SQL data-quality check

**For the full project walkthrough with screenshots,** see [README.md](README.md).

### Why I picked this one first

Three reasons. It mirrors my work history directly, so I can talk about it from real experience, not theory. Every hiring manager I want to talk to recognizes the shape of the problem instantly — no setup needed. And the scope let me use *every* core Excel and SQL skill in a single piece of work, which means one well-built project does the work of three thinner ones.

---

## Project Roadmap

| Project | Domain | Skill focus | Status |
|---|---|---|---|
| Project Portfolio Tracker | PMO / Operations | SQL joins, Excel dashboard, status reporting | **Built first** |
| Patient No-Show Analysis | Healthcare | Segmentation, no-show rates, recommendations | **Planned next** |
| Departmental Budget vs. Actual | Finance / Ops | Variance analysis, forecasting | Future |
| Employee Training & Compliance | HR / Compliance | Overdue flags, audit readiness | Future |
| Customer Service Ticket Analysis | Operations | SLA tracking, bottleneck analysis | Future |
| Inventory & Reorder Analysis | Retail / Supply Chain | Reorder logic, ABC analysis | Future |
| Hiring Pipeline Funnel | Recruiting | Conversion rates, time-in-stage | Future |

### My top 3

1. **Project Portfolio Tracker** — strongest match for my project management background; built first.
2. **Patient No-Show Analysis** — adds healthcare domain range and gives me a "we recommended X intervention" story.
3. **Departmental Budget vs. Actual Tracker** — shows I can speak the language of finance and leadership.

---

## Design Choices and Lessons from Project 1

### Why these five tables

I started with the business questions, not the data. The questions were: which projects are healthy, which are at risk, which are over budget, who's overworked, and is there a data-quality problem hiding under any of it. I worked backwards to the tables I'd need: `projects`, `tasks` (for % complete), `time_entries` (for capacity), `employees` (for names), `project_budget_actuals` (for % burned). Five tables with real foreign keys — enough to demo joins without being overwhelming.

### The health flag was the most important design choice

A raw number — "actual is $48,213 vs. budget $45,000" — is a number. A label — "Over Budget" — tells you what to do. So the headline query produces a three-way flag:

- `Over Budget` if total actual > total budget
- `At Risk` if (% budget burned) − (% complete) > 15 percentage points
- `On Track` otherwise

The 15-point threshold was the most arbitrary part. I picked it because it produces a useful distribution on this dataset. In a real engagement I'd defend it by tying it to historical data ("projects that crossed 15 points in our archive ended up overrun 70% of the time"). For a synthetic-data portfolio piece, "this is a tunable parameter and here's why I picked the value I did" is the answer I'd give in an interview.

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

The two CTEs handle each rollup separately. Without them, the SELECT would have nested aggregations and become hard to read. The `NULLIF` guards protect against divide-by-zero. The `LEFT JOIN`s mean even projects without tasks or budget records still appear in the result.

### Lessons learned for the next project

- **Plan the screenshots before building.** I built the workbook, then realized I needed to take screenshots, then realized two of them looked confusing without a caption. Next time I'll think about the README story first and let that drive what the dashboard needs to show.
- **Write the SQL inserts script earlier.** I built the dataset using Python and CSVs, which is great for openpyxl but not for sharing the data with someone running queries online. I added `generate_inserts.py` late. Next project I'll plan for "anyone should be able to load this dataset into DB Fiddle in 30 seconds" from the start.
- **Don't over-engineer the data quality demo.** I planted exactly 14 duplicates — a perfect number for the screenshot but slightly artificial-looking. Next time I'd plant an uneven distribution (7 from one source, 3 from another, 2 from a third) so the data-quality query tells a richer story.

For my interview-prep prompts and resume-bullet drafts, see [`interview_practice_prompt.md`](interview_practice_prompt.md).

---

## Repo Structure

This repo is organized so a reviewer can open the Excel workbook first, then inspect the SQL, data, scripts, and documentation if they want more detail.

```
portfolio-projects/
├── README.md                          ← project write-up + screenshots
├── project_tracker_dashboard.xlsx     ← the finished Excel workbook
├── PORTFOLIO_STRATEGY.md              ← this file
├── GLOSSARY.md                        ← terms I'm learning as I go
├── interview_practice_prompt.md       ← coach prompt for Claude.ai
├── data/raw/                          ← five synthetic CSVs
├── sql/                               ← schema + 8 analysis queries + INSERT script
├── scripts/                           ← Python: data generator, workbook builder, inserts
└── images/                            ← dashboard and SQL screenshots
```

The .xlsx lives at the root because it's the headline deliverable — anyone clicking "open this first" should see it without hunting. The Python scripts live in `scripts/` because they're tooling, not the work itself. The whole project rebuilds with two commands: `python3 scripts/generate_data.py` then `python3 scripts/build_workbook.py`.

---

## Project Documentation Template

Every project README in this portfolio follows the same nine-section structure:

1. Business question or problem (2-3 sentences, plain English)
2. How to review this project (where to look first)
3. Headline numbers (the 5-bullet "what this build shows")
4. The Excel work (with screenshots)
5. The SQL work (with screenshots)
6. Business recommendations (what I'd tell the manager)
7. What's in this folder (file map)
8. To regenerate from scratch (the commands)
9. What this project demonstrates (skills mapped to the work)

Same headings, same flow, every time. Reviewers who skim two of my projects shouldn't have to relearn how to read them.

---

## Portfolio Readiness Checklist

Before I publish a project to this repo, it has to clear all of these:

- [ ] Clear business question stated up front
- [ ] README with at least three rendered screenshots
- [ ] Dataset documented (synthetic or real, row counts, source)
- [ ] SQL files with commented queries
- [ ] Excel workbook (or other deliverable) committed
- [ ] Business recommendations written like a manager would write them
- [ ] Two commands rebuild the whole project
- [ ] Resume bullet drafted
- [ ] Five interview answers prepared and rehearsed

---

## What I'm Doing Next

1. **Project 2: Patient Appointment & No-Show Analysis.** Different domain (healthcare), same depth as Project 1. Queued up.
2. **A 1-page PDF case study from Project 1** to pin to LinkedIn Featured.
3. **Resume + LinkedIn updates** with a link back to this repo.
4. **Interview prep practice** — running through the prompt in `interview_practice_prompt.md` until I can answer each mode in under 90 seconds without notes.
