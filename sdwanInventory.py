import argparse
from RecupererEtPartager import RecupererEtPartager

parser = argparse.ArgumentParser(
    description="Recuperer les devices SDWAN et les envoyer vers un Room webex")

parser.add_argument('vManageIP', help="l'adresse IP du vmanage")
parser.add_argument('--username', '-u',
                    help="le nom d'utilisateur du vManage", default="admin", required=False)
parser.add_argument('--password', '-pw',
                    help="le mot de passe du vManage", required=True)
parser.add_argument(
    '--port', '-p', help="le port utilise au niveau du vManage", default="8443", required=False)
parser.add_argument(
    '--room', '-r', help="l'espace de travail webex dans lequel le fichier sera partage", required=True)
parser.add_argument('--webexToken', '-wt',
                    help="le token pour l'acces a l'API webex", required=True)
parser.add_argument('--filename', '-f', help="nom du fichier contenant la liste des devices",
                    default="devices.xlsx", required=False)
args = parser.parse_args()
RecupererEtPartager(args)
