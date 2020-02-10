import os
import sys
import serversocket.reptilesserversocket
import devices.camera.reptilescamera

sys.path.append('../')
import common

# header 2[byte], length 4[byte], data length[byte]

class ReptilesServer():

    def __init__(self):

        # socket
        self.socket = serversocket.reptilesserversocket.ReptilesServerSocket()
        self.socket.setsocket()
        self.socket.bind()
        self.socket.listen()

        # camera
        self.camera = devices.camera.reptilescamera.ReptilesCamera()

    def loop(self):

        while True:
            self.socket.accept()
            
            header = self.__recv_header()
            length = self.__recv_length()
            data = self.__recv_data(length)

            print('header=', header)
            print('length=', length)
            print('data=', data)
            
            if header == common.define.HEADER_GET_IMG_DATA:
                print('HEADER_GET_IMG_DATA')
                self.__get_img_data()

                self.__send_header(common.define.HEADER_ACK)
                img_size = os.path.getsize('./images/image.jpg')
                self.__send_length(img_size)
                print(img_size)

                with open('./images/image.jpg', mode='rb') as f:
                    while img_size >= 0:
                        if img_size >= common.define.FILE_BUF_SIZE:
                            datas = f.read(common.define.FILE_BUF_SIZE)
                            self.__send_data(datas, False)
                        else:
                            datas = f.read(img_size)
                            self.__send_data(datas, False)
                        img_size -= common.define.FILE_BUF_SIZE


    def __get_img_data(self):
        self.camera.capture()

    def __send_header(self, header):
        send_data = header.to_bytes(2, 'little')
        self.socket.send(send_data)

    def __send_length(self, length):
        send_data = length.to_bytes(4, 'little')
        self.socket.send(send_data)

    def __send_data(self, data, to_byte=True):
        if to_byte:
            send_data = data.to_bytes(length, 'little')
            self.socket.send(send_data)
        else:
            self.socket.send(data)

    def __recv_header(self):
        header = self.socket.receive(2)
        return int.from_bytes(header, 'little')

    def __recv_length(self):
        length = self.socket.receive(4)
        return int.from_bytes(length, 'little')

    def __recv_data(self, length, from_byte=True):
        data = self.socket.receive(length)
        if from_byte:
            return int.from_bytes(data, 'little')
        else:
            return data
