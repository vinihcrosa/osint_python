import requests
import time

from . import database

def init(args):
    print(args)

    URL = 'http://localhost:5001/startscan'

    if args.URL:
        URL = args.URL + '/startscan'

    instances = database.getInstances()

    for instance in instances:
        request = startScan(instance['name'], instance['target'], URL)
        print(request)
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