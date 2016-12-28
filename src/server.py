from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import pickle
from command import Command
from status import Status
from messages import GpioCommand
'8000'


class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        print self.data
        com = pickle.loads(self.data)
        print com
        self.sendMessage(self.data)

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()
