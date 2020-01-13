import sys
import serversocket.reptilesserversocket
import devices.camera.reptilescamera

sys.path.append('../')
import common

# header 2[byte], length 4[byte], data length[byte]

class ReptilesServer():

    def __init__(self):

        # socket
        self.socket = ReptilesServerSocket()
        self.socket.setsocket()
        self.socket.bind()
        self.socket.listen()

        # camera
        self.camera = Camera()

    def loop(self):

        while True:
            header = __recv_header()
            length = __recv_length()
            data = __recv_data(length)
            
            if header == common.define.HEADER_GET_IMG_DATA:

                __send_header(common.define.HEADER_ACK)
                __send_length()


    def __get_img_data(self, data):
        camera.capture()


    def __send_header(self, header):
        send_data = header.to_bytes(2, 'little')
        self.socket.send(send_data)

    def __send_length(self, length):
        send_data = header.to_bytes(4, 'little')
        self.socket.send(send_data)

    def __recv_header(self):
        header = self.socket.receive(2)
        return int.from_bytes(header, 'little')

    def __recv_length(self):
        length = self.socket.receive(4)
        return int.from_bytes(length, 'little')

    def __recv_data(self, length):
        data = self.socket.receive(length)
        return int.from_bytes(data, 'little')

