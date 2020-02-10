import os, sys, time
import socket
#import clientsocket.reptilesclientsocket
import monitorapp.src.clientapp.clientsocket.reptilesclientsocket

import monitorapp.src.common.define as define

SERVER_IP_ADDR = "192.168.0.10"
SERVER_PORT = 50000

class ReptilesClient():

    def __init__(self):
        pass

    def connect(self):
        #socket
        self.sock = monitorapp.src.clientapp.clientsocket.reptilesclientsocket.ReptilesClientSocket()
        self.sock.connect()
        
    def get_img_data(self):
        self.__send_header(define.HEADER_GET_IMG_DATA)
        
        self.__send_length(0)

        recv_header = self.__recv_header()
        recv_length = self.__recv_length()

        with open('./monitorapp/src/clientapp/images/image.jpg', mode='wb') as f:
            while recv_length >= 0:
                if recv_length >= define.FILE_BUF_SIZE:
                    datas = self.__recv_data(define.FILE_BUF_SIZE, False)
                    f.write(datas)
                else:
                    datas = self.__recv_data(recv_length, False)
                    f.write(datas)
                recv_length -= define.FILE_BUF_SIZE


    def __send_header(self, header):
        send_data = header.to_bytes(2, 'little')
        self.sock.send(send_data)

    def __send_length(self, length):
        send_data = length.to_bytes(4, 'little')
        self.sock.send(send_data)

    def __recv_header(self):
        header = self.sock.receive(2)
        return int.from_bytes(header, 'little')

    def __recv_length(self):
        length = self.sock.receive(4)
        return int.from_bytes(length, 'little')

    def __recv_data(self, length):
        data = self.sock.receive(length)
        return int.from_bytes(data, 'little')

    def __recv_data(self, length, from_byte=True):
        data = self.sock.receive(length)
        if from_byte:
            return int.from_bytes(data, 'little')
        else:
            return data
