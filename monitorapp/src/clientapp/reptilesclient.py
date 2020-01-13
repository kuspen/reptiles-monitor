import sys
import socket
import clientsocket.reptilesclientsocket

sys.path.append('../')

import common

SERVER_IP_ADDR = "192.168.0.10"
SERVER_PORT = 50000

class ReptilesClient():

    def __init__(self):
        
        #socket
        self.socket = clientsocket.reptilesclientsocket.ReptilesClientSocket()
        self.socket.connect()
        
    def get_img_data():
        self.__send_header(common.define.HEADER_GET_IMG_DATA)
        self.__send_length(0)

        header = self.__recv_header()
        length = self.__recv_length()
        data = self.__recv_data(length)

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
