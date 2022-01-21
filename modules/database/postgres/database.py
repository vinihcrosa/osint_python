import psycopg2
import os

from dotenv import load_config, find_dotenv

from modules import logs

DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_HOST = os.environ['DB_HOST']
DB_DATABASE = os.environ['DB_DATABASE']


def create_table():
    create_table_instance_query = """
    CREATE TABLE IF NOT EXISTS instance(
	    id serial PRIMARY KEY,
	    name varchar(50) NOT NULL,
  	  target varchar(50) NOT NULL UNIQUE
    )
  """

    con = psycopg2.connect(
        host=DB_HOST,
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASS
    )

    print(DB_DATABASE, DB_HOST, DB_PASS, DB_USER)

    con.close()
