"""Generate 04_sample_inserts.sql — PostgreSQL INSERT statements for all 5 tables.

Paired with sql/01_create_tables.sql so the dataset can be loaded into DB Fiddle,
Supabase, or any Postgres environment by pasting two files.
"""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "raw"
OUT     = Path(__file__).parent / "sql" / "04_sample_inserts.sql"

def sql_str(s):
    """Escape a string for SQL or return NULL if empty."""
    if s is None or s == "":
        return "NULL"
    return "'" + s.replace("'", "''") + "'"

def sql_num(s):
    """Return number or NULL."""
    if s is None or s == "":
        return "NULL"
    return s

def sql_date(s):
    """Return quoted date or NULL."""
    if s is None or s == "":
        return "NULL"
    return "'" + s + "'"

def write_table(out_f, table, csv_path, columns, types):
    """types: list of 's' (str), 'n' (num), 'd' (date) matching columns order."""
    rows = list(csv.DictReader(open(csv_path)))
    out_f.write(f"\n-- {table}: {len(rows)} rows\n")
    chunk = 500   # batch INSERTs
    for i in range(0, len(rows), chunk):
        batch = rows[i:i+chunk]
        out_f.write(f"INSERT INTO {table} ({', '.join(columns)}) VALUES\n")
        values = []
        for row in batch:
            vals = []
            for col, t in zip(columns, types):
                v = row.get(col, "")
                if t == "s":
                    vals.append(sql_str(v))
                elif t == "n":
                    vals.append(sql_num(v))
                elif t == "d":
                    vals.append(sql_date(v))
            values.append("  (" + ", ".join(vals) + ")")
        out_f.write(",\n".join(values))
        out_f.write(";\n")

OUT.parent.mkdir(exist_ok=True)
with open(OUT, "w") as f:
    f.write("-- Project Portfolio Tracker — Sample data inserts\n")
    f.write("-- Run AFTER 01_create_tables.sql.\n")
    f.write("-- Generated from CSVs by generate_inserts.py.\n")

    write_table(f, "employees", DATA_DIR/"employees.csv",
                ["employee_id","full_name","role","department","hourly_rate","hire_date"],
                ["n","s","s","s","n","d"])

    write_table(f, "projects", DATA_DIR/"projects.csv",
                ["project_id","project_name","client_name","project_manager_id",
                 "start_date","planned_end_date","actual_end_date","budget_amount","status"],
                ["n","s","s","n","d","d","d","n","s"])

    write_table(f, "tasks", DATA_DIR/"tasks.csv",
                ["task_id","project_id","task_name","assignee_id",
                 "due_date","completed_date","status","estimated_hours"],
                ["n","n","s","n","d","d","s","n"])

    write_table(f, "time_entries", DATA_DIR/"time_entries.csv",
                ["entry_id","employee_id","task_id","entry_date","hours_logged"],
                ["n","n","n","d","n"])

    write_table(f, "project_budget_actuals", DATA_DIR/"project_budget_actuals.csv",
                ["record_id","project_id","month_start","budgeted_amount","actual_amount"],
                ["n","n","d","n","n"])

print(f"Wrote: {OUT}")
print(f"Size: {OUT.stat().st_size:,} bytes")
