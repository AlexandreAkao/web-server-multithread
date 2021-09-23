import socket
from threading import Thread
from response_controller import ResposeController

class WebServer:

    def __init__(self, address='0.0.0.0', port=6789):
        self.port = port
        self.address = address

    def start(self):
        print(f"🚀 Server running in http://localhost:{self.port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.address, self.port))
            s.listen(10)

            while True:
                print('Waiting connections...')
                conn, addr = s.accept()
                req = HttpRequest(conn, addr)
                req.start()


class HttpRequest(Thread):

    def __init__(self, conn, addr):
        super(HttpRequest, self).__init__()
        self.conn = conn
        self.addr = addr
        self.CRLF = '\r\n'
        self.buffer_size = 4096
        self.handler = ResposeController()

    def run(self):
        request = self.conn.recv(self.buffer_size)
        # print(request)
        endpoint = self.handler.get_endpoint(request)
        print(endpoint)
        response = HttpResponse(self.conn, self.addr, endpoint)
        response.process_response()

        self.conn.close()


class HttpResponse:

    def __init__(self, conn, addr, file):
        self.conn = conn
        self.addr = addr
        self.file = file
        self.handler = ResposeController()

    def process_response(self):
        response = self.handler.get_response(self.file)
        self.conn.sendall(response)