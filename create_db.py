"""
create_db.py — Run this ONCE to set up the sample SQLite database.
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

# ── Tables ──────────────────────────────────────────────────────────────────
cur.executescript("""
CREATE TABLE IF NOT EXISTS departments (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT NOT NULL,
    budget  REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    department_id INTEGER REFERENCES departments(id),
    role          TEXT NOT NULL,
    salary        REAL NOT NULL,
    hire_date     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
    dept_id     INTEGER REFERENCES departments(id),
    status      TEXT NOT NULL,
    budget      REAL NOT NULL,
    start_date  TEXT NOT NULL,
    end_date    TEXT
);

CREATE TABLE IF NOT EXISTS project_assignments (
    employee_id INTEGER REFERENCES employees(id),
    project_id  INTEGER REFERENCES projects(id),
    role        TEXT,
    PRIMARY KEY (employee_id, project_id)
);
""")

# ── Seed data ────────────────────────────────────────────────────────────────
cur.executemany("INSERT OR IGNORE INTO departments (id, name, budget) VALUES (?,?,?)", [
    (1, "Engineering",  1_200_000),
    (2, "Marketing",      500_000),
    (3, "Data Science",   800_000),
    (4, "HR",             300_000),
])

cur.executemany(
    "INSERT OR IGNORE INTO employees (id, name, department_id, role, salary, hire_date) VALUES (?,?,?,?,?,?)",
    [
        (1,  "Alice Johnson",   1, "Senior Engineer",     95_000, "2021-03-15"),
        (2,  "Bob Smith",       1, "Junior Engineer",     65_000, "2023-01-10"),
        (3,  "Carol White",     3, "Data Scientist",      85_000, "2022-07-01"),
        (4,  "David Brown",     2, "Marketing Manager",   75_000, "2020-11-20"),
        (5,  "Eva Martinez",    3, "ML Engineer",         90_000, "2022-09-05"),
        (6,  "Frank Lee",       4, "HR Specialist",       55_000, "2021-06-30"),
        (7,  "Grace Kim",       1, "DevOps Engineer",     88_000, "2021-09-12"),
        (8,  "Henry Wilson",    2, "Content Strategist",  60_000, "2023-03-01"),
        (9,  "Isla Patel",      3, "Data Analyst",        70_000, "2022-12-15"),
        (10, "Jack Turner",     1, "Backend Engineer",    80_000, "2020-05-22"),
    ]
)

cur.executemany(
    "INSERT OR IGNORE INTO projects (id, title, dept_id, status, budget, start_date, end_date) VALUES (?,?,?,?,?,?,?)",
    [
        (1, "API Gateway Rewrite",       1, "In Progress", 200_000, "2024-01-01", None),
        (2, "Customer Analytics Dashboard", 3, "Completed", 150_000, "2023-06-01", "2024-01-31"),
        (3, "Brand Refresh Campaign",    2, "Planning",    80_000,  "2024-03-01", None),
        (4, "ML Recommendation Engine",  3, "In Progress", 250_000, "2024-02-01", None),
        (5, "HR Onboarding Portal",      4, "Completed",   50_000,  "2023-09-01", "2024-01-15"),
    ]
)

cur.executemany(
    "INSERT OR IGNORE INTO project_assignments (employee_id, project_id, role) VALUES (?,?,?)",
    [
        (1, 1, "Tech Lead"),   (2, 1, "Developer"),  (7, 1, "DevOps"),
        (3, 2, "Analyst"),     (9, 2, "Analyst"),    (5, 4, "Lead ML"),
        (3, 4, "Data Eng"),    (4, 3, "Lead"),       (8, 3, "Content"),
        (6, 5, "Owner"),
    ]
)

conn.commit()
conn.close()
print("✅  company.db created with sample data.")
