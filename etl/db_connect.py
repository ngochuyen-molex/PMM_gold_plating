import snowflake.connector
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
def get_pg_conn():
    try:
        conn = psycopg.connect(
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT"),
            dbname=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD")
        )
        print("✅ PostgreSQL connected")
        return conn
    except Exception as e:
        print("❌ PostgreSQL connection failed")
        raise e


def get_sf_conn():
    try:
        conn = snowflake.connector.connect(connection_name="default")
        print("✅ Snowflake connected")
        return conn
    except Exception as e:
        print("❌ Snowflake connection failed")
        raise RuntimeError(
             "Failed to connect to Snowflake using the local connections.toml profile "
            "'default'. Check that your Snowflake connector supports connection_name "
            "and that your local Snowflake config is set up correctly."
      ) from e

if __name__ == "__main__":
    get_pg_conn()
    get_sf_conn()
