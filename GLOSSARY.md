# Glossary — terms you'll keep seeing

Plain-English meanings of words that show up constantly in tech, data work, and analyst job descriptions. Keep this open while you work and you'll absorb the vocabulary in a couple of weeks just by referring back to it.

---

## Files & folders

**File** — any document on your computer or GitHub. README.md is a file. So is a CSV.

**Folder** (= directory) — a container for files. The `images/` folder holds images. "Folder" and "directory" are the same thing — analysts say folder, engineers say directory.

**Subfolder** — a folder inside another folder. `data/raw/` means the `raw` subfolder lives inside the `data` folder.

**Path** — the full address of a file. Slashes separate folders. `sql/04_sample_inserts.sql` means "the file 04_sample_inserts.sql, which lives inside the sql folder."

**Root** (or "repo root") — the very top level of a folder structure. The first thing you see when you open the URL of a GitHub repo. Files "in the root" are not inside any subfolder.

**File tree** — the visible map of folders and files. What GitHub shows on the repo home page is a file tree.

**File extension** — the part after the dot. `.md` = Markdown, `.py` = Python, `.sql` = SQL, `.csv` = comma-separated values, `.xlsx` = Excel.

---

## GitHub specifically

**Repo** (= repository) — a project's GitHub home. One folder containing all the files for a project, plus the history of every change. github.com/bpearso5/portfolio-projects is one repo.

**Commit** — a single saved change with a short message describing what changed. Every time you click "Commit changes" in GitHub, you make one commit. Commits are like save points in a video game — you can always go back to an earlier one.

**Push** — upload your commits to GitHub so others can see them. The web UI does this automatically when you click "Commit changes." If you ever use GitHub Desktop or the command line, you'll have to push manually.

**Pull** — the opposite. Download the latest commits from GitHub to your local copy.

**Branch** — a parallel version line for changes. Most beginners use only one branch called `main`. Branches matter when teams work on the same code at the same time. Don't worry about branches yet.

**Pull request** (PR) — when you propose to merge changes from one branch into another. You won't need this until you collaborate with other people on the same repo.

**Fork** — your own copy of someone else's repo so you can make changes without affecting theirs.

**Clone** — download a complete copy of a repo to your computer.

**README** — the file that GitHub displays automatically on the repo home page. By convention it's named `README.md` (Markdown). It's the first thing a recruiter or a new contributor reads.

**Issue** — a tracked task or bug report inside a repo. Used by teams.

**Star** — a bookmark/like on a repo.

**Watching** — get notified about changes to a repo.

---

## Markdown

**Markdown** — a simple way to write formatted text using plain symbols. `# Title` becomes a big heading. `**bold**` becomes **bold**. `[link text](url)` becomes a hyperlink. README files use Markdown.

**Render** — to display Markdown as formatted text instead of as raw symbols. GitHub renders README.md automatically.

---

## Code

**Script** — a small program. `generate_data.py` is a script written in Python.

**Function** — a reusable block of code that takes inputs and produces outputs. Like a SUMIF in Excel — same idea, different syntax.

**Variable** — a name that holds a value. `OUT_DIR = "data/raw"` means the variable `OUT_DIR` is set to the text `"data/raw"`.

**Library** (= package, = module) — a bundle of pre-written code you can use. `openpyxl` is a Python library for working with Excel. `pandas` is a Python library for data analysis. You "import" a library to use it.

**Syntax** — the grammar of a programming language. SQL syntax uses words like SELECT and FROM. Python syntax uses indentation.

**Comment** — text in code that the computer ignores. Used to explain what the code does. In Python, lines starting with `#` are comments. In SQL, lines starting with `--` are comments.

**Hardcoded** — a value typed directly into the code instead of pulled from somewhere else. "The threshold is hardcoded at 15%" means someone typed 15 into the code; if you want 20%, you have to edit the code.

**Bug** — an error in code that causes wrong behavior.

**Debug** — figure out and fix a bug.

---

## Data

**Dataset** — a collection of structured data, usually one or more tables.

**Table** — rows and columns of data. Like a sheet in Excel. In SQL, "table" specifically means a database table.

**Row** (= record) — one item in a table. One employee. One project. One time entry.

**Column** (= field) — one attribute. `employee_id` is a column. `hourly_rate` is a column.

**Schema** — the structure of a database. Which tables exist, which columns, how they connect. Your `01_create_tables.sql` defines a schema.

**Relational data** — data spread across multiple tables that connect to each other via shared columns (like `employee_id` in both the employees table and the time_entries table). Excel struggles with relational data; SQL is built for it.

**Synthetic data** — fake data generated for testing or demos, not from real users. Your project uses synthetic data.

**ETL** (Extract, Transform, Load) — the process of pulling data from one place, cleaning/reshaping it, and loading it somewhere else. Analyst job descriptions love this acronym.

**Pipeline** — a series of automated steps that move and transform data from raw sources to a final report or dashboard.

**Data warehouse** — a big database designed for analysis (Snowflake, BigQuery, Redshift). Different from the operational databases that run an app.

**Dashboard** — a visual report with multiple charts and metrics on one page. Your `project_tracker_dashboard.xlsx` is a dashboard.

**KPI** (Key Performance Indicator) — a metric that matters for a business goal. "% On Track" is a KPI.

**Metric** — any measurement (revenue, hours, count of things). A KPI is a metric that's been singled out as important.

**Aggregation** — combining many rows into one summary. `SUM`, `AVG`, `COUNT` are aggregations.

---

## SQL specifically

**Query** — a single request to a database. `SELECT * FROM employees` is a query.

**SELECT** — the keyword that tells SQL "I want to see these columns."

**WHERE** — filter rows. `WHERE status = 'Done'` returns only rows where the status is Done.

**JOIN** — combine rows from two tables that share a column. `JOIN tasks ON tasks.project_id = projects.project_id` combines tasks with their projects.

**GROUP BY** — collapse rows that share a value into one row, then aggregate. `GROUP BY department` gives you one row per department.

**HAVING** — filter after a GROUP BY. (WHERE filters before grouping; HAVING filters after.)

**CTE** (Common Table Expression) — a named subquery that makes complex SQL readable. Defined with `WITH ... AS (...)`. You used two of these in Q2.

**CASE** — SQL's IF/THEN. Used to bucket values: `CASE WHEN x > 100 THEN 'High' ELSE 'Low' END`.

**NULL** — represents missing/unknown data. NOT the same as zero or empty string.

**Primary key** — the column that uniquely identifies each row in a table. `employee_id` is the primary key of the employees table.

**Foreign key** — a column in one table that references the primary key of another table, creating a relationship. `time_entries.employee_id` is a foreign key pointing back to `employees.employee_id`.

---

## Excel specifically

**Cell reference** — the address of a cell. `A1` means column A, row 1. `B2:B10` means a range of cells.

**Absolute reference** — a cell reference with `$` that doesn't change when you copy the formula. `$A$1` always points to A1 even if you drag the formula.

**Pivot table** — a tool that summarizes a big table by grouping and aggregating. Like SQL's GROUP BY but in Excel.

**Conditional formatting** — formatting that changes based on the value (red if negative, green if positive, etc.).

**Slicer** — a clickable filter for pivot tables. Lets users explore data by category.

**Named range** — a label for a range of cells, so you can write `=SUM(Sales)` instead of `=SUM(B2:B100)`.

---

## Job-description acronyms

**SaaS** — Software as a Service. A web app you pay a subscription for (Salesforce, Notion, etc.).
**API** (Application Programming Interface) — how software talks to other software. Most SaaS tools have APIs you can pull data from.
**SQL** (Structured Query Language) — the language used to query databases. Most analyst roles want this.
**BI** (Business Intelligence) — the field of turning company data into reports and dashboards. Tableau, Power BI, Looker are BI tools.
**OLAP** / **OLTP** — analytical vs. transactional databases. Don't worry about it unless asked.
**ERP** — software that runs the back office (finance, HR, supply chain). SAP, Oracle, NetSuite.
**CRM** — software for tracking customer relationships. Salesforce, HubSpot.
**Stakeholder** — anyone with an interest in the work. Your boss, the team using the report, the client.
**End user** — the person who'll actually use what you build.

---

## Things people say in meetings

**"Single source of truth"** — one definitive place for a piece of data, instead of three spreadsheets that disagree.
**"Drill down"** — click into a summary to see the underlying detail.
**"Slice and dice"** — analyze the same data multiple ways (by month, by region, by product).
**"Self-serve"** — a tool/dashboard end users can use without asking the analyst for help.
**"Ad hoc"** — one-time, custom, not from a template. "An ad hoc analysis" means "I made it just for this question."
**"Roll up"** — aggregate to a higher level. "Roll up daily numbers to monthly."
**"Source system"** — where the data originally lives (the CRM, the ERP, the database under the app).
**"Data quality"** — whether the data is accurate, complete, and consistent. Your duplicate-detection query is a data-quality check.

---

## Updating this glossary

When you hit a new term and don't know what it means, add it here. Two months from now you'll have a personalized cheat sheet that's worth more than any course.
