import os
import streamlit as st
import snowflake.connector
from snowflake.snowpark.context import get_active_session
from dotenv import load_dotenv

def get_session():
    try:
        return get_active_session()
    except Exception:
        load_dotenv()

        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER").strip(),
            password=os.getenv("SNOWFLAKE_PAT").strip(),
            account=os.getenv("SNOWFLAKE_ACCOUNT").strip(),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE").strip(),
            database=os.getenv("SNOWFLAKE_DATABASE").strip(),
            schema=os.getenv("SNOWFLAKE_SCHEMA").strip()
        )

        return conn
    
session = get_session()

def main():
    return st.write("hello world")

if __name__ == "__main__":
    main()
