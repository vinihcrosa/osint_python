import sqlite3

from modules import logs

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

create_instances_table_query = """
    CREATE TABLE IF NOT EXISTS instances(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        target TEXT NOT NULL UNIQUE
    )
    """

def init():
    conn = sqlite3.connect('./database/database.sql')

    try:
        cursor = conn.cursor()
        cursor.execute(create_spiderfoot_table_query)
    except:
        logs.createLog('não foi possivel criar a tabela results', 50)

    try:
        cursor.execute(create_instances_table_query)
    except:
        logs.createLog('não foi possivel criar a tabela instances', 50)

    conn.close()