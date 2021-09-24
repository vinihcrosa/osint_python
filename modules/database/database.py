import sqlite3
from pathlib import Path

from modules import logs
from . import create_databases

database_path = Path('./database/database.sql').resolve()

def getInstances():
    create_databases.init()
    newConn = sqlite3.connect('./database/database.sql')

    select_instances_query = """SELECT * FROM instances"""

    try:
        cursor = newConn.execute(select_instances_query)
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

    newConn.close()
    return instances

def createInstance(name, target):
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


def insertResult(result):
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
        logs.createLog('Result inserido no banco de dados, id do results -> ' + cursor.lastrowid, 20)
        conn.close()
    except:
        logs.createLog('Erro ao criar resultado no bancod e dados: ' + result, 30)