import sys
import socket

sys.path.append('../')

import common.define

BUF_SIZE = 2048

class ReptilesServerSocket():

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def setsocket(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self):
        self.sock.bind((common.define.SERVER_IP_ADDR, common.define.SERVER_PORT))

    def listen(self, num=1):
        self.sock.listen(num)

    def accept(self):
        self.conn, self.addr = self.sock.accept()

    def send(self, msg):
        totalsent = 0
        msglen = len(msg)
        while totalsent < msglen:
            sent = self.conn.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self, msglen):
        chunks = []
        bytes_recd = 0
        while bytes_recd < msglen:
            chunk = self.conn.recv(min(msglen - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

