import os
import io
import uuid
import pandas as pd
from db_connect import get_pg_conn, get_sf_conn

# ---------- CONFIG ----------
def load_sql(file_path):
    with open(file_path, "r") as f:
        return f.read()

SNOWFLAKE_SQL = load_sql("sql\\exploration\\gold_movement_per_run.sql")


# ---------- LOAD ----------
def load_to_postgres(pg_conn, df):
    if df.empty:
        print("No data returned")
        return

    df = df.copy()

    df.insert(0, "load_batch_id", str(uuid.uuid4()))

    # rename columns to match table
    # df.columns = [
    #     "load_batch_id",
    #     "order_number",
    #     "material_number",
    #     "material_description",
    #     "work_center",
    #     "posting_date",
    #     "day_yield",
    #     "day_scrap",
    #     "gold_issued_261",
    #     "gold_issued_reversal_262",
    #     "gold_byproduct_531",
    #     "gold_byproduct_reversal_532",
    #     "entries"
    # ]

    buffer = io.StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    copy_sql = """
    COPY raw.gold_movement (
        load_batch_id,
        order_number,
        material_number,
        material_description,
        work_center,
        posting_date,
        day_yield,
        day_scrap,
        gold_issued_261,
        gold_issued_reversal_262,
        gold_byproduct_531,
        gold_byproduct_reversal_532,
        entries
    )
    FROM STDIN WITH CSV
    """

    with pg_conn.cursor() as cur:
        with cur.copy(copy_sql) as copy:
            copy.write(buffer.read())

    pg_conn.commit()
    print(f"Loaded {len(df)} rows")

# ---------- MAIN ----------
def main():
    # connect
    sf = get_sf_conn()
    pg = get_pg_conn()

    try:
        df = pd.read_sql(SNOWFLAKE_SQL, sf)

        print(f"Extracted {len(df)} rows")

        load_to_postgres(pg, df)

    finally:
        sf.close()
        pg.close()

if __name__ == "__main__":
    main()