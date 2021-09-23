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