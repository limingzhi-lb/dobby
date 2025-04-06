import socket
from wifi import connect_wifi


class SocketServer(object):

    def __init__(self):
        connect_wifi()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', 80))
        self.socket.listen(5)

    def listen(self):
        conn, addr = self.socket.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        return request, conn

    def send_response(self, conn, response):
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()


current_socket = SocketServer()
