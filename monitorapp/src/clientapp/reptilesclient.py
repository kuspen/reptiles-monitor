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
        
    def get_img_data(self):
        self.__send_header(common.define.HEADER_GET_IMG_DATA)
        self.__send_length(0)

        recv_header = self.__recv_header()
        recv_length = self.__recv_length()

        print('recv_header=', recv_header)
        with open('./images/image.jpg', mode='wb') as f:
            while recv_length >= 0:
                print('recv_length=', recv_length)
                if recv_length >= common.define.FILE_BUF_SIZE:
                    datas = self.__recv_data(common.define.FILE_BUF_SIZE, False)
                    f.write(datas)
                else:
                    datas = self.__recv_data(recv_length, False)
                    f.write(datas)
                recv_length -= common.define.FILE_BUF_SIZE


    def __send_header(self, header):
        send_data = header.to_bytes(2, 'little')
        self.socket.send(send_data)

    def __send_length(self, length):
        send_data = length.to_bytes(4, 'little')
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

    def __recv_data(self, length, from_byte=True):
        data = self.socket.receive(length)
        if from_byte:
            return int.from_bytes(data, 'little')
        else:
            return data
