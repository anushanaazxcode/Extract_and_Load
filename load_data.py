import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "sales_data.csv"
DB_FILE = BASE_DIR / "sales.db"


def extract_data():
    """Read records from the source CSV file."""
    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def load_data(rows):
    """Create the table and load the CSV records into SQLite."""
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        # Rebuild the table on each run so repeated runs do not create duplicates.
        cursor.execute("DROP TABLE IF EXISTS sales")
        cursor.execute("""
            CREATE TABLE sales (
                order_id INTEGER PRIMARY KEY,
                product TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL
            )
        """)

        cursor.executemany("""
            INSERT INTO sales (order_id, product, category, quantity, unit_price)
            VALUES (?, ?, ?, ?, ?)
        """, [
            (
                int(row["order_id"]),
                row["product"],
                row["category"],
                int(row["quantity"]),
                float(row["unit_price"])
            )
            for row in rows
        ])

        cursor.execute("SELECT COUNT(*) FROM sales")
        loaded_count = cursor.fetchone()[0]

    return loaded_count


def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Source file not found: {CSV_FILE}")

    rows = extract_data()
    loaded_count = load_data(rows)

    print(f"Source rows: {len(rows)}")
    print(f"Rows loaded into SQLite: {loaded_count}")

    if loaded_count != len(rows):
        raise RuntimeError("Row count check failed!")

    print("SUCCESS: Data extracted, loaded, and row count verified.")


if __name__ == "__main__":
    main()
