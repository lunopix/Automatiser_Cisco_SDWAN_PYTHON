import requests
import sys


class Authentification:
    username = ""
    password = ""
    port = ""
    vManageIP = ""

    def __init__(self, args):
        self.username = args.username
        self.password = args.password
        self.port = args.port
        self.vManageIP = args.vManageIP

    def main(self):
        JsessionID = self.Recuperer_JSessionID()
        Token = self.Recuperer_Token(JsessionID)
        if JsessionID and Token:
            print('______Authentification reussie_____')
            return (JsessionID, Token)

    def Recuperer_JSessionID(self):

        url = f"https://{self.vManageIP}:{self.port}/j_security_check"
        payload = {'j_username': self.username, 'j_password': self.password}

        try:
            response = requests.post(url=url, data=payload, verify=False)
            if response.headers['Set-Cookie']:
                return response.headers['Set-Cookie'].split(';')[0]
            else:
                print("L'authentification a echoué, veuillez vérifier vos identifiants")
                sys.exit(0)
        except requests.exceptions.RequestException as err:
            print(
                f"l'erreur suivante empeche l'exécution du programme : {err}")

    def Recuperer_Token(self, jsessionID):

        url = f"https://{self.vManageIP}:{self.port}/dataservice/client/token"
        headers = {'Cookie': jsessionID}

        try:
            response = requests.get(url=url, headers=headers, verify=False)
            if(response.status_code == 200):
                return response.text
            else:
                print("Le cookie est invalide, veuillez réessayer")
                sys.exit(0)

        except requests.exceptions.RequestException as err:
            print(
                f"l'erreur suivante empeche l'exécution du programme : {err}")
