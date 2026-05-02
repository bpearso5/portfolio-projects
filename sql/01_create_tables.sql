-- Project Portfolio Tracker — Schema
-- PostgreSQL syntax (works in BigQuery/MySQL/SQL Server with minor changes)

DROP TABLE IF EXISTS time_entries;
DROP TABLE IF EXISTS project_budget_actuals;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id     INTEGER PRIMARY KEY,
    full_name       VARCHAR(100) NOT NULL,
    role            VARCHAR(50),
    department      VARCHAR(50),
    hourly_rate     NUMERIC(8,2),
    hire_date       DATE
);

CREATE TABLE projects (
    project_id          INTEGER PRIMARY KEY,
    project_name        VARCHAR(150) NOT NULL,
    client_name         VARCHAR(100),
    project_manager_id  INTEGER,
    start_date          DATE,
    planned_end_date    DATE,
    actual_end_date     DATE,
    budget_amount       NUMERIC(12,2),
    status              VARCHAR(30)
);

CREATE TABLE tasks (
    task_id         INTEGER PRIMARY KEY,
    project_id      INTEGER REFERENCES projects(project_id),
    task_name       VARCHAR(200),
    assignee_id     INTEGER REFERENCES employees(employee_id),
    due_date        DATE,
    completed_date  DATE,
    status          VARCHAR(30),
    estimated_hours NUMERIC(6,2)
);

CREATE TABLE time_entries (
    entry_id      INTEGER PRIMARY KEY,
    employee_id   INTEGER REFERENCES employees(employee_id),
    task_id       INTEGER REFERENCES tasks(task_id),
    entry_date    DATE,
    hours_logged  NUMERIC(5,2)
);

CREATE TABLE project_budget_actuals (
    record_id        INTEGER PRIMARY KEY,
    project_id       INTEGER REFERENCES projects(project_id),
    month_start      DATE,
    budgeted_amount  NUMERIC(12,2),
    actual_amount    NUMERIC(12,2)
);
