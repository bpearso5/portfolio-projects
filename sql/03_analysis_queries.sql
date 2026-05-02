-- Project Portfolio Tracker — Analysis Queries
-- These are the queries referenced in the portfolio README.

-- =============================================================
-- Q1. Clean and standardize project status values
-- =============================================================
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

-- =============================================================
-- Q2. Project portfolio health — budget burn vs % complete
-- =============================================================
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
LEFT JOIN task_progress tp ON tp.project_id = p.project_id
LEFT JOIN budget_rollup br ON br.project_id = p.project_id
ORDER BY pct_budget_burned DESC NULLS LAST;

-- =============================================================
-- Q3. Overdue tasks by project and PM
-- =============================================================
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

-- =============================================================
-- Q4. Employee capacity — hours logged per week vs expected 40
-- =============================================================
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
JOIN employees e ON e.employee_id = te.employee_id
WHERE te.entry_date >= CURRENT_DATE - INTERVAL '8 weeks'
GROUP BY e.full_name, DATE_TRUNC('week', te.entry_date)
ORDER BY week_start DESC, hours_this_week DESC;

-- =============================================================
-- Q5. Find duplicate time entries (data quality check)
-- =============================================================
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

-- =============================================================
-- Q6. Top 5 over-budget projects
-- =============================================================
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

-- =============================================================
-- Q7. Month-over-month spend trend
-- =============================================================
SELECT
    DATE_TRUNC('month', month_start) AS month,
    SUM(budgeted_amount) AS planned_spend,
    SUM(actual_amount)   AS actual_spend,
    SUM(actual_amount) - SUM(budgeted_amount) AS variance
FROM project_budget_actuals
GROUP BY DATE_TRUNC('month', month_start)
ORDER BY month;

-- =============================================================
-- Q8. PM scorecard — projects on time, on budget
-- =============================================================
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
