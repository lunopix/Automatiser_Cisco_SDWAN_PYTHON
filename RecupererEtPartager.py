from Partager import Partager
from Recuperer import Recuperer


class RecupererEtPartager:

    devices = {}
    webexToken = ""
    roomID = ""
    filename = ""

    def __init__(self, args, auto=True):

        self.webexToken = 'Bearer '+args.webexToken
        self.filename = args.filename
        if auto:
            self.recuperer(args)
            self.share()

    def recuperer(self, args):
        recup = Recuperer()
        self.devices = recup.RecupererDevices(args)
        self.roomID = recup.RecupererRooms(self.webexToken, args.room)

    def share(self):
        Partager(self.devices, self.roomID,
                 self.webexToken, filename=self.filename)
