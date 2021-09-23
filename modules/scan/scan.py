import requests
import time

from modules import logs
from modules import database

def init(args):
    URL = 'http://localhost:5001/startscan'

    if args.URL:
        URL = args.URL + '/startscan'

    instances = database.getInstances()

    for instance in instances:
        request = startScan(instance['name'], instance['target'], URL)
        if request.status_code == 200:
            logs.createLog(
                'Scan iniciado name: ' + instance['name'] + " - target: " + instance['target'],
                20
            )
        else:
            logs.createLog(
                'Erro ao iciar scan name: '+ instance['name'] + " - target: " + instance['target'],
                40
            )
        time.sleep(3)

    return 0

def startScan(name=str, target=str, URL=str):
    body = {
        "scanname": name,
        "scantarget": target,
        "usecase": "all",
        "modulelist": "",
        "typelist": ""
    }
    request = requests.post(
        URL,
        data=body)
    
    return request