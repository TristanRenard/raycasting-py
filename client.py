import socket

class Client:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port

    def send(self, message):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            print('connected')
            data = message
            data = data.encode('utf-8')
            self.sock.send(data)
            print('message sent')
            self.sock.close()
            print('connection closed')

        except ConnectionRefusedError:
            print('connection failed')
            exit()
        finally:
            self.sock.close()