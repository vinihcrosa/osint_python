import argparse
import modules.scan
import modules.export

parser = argparse.ArgumentParser(
    description='CLI para tratamento de dados de OSINT')
subparsers = parser.add_subparsers(help='teste', dest='command')

scan = subparsers.add_parser('scan', help='init scan on spiderfoot')
scan.add_argument(
    '-U', '--URL', type=str,
    help='URL do spiderfoot para fazer os scans'
)

export = subparsers.add_parser('export',
    help='export data from spiderfoot to selected destination')
export.add_argument(
    '-p', '--path', type=str,
    help='path de onde o banco de dados se encontra, caso vazio será usado o padrão')

instance = subparsers.add_parser(
    'instance',
    help='instancias de scan do spiderfoot'
)
instance.add_argument(
    '--add', action='store_true', help='adicionar uma nova instancia')

args = parser.parse_args()

if args.command == 'scan':
    modules.scan.init(args)
elif args.command == 'export':
    modules.export.init(args)
