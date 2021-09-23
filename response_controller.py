from header import Header
from util import CRLF, existsFile
from file_reader import FileReader

class ResposeController:
    def get_endpoint(self, request):
        requestInfo = str(request)
        if "GET" in requestInfo and "HTTP" in requestInfo:
            path = requestInfo.split(" ")[1].strip("/")
            return path
        return None

    def get_response(self, filename, status = 200):
        if not existsFile(filename):
            status = 404
            filename = "404.html"

        file = FileReader(filename)
        header_response = Header({
            "status": status,
            "file": filename,
            "connection": "close",
            "server": "UNIFOR/1.0 socket/1.0"
        })
        return CRLF().join([
            header_response.get_headers(),
            b'',
            file.data
        ])
