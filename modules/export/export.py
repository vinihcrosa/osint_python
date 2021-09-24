import json
import sqlite3
from modules.database import database
from modules import logs

def init(args):
    print(args)
    select_results_query = """
    SELECT * FROM tbl_scan_instance AS I 
    JOIN tbl_scan_results AS R ON R.scan_instance_id=I.guid 
    JOIN tbl_event_types AS T ON R.type=T.event"""


    conn = sqlite3.connect(args.path)
    cursor = conn.execute(select_results_query)
    rows = cursor.fetchall()
    insert_result(rows)
    conn.close()


def insert_result(results):
    for result in results:
        database.insertResult(result)
        logs.createLog('resultado enviado para banco de dados', 20)
