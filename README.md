# Task 01 — Extract and Load

## Project overview
This beginner-friendly data engineering project reads sales records from a CSV file, loads them into an SQLite database table, and checks that the number of loaded rows matches the source row count.

## What the project includes
- **Extract:** Reads records from `sales_data.csv`.
- **Load:** Stores the records in the `sales` table inside `sales.db`.
- **Validation:** Compares the source row count with the database row count.
- **Repeatable execution:** The `sales` table is rebuilt each time the script runs, preventing duplicate rows when the project is run again.

## Tools used
- Python
- CSV module
- SQLite (`sqlite3`)

## Project files
- `load_data.py` — main ETL script
- `sales_data.csv` — sample source data
- `sales.db` — created automatically when the script runs

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python load_data.py
   ```

## Expected output
```text
Source rows: 8
Rows loaded into SQLite: 8
SUCCESS: Data extracted, loaded, and row count verified.
```

## Verify the database
After running the script, open `sales.db` with an SQLite database viewer and run:

```sql
SELECT COUNT(*) FROM sales;
SELECT * FROM sales;
```

The row count should be `8`.

## Design decision
A local CSV file and SQLite database were chosen to keep the project small and easy to run without API keys, cloud services, or external Python packages.
