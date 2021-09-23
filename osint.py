import argparse
from modules import switcher
parser = argparse.ArgumentParser(
    description='CLI para tratamento de dados de OSINT')
subparsers = parser.add_subparsers(help='teste', dest='command')

## SubParser de scan
scan = subparsers.add_parser('scan', help='init scan on spiderfoot')
scan.add_argument(
    '-U', '--URL', type=str,
    help='URL do spiderfoot para fazer os scans'
)

## SubParser de export
export = subparsers.add_parser('export',
    help='export data from spiderfoot to selected destination')
export.add_argument(
    '-p', '--path', type=str,
    help='path de onde o banco de dados se encontra, caso vazio será usado o padrão')


## SubParser de instance
instance = subparsers.add_parser(
    'instance',
    help='instancias de scan do spiderfoot'
)
instance.add_argument(
    '--add', action='store_true', help='adicionar uma nova instancia')
instance.add_argument(
    '-p', '--path', type=str, help="caminho para o arquivo de instancias"
)
instance.add_argument(
    '-N', '--name', type=str, help='Nome da instancia adicionada'
)
instance.add_argument(
    '-T', '--target', type=str, help='Target que será analisado'
)
instance.add_argument(
    '--google', action='store_true', help='planilha csv exportada do google'
)

args = parser.parse_args()

switcher.switch(args)