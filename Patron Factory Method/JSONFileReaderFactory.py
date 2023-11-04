from Creator import Creator
from JSONFileReader import JSONFileReader


class JSONFileReaderFactory(Creator):
    def create_reader(self):
        return JSONFileReader()