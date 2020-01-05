import socket.ReptilesSocket

# header 2[byte], length 4[byte], data length[byte]

HEADER_GET_IMG_DATA = 0x1000

class ReptilesServer:

    def __init__(self):
        self.socket = ReptilesSocket()

    def connect(self):
        self.socket.connect()

    def run(self):
        pass

#    def getImgData(self):
#        self.socket.send(HEADER_GET_IMG_DATA.to_bytes)



