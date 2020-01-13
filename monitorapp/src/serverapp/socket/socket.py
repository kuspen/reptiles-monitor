import socket

SERVER_IP_ADDR = '192.168.0.10'
SERVER_PORT = 50000

BUF_SIZE = 2048

class ReptilesServerSocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def setsocket(self):
        self.sock.setsocket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self):
        self.sock.bind(SERVER_IP_ADDR, SERVER_PORT)

    def listen(self, num=1):
        self.sock.listen(num)

    def send(self, msg):
        totalsent = 0
        msglen = len(msg)
        while totalsent < msglen:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self, msglen):
        chunks = []
        bytes_recd = 0
        while bytes_recd < msglen:
            chunk = self.sock.recv(min(msglen - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

