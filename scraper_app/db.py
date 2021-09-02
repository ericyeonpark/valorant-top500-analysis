import json
import os
from typing import Tuple, List, Dict

from dotenv import load_dotenv
import psycopg2

load_dotenv()
db_url = os.getenv('DB_URL')
table_name = 'val500test'


def db_action(sql_action: str):
    """ DB Setter - Performs a DB action returns None """
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(sql_action)
    conn.commit()
    curs.close()
    conn.close()


def db_query(sql_query: str) -> List[Tuple]:
    """ DB Getter - Returns query results as a list """
    conn = psycopg2.connect(db_url)
    curs = conn.cursor()
    curs.execute(sql_query)
    results = curs.fetchall()
    curs.close()
    conn.close()
    return results


def insert_data(data: List[Dict]):
    """ Insert data into the table """
    for item in data:
        db_action(f"""INSERT INTO {table_name} (
        id,
        Rank,
        Player,
        Rating,
        Winrate,
        Games,
        Average_Score,
        Head_Shot_Pct,
        Class,
        Region) 
        VALUES {json.dumps(tuple(item.values()))};""")


def load_data() -> List[Tuple]:
    """ Get all incidents stored in police_force table """
    return db_query(f"SELECT * FROM {table_name};")


def initialize_ranks_table():
    """ This only needs to be run once when setting up the DB """
    db_action(f"""CREATE TABLE IF NOT EXISTS first_test (
    id SERIAL PRIMARY KEY NOT NULL,
    Rank INT,
    Player TEXT,
    Rating FLOAT,
    Winrate FLOAT,
    Games INT,
    Average_Score INT,
    Head_Shot_Pct FLOAT,
    Class TEXT,
    Region TEXT,);""")


def reset_table():
    """ DANGER! this will delete all data in the table!!! """
    db_action(f"DROP TABLE {table_name}")
    initialize_ranks_table()
