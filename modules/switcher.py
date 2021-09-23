from modules.export import export
from modules.scan import scan
from modules.instance import instance

def switch(args):
    if args.command == 'scan':
        scan.init(args)
    elif args.command =='export':
        export.init(args)
    elif args.command =='instance':
        instance.init(args)