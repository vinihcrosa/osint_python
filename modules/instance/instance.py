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
                #print("name:  ", name)
                email = contas["Email Address [Required]"][i]
                #print("email: ", email)
                database.createInstance(name, email)
