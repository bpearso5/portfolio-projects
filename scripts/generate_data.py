"""Generate synthetic CSVs for the Project Portfolio Tracker portfolio project.

Outputs (in data/raw/, relative to repo root):
  employees.csv             50 rows
  projects.csv              20 rows  (intentionally messy status values, 1 missing PM)
  tasks.csv                 ~454 rows
  time_entries.csv          ~1414 rows  (includes 14 duplicates)
  project_budget_actuals.csv 240 rows  (12 months x 20 projects)

Run from anywhere:
    python3 scripts/generate_data.py
"""
import csv
import os
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

ROOT = Path(__file__).parent.parent          # ..  (script lives in scripts/)
OUT_DIR = ROOT / "data" / "raw"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------- EMPLOYEES --------------------
FIRST = ["Alex","Brystal","Carlos","Dana","Eli","Fatima","Grace","Hassan","Imani","Jorge",
        "Kelly","Liam","Maya","Noah","Olivia","Priya","Quinn","Ravi","Sofia","Theo",
        "Uma","Victor","Wendy","Xavier","Yara","Zane","Aiden","Bella","Caleb","Diana",
        "Ethan","Fiona","Gavin","Hailey","Ian","Jade","Kyle","Lena","Marcus","Nina",
        "Owen","Paige","Quincy","Rachel","Sam","Tara","Umar","Vera","Will","Zoe"]
LAST = ["Smith","Johnson","Patel","Garcia","Lee","Nguyen","Brown","Khan","Davis","Martin",
        "Wilson","Anderson","Thomas","Jackson","White","Harris","Clark","Lewis","Walker","Young",
        "Allen","King","Wright","Scott","Green","Baker","Adams","Hill","Mitchell","Carter",
        "Roberts","Phillips","Evans","Turner","Diaz","Parker","Edwards","Collins","Reyes","Stewart",
        "Morris","Murphy","Cook","Rogers","Morgan","Bell","Cooper","Bailey","Cox","Howard"]

ROLES = ["Project Manager","Senior Analyst","Analyst","Consultant","Engineer",
         "Designer","Developer","Coordinator"]
DEPTS = ["Delivery","Operations","Engineering","Design","Finance","PMO"]

employees = []
for i in range(1, 51):
    fn = FIRST[i-1]
    ln = LAST[i % len(LAST)]
    role = random.choice(ROLES)
    if i <= 6:
        role = "Project Manager"
    employees.append({
        "employee_id": i,
        "full_name": f"{fn} {ln}",
        "role": role,
        "department": random.choice(DEPTS),
        "hourly_rate": round(random.uniform(45, 145), 2),
        "hire_date": (date(2018,1,1) + timedelta(days=random.randint(0, 2500))).isoformat(),
    })

with open(OUT_DIR / "employees.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=employees[0].keys())
    w.writeheader(); w.writerows(employees)

PMS = [e["employee_id"] for e in employees if e["role"] == "Project Manager"]

# -------------------- PROJECTS --------------------
CLIENTS = ["Acme Co.","Northwind Health","Globex Logistics","Initech","Umbrella Bio",
           "Soylent Foods","Wayne Industries","Stark Solutions","Hooli","Pied Piper",
           "Vandelay Imports","Cyberdyne","Tyrell Corp","Massive Dynamic","Wonka Mfg"]

PROJECT_NAMES = [
    "ERP Implementation","CRM Migration","Cloud Cost Optimization","Cybersecurity Uplift",
    "Data Warehouse Rebuild","Customer Portal Refresh","Mobile App Launch","HR Systems Consolidation",
    "Compliance Remediation","Procurement Automation","Reporting Modernization","Network Upgrade",
    "Onboarding Redesign","Inventory Visibility","Patient Scheduling Pilot","Field Service Rollout",
    "Marketing Ops Migration","Vendor Risk Program","Service Desk Re-platform","Quality Management Rollout"
]

# Messiness: status values inconsistent on purpose
STATUS_MESSY = ["in progress","In Progress","IN-PROGRESS","InProgress",
                "Not Started","NEW","On Hold","Paused","Completed","DONE","Cancelled","Canceled"]

projects = []
today = date(2026, 5, 2)
for pid in range(1, 21):
    start = today - timedelta(days=random.randint(60, 365))
    planned_end = start + timedelta(days=random.randint(120, 360))
    status_choice = random.choice(STATUS_MESSY)
    actual_end = ""
    if status_choice in ("Completed", "DONE"):
        actual_end = (planned_end + timedelta(days=random.randint(-30, 45))).isoformat()
    pm = random.choice(PMS)
    if pid == 7:
        pm = ""
    budget = random.choice([60000, 80000, 120000, 150000, 200000, 250000, 300000, 400000])
    projects.append({
        "project_id": pid,
        "project_name": PROJECT_NAMES[pid-1],
        "client_name": random.choice(CLIENTS),
        "project_manager_id": pm,
        "start_date": start.isoformat(),
        "planned_end_date": planned_end.isoformat(),
        "actual_end_date": actual_end,
        "budget_amount": budget,
        "status": status_choice,
    })

# Bias Acme Co. concentration
acme_count = sum(1 for p in projects if p["client_name"] == "Acme Co.")
if acme_count < 4:
    for i in range(4 - acme_count):
        projects[i*3]["client_name"] = "Acme Co."

with open(OUT_DIR / "projects.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=projects[0].keys())
    w.writeheader(); w.writerows(projects)

# -------------------- TASKS --------------------
TASK_VERBS = ["Draft","Review","Implement","Test","Deploy","Document","Configure","Migrate",
              "Validate","Approve","Plan","Kickoff","Train","Pilot","Hand-off"]
TASK_OBJS = ["requirements","data model","integration","reports","UAT plan","training materials",
             "rollout plan","security review","cutover","change request","stakeholder briefing",
             "vendor SOW","test cases","RACI","risk register"]

TASK_STATUSES = ["Open","In Progress","Done","Blocked"]

PROFILE_NEAR_DONE = [20, 5, 70, 5]
PROFILE_HEALTHY   = [25, 25, 45, 5]
PROFILE_BEHIND    = [40, 35, 20, 5]
PROFILE_STALLED   = [50, 25, 15, 10]

PROFILE_BY_PID = {
    2: PROFILE_NEAR_DONE, 6: PROFILE_NEAR_DONE, 10: PROFILE_NEAR_DONE,
    14: PROFILE_NEAR_DONE, 17: PROFILE_NEAR_DONE,
    5: PROFILE_HEALTHY,    7: PROFILE_HEALTHY,   8: PROFILE_HEALTHY,
    12: PROFILE_HEALTHY,   13: PROFILE_HEALTHY,  19: PROFILE_HEALTHY,
    3: PROFILE_BEHIND,     11: PROFILE_BEHIND,   16: PROFILE_BEHIND,
    18: PROFILE_BEHIND,    20: PROFILE_BEHIND,
    1: PROFILE_STALLED,    4: PROFILE_STALLED,   9: PROFILE_STALLED,
    15: PROFILE_STALLED,
}

tasks = []
tid = 1
for p in projects:
    n_tasks = random.randint(15, 30)
    p_start = date.fromisoformat(p["start_date"])
    p_end = date.fromisoformat(p["planned_end_date"])
    weights = PROFILE_BY_PID.get(int(p["project_id"]), [25, 30, 40, 5])
    for _ in range(n_tasks):
        due = p_start + timedelta(days=random.randint(7, max(8, (p_end - p_start).days)))
        status = random.choices(TASK_STATUSES, weights=weights)[0]
        completed = ""
        if status == "Done":
            completed = (due + timedelta(days=random.randint(-7, 10))).isoformat()
        tasks.append({
            "task_id": tid,
            "project_id": p["project_id"],
            "task_name": f"{random.choice(TASK_VERBS)} {random.choice(TASK_OBJS)}",
            "assignee_id": random.choice([e["employee_id"] for e in employees]),
            "due_date": due.isoformat(),
            "completed_date": completed,
            "status": status,
            "estimated_hours": random.choice([4, 8, 16, 24, 40, 60, 80]),
        })
        tid += 1

with open(OUT_DIR / "tasks.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=tasks[0].keys())
    w.writeheader(); w.writerows(tasks)

# -------------------- TIME ENTRIES --------------------
time_entries = []
eid = 1
weeks_back = 8
for week in range(weeks_back):
    week_start = today - timedelta(days=(week * 7) + today.weekday())
    for emp in employees:
        if random.random() < 0.15:
            continue
        target = random.choices([28, 35, 40, 42, 48, 52], weights=[10, 25, 30, 15, 15, 5])[0]
        n_entries = random.randint(3, 5)
        per_entry = target / n_entries
        chosen_tasks = random.sample([t["task_id"] for t in tasks], n_entries)
        for tk in chosen_tasks:
            day = week_start + timedelta(days=random.randint(0, 4))
            time_entries.append({
                "entry_id": eid,
                "employee_id": emp["employee_id"],
                "task_id": tk,
                "entry_date": day.isoformat(),
                "hours_logged": round(per_entry + random.uniform(-1.5, 1.5), 2),
            })
            eid += 1

# Inject 14 duplicate rows for the data quality demo
for _ in range(14):
    src = random.choice(time_entries)
    dup = dict(src); dup["entry_id"] = eid; eid += 1
    time_entries.append(dup)

with open(OUT_DIR / "time_entries.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=time_entries[0].keys())
    w.writeheader(); w.writerows(time_entries)

# -------------------- BUDGET ACTUALS --------------------
budget_actuals = []
rid = 1
months = []
m = date(2025, 6, 1)
for _ in range(12):
    months.append(m)
    if m.month == 12:
        m = date(m.year + 1, 1, 1)
    else:
        m = date(m.year, m.month + 1, 1)

NEAR_DONE_PIDS = {2, 6, 10, 14, 17}
HEALTHY_PIDS   = {5, 7, 8, 12, 13, 19}
BEHIND_PIDS    = {3, 11, 16, 18, 20}
OVER_PIDS      = {1, 4, 9, 15}

for p in projects:
    pid = int(p["project_id"])
    total_budget = p["budget_amount"]
    if pid in OVER_PIDS:
        target_burn_frac = random.uniform(1.10, 1.30)
    elif pid in BEHIND_PIDS:
        target_burn_frac = random.uniform(0.78, 0.92)
    elif pid in HEALTHY_PIDS:
        target_burn_frac = random.uniform(0.40, 0.55)
    elif pid in NEAR_DONE_PIDS:
        target_burn_frac = random.uniform(0.65, 0.78)
    else:
        target_burn_frac = random.uniform(0.55, 0.70)

    monthly_plan = total_budget / 12
    target_total_actual = total_budget * target_burn_frac
    monthly_weights = [random.uniform(0.6, 1.4) for _ in months]
    weight_sum = sum(monthly_weights)
    monthly_actuals = [target_total_actual * w / weight_sum for w in monthly_weights]

    for i, mo in enumerate(months):
        plan = round(monthly_plan * random.uniform(0.92, 1.08), 2)
        actual = round(monthly_actuals[i], 2)
        budget_actuals.append({
            "record_id": rid,
            "project_id": pid,
            "month_start": mo.isoformat(),
            "budgeted_amount": plan,
            "actual_amount": actual,
        })
        rid += 1

with open(OUT_DIR / "project_budget_actuals.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=budget_actuals[0].keys())
    w.writeheader(); w.writerows(budget_actuals)

print(f"employees:        {len(employees)}")
print(f"projects:         {len(projects)}")
print(f"tasks:            {len(tasks)}")
print(f"time_entries:     {len(time_entries)}")
print(f"budget_actuals:   {len(budget_actuals)}")
print(f"output dir:       {OUT_DIR}")
