import pandas as pd

from modules.database import database
from modules import logs

def init(args):
    print(args)
    if args.add:
        if(args.path and args.google):
            contas = pd.read_csv(args.path)



            for i in contas.index:
                name = contas['First Name [Required]'][i] + contas['Last Name [Required]'][i]
                email = contas["Email Address [Required]"][i]
                database.createInstance(name, email)
                logs.createLog('Instance criada via google sheets', '20')

        elif (args.name and args.target):
            database.createInstance(args.name, args.target)
            logs.createLog('instancia criada de argumentos', 20)
