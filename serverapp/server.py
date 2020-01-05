import socket.ReptilesSocket

# header 2[byte], length 4[byte], data length[byte]

__HEADER_GET_IMG_DATA = 0x1000

class ReptilesServer:

    def __init__(self):
        self.socket = ReptilesSocket()

    def connect(self):
        self.socket.connect()

    def get_img_data(self):
        header = __recv_header()
        length = __recv_length()
        data = __recv_data(length)

        __send_header(__HEADER_GET_IMG_DATA)
        __send_length()

    def __send_header(header):
        send_data = header.to_bytes(2, 'little')
        self.socket(send_data)

    def __send_length(length):
        send_data = header.to_bytes(4, 'little')
        self.socket(send_data)

    def __recv_header():
        header = self.socket(2)
        return int.from_bytes(header, 'little')

    def __recv_length():
        length = self.socket(4)
        return int.from_bytes(length, 'little')

    def __recv_data(length):
        data = self.socket(length)
        return int.from_bytes(data, 'little')

