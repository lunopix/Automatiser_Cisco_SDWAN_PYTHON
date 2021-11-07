import requests
from Authentification import Authentification
import sys


class Recuperer:

    def RecupererDevices(self, args):

        url = f"https://{args.vManageIP}:{args.port}/dataservice/device"
        auth = Authentification(args)
        jsessionID, Token = auth.main()
        header = {'Content-Type': 'application/json',
                  'Cookie': jsessionID, 'X-XSRF-TOKEN': Token}
        try:
            response = requests.get(url=url, headers=header, verify=False)
            devices = response.json()['data']

            if len(devices) == 0:
                print("Aucun Device n'a été trouvé")
                sys.exit(0)
            print('______Liste des devices recuperee_____')
            return devices
        except requests.exceptions.RequestException as err:
            print(
                f"Une erreur s est produite lors de la recuperation des infos : {err}")

    def RecupererRooms(self, token, title):

        url = "https://webexapis.com/v1/rooms"

        headers = {'Authorization': token}
        try:
            response = requests.get(url=url, headers=headers, verify=False)
            rooms = response.json()['items']

            for room in rooms:
                if(room['title'] == title):
                    print(f'______Espace de travail {title} trouve_____')
                    return room['id']

            print("l'espace de travail spécifié est intouvable")
            sys.exit(0)

        except requests.exceptions.RequestException as err:
            print(f"Impossible d'établir une connexion avec webex : {err}")
