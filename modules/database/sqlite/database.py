import sqlite3
from pathlib import Path

from modules import logs

database_path = Path('./database/database.sql').resolve()

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

def get_instances():
    create_databases.init()
    new_conn = sqlite3.connect('./database/database.sql')

    select_instances_query = """SELECT * FROM instances"""

    try:
        cursor = new_conn.execute(select_instances_query)
        rows = cursor.fetchall()
        instances = []

        for row in rows:
            instance = {
                'name': row[1],
                'target': row[2]
            }
            instances.append(instance)
    except:
        logs.createLog('não foi possível selecionar as instances', 30)

    new_conn.close()
    return instances

def create_instance(name, target):
    conn = sqlite3.connect(database_path)

    create_instance_query = """
    INSERT INTO instances(name, target) 
    VALUES(?, ?)
    """

    try:
        cursor = conn.cursor()
        cursor.execute(create_instance_query, (name, target))
        conn.commit()
        logs.createLog('Instancia criada com sucesso name: {}, taget: {}'.format(name, target), 20)
        return cursor.lastrowid
    except:
        logs.createLog('Não foi possivel criar a instancia name: {}, target: {}'
                       .format(name, target), 30)


def insert_result(result):
    insert_result_query = """INSERT INTO results(name, target, status, hash,
                        type, generated, confidence, visibility,
                        risk, module, data, false_positive,
                        event, event_descr, event_raw, event_type)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""


    data = [result[1], result[2], result[6], result[8],
            result[9], result[10]*1000, result[11], result[12],
            result[13], result[14], result[15], result[16],
            result[18], result[19], result[20], result[21]]
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.execute(insert_result_query, data)
        conn.commit()
        logs.createLog('Result inserido no banco de dados, id do results -> c' + cursor.lastrowid, 20)
        conn.close()
    except:
        logs.createLog('Erro ao criar resultado no bancod e dados: ' + result, 30)