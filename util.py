import os

def CRLF():
  return "\r\n".encode("utf-8")

def existsFile(filename):
  return os.path.isfile(f'web/{filename}')