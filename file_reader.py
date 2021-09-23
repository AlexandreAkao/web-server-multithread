class FileReader:
    def __init__(self, name):
        self.name = name
        self.data = self.get_data()
        self.length = len(self.data)
    
    def get_data(self):
        with open(f'web/{self.name}', 'rb') as data:
            return data.read()