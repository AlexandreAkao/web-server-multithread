from datetime import datetime
from file_reader import FileReader
from util import CRLF
import model.http_code as http_code
import model.content_type as content_type

class Header:

    def __init__(self, config):
        self.status = config["status"]
        self.file = FileReader(config["file"])
        self.connection = config["connection"]
        self.server = config["server"]
            
    def get_status(self):
        return http_code.status().get(self.status)

    def get_content_type(self):
        ext = self.file.name.split(".")[-1]
        return content_type.get_content_type().get(ext).encode("utf-8")

    def get_content_length(self):
        file_size = self.file.length
        return f"Content-Length: {file_size}".encode("utf-8")

    def get_date(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"Date: {date}".encode("utf-8")

    def get_connection(self):
        return f"Connection: {self.connection}".encode("utf-8")

    def get_server(self):
        return f"Server: {self.server}".encode("utf-8")

    def get_headers(self):
        return CRLF().join([
            self.get_status(),
            self.get_content_type(),
            self.get_content_length(),
            self.get_date(),
            self.get_connection(),
            self.get_server(),
        ])