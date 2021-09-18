import sqlite3
from pathlib import Path

database_path = Path('../database/database.sql').resolve()

def init():


    conn = sqlite3.connect('./database/database.sql')

    create_spiderfoot_table_query = """
CREATE TABLE IF NOT EXISTS results(
    guid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    target TEXT NOT NULL,
    status TEXT NOT NULL,
    hash TEXT NOT NULL,
    type TEXT NOT NULL,
    generated INTEGER NOT NULL,
    confidence TEXT NOT NULL,
    visibility TEXT NOT NULL,
    risk TEXT NOT NULL,
    module TEXT NOT NULL,
    data TEXT NOT NULL,
    false_positive TEXT NOT NULL,
    event TEXT NOT NULL,
    event_descr TEXT NOT NULL,
    event_raw TEXT NOT NULL,
    event_type TEXT NOT NULL
)
"""

    try:
        cursor = conn.cursor()
        cursor.execute(create_spiderfoot_table_query)
    except:
        print('An exception occurred')


    create_instances_table_query = """
    CREATE TABLE IF NOT EXISTS instances(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        target TEXT NOT NULL UNIQUE
    )
    """

    cursor.execute(create_instances_table_query)

    conn.close()

def getInstances():
    init()
    newConn = sqlite3.connect('./database/database.sql')

    select_instances_query = """SELECT * FROM instances"""

    cursor = newConn.execute(select_instances_query)

    rows = cursor.fetchall()

    instances = []

    for row in rows:
        instance = {
            'name': row[1],
            'target': row[2]
        }
        instances.append(instance)

    newConn.close()
    return instances