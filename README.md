# Project Portfolio Tracker — Excel + SQL Portfolio Project

A dashboard that surfaces project health, budget overruns, and team capacity from a relational dataset. Built on synthetic data for a 50-person services firm running 20 active client projects.

## Headline numbers in this build
- **20 projects** tracked across **5 tables** (~3,000 rows total).
- **11 On Track** (55%), **5 At Risk** (25%), **4 Over Budget** (20%).
- **$95,524** total cost overrun, concentrated in 4 projects.
- **245** overdue tasks across the portfolio.
- **10 employees** overallocated for ≥3 of the last 8 weeks.

## What's in this folder

| File | What it is |
|---|---|
| `project_tracker_dashboard.xlsx` | The finished workbook. Open this first. |
| `Excel_SQL_Portfolio_Guide.md` | Full strategy doc + 7 project ideas + write-up template + Project 1 walkthrough. |
| `generate_data.py` | Generates the 5 synthetic CSVs. Reproducible (seed=42). |
| `build_workbook.py` | Builds the Excel workbook from the CSVs. |
| `data/raw/employees.csv` | 50 employees |
| `data/raw/projects.csv` | 20 projects with intentionally messy status values |
| `data/raw/tasks.csv` | 454 tasks |
| `data/raw/time_entries.csv` | 1,414 time entries (includes 14 duplicates for the data-quality demo) |
| `data/raw/project_budget_actuals.csv` | 240 monthly budget vs. actual records |
| `sql/01_create_tables.sql` | Schema (PostgreSQL syntax) |
| `sql/02_load_data.sql` | `\copy` commands to load the CSVs |
| `sql/03_analysis_queries.sql` | 8 analysis queries: cleaning, health flags, overdue, capacity, duplicates, top-5 overrun, monthly trend, PM scorecard |

## Workbook tabs
- **README** — what's in the workbook and how to refresh it
- **Dashboard** — KPI cards, project health summary + bar chart, top-5 over-budget table, monthly planned-vs-actual line chart, capacity hot list
- **Exec_OnePager** — print-friendly 1-page summary
- **Data_Projects** — cleaned project list with formula columns for `pct_complete`, `pct_budget_burned`, `health_flag`, `overrun`, with conditional formatting on the health flag
- **Data_Tasks** — task-level data with `overdue_flag`
- **Data_TimeEntries_Wk** — weekly hours per employee with `capacity_flag`
- **Data_Budget** — monthly budget vs. actual with variance and a color-scale on variance

## To regenerate everything from scratch
```bash
python3 generate_data.py     # rebuilds the 5 CSVs
python3 build_workbook.py    # rebuilds the .xlsx
```

## What this project demonstrates

**SQL:** joins across 5 tables, CTEs, CASE for status normalization and health flags, GROUP BY aggregations, date functions, duplicate detection.

**Excel:** Tables, XLOOKUP/INDEX-MATCH, COUNTIFS/SUMIFS, IFERROR, LARGE for ranking, conditional formatting (cell-value rules + color scales), bar and line charts, KPI cards, dashboard layout, print-ready exec summary.

**Business judgment:** translates query output into a recommendation a COO could act on this week.

## Suggested next steps
1. Open `project_tracker_dashboard.xlsx` and click through each tab.
2. Take 4-5 screenshots: Dashboard top, Exec_OnePager, the conditional-formatted health flag column on Data_Projects, the overdue flags on Data_Tasks, the variance color scale on Data_Budget. Save them in an `images/` folder.
3. Copy the Project 1 section of `Excel_SQL_Portfolio_Guide.md` into a GitHub README and personalize the voice.
4. Pin a 1-page PDF of `Exec_OnePager` to LinkedIn Featured.
5. When ready, build Project 2 (Patient Appointment & No-Show Analysis).
