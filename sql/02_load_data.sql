-- Load CSVs into the schema (PostgreSQL \copy syntax).
-- Run this from psql with the data files in ../data/raw/

\copy employees             FROM 'data/raw/employees.csv'             DELIMITER ',' CSV HEADER;
\copy projects              FROM 'data/raw/projects.csv'              DELIMITER ',' CSV HEADER NULL AS '';
\copy tasks                 FROM 'data/raw/tasks.csv'                 DELIMITER ',' CSV HEADER NULL AS '';
\copy time_entries          FROM 'data/raw/time_entries.csv'          DELIMITER ',' CSV HEADER;
\copy project_budget_actuals FROM 'data/raw/project_budget_actuals.csv' DELIMITER ',' CSV HEADER;
