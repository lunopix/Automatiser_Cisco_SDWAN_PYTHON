import requests
import xlsxwriter
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Partager:
    fileName = ""
    devices = {}
    roomID = ""
    webexToken = ""

    def __init__(self, devices, roomID, webexToken, filename="devices.xlsx", auto=True):
        self.devices = devices
        self.roomID = roomID
        self.webexToken = webexToken
        self.fileName = filename
        if auto:
            self.CreerFichier()
            self.UploadTowebex()

    def CreerFichier(self):
        workbook = xlsxwriter.Workbook(self.fileName)
        worksheet = workbook.add_worksheet()
        ligne = 0
        premiereLigne = ["system-ip", "site-id",
                         "device-model", "status", "board-serial"]
        for colonne, attribut in enumerate(premiereLigne):
            worksheet.write(ligne, colonne,  attribut)

        ligne = 1
        for device in self.devices:
            for colonne, attribut in enumerate(premiereLigne):
                worksheet.write(ligne, colonne, device[attribut])
            ligne += 1
        workbook.close()
        print(f'______fichier {self.fileName} cree_____')

    def UploadTowebex(self):

        url = "https://webexapis.com/v1/messages"

        donnees = MultipartEncoder(
            {
                'roomId': self.roomID,
                'text': 'Ci-joint la liste des devices SDWAN',
                'files': (
                    self.fileName,
                    open(self.fileName, 'rb'),
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
            }
        )

        headers = {'Authorization': self.webexToken,
                   'Content-Type': donnees.content_type}

        try:
            requests.post(url, data=donnees, headers=headers)
            print('______Partage des informations reussies_____')

        except requests.exceptions.RequestException as err:
            print(
                f"la partage du fichier dans l'espace de travail webex a échoué : {err}")
