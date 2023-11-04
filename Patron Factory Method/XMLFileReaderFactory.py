from Creator import Creator
from XMLFileReader import XMLFileReader


class XMLFileReaderFactory(Creator):
    def create_reader(self):
        return XMLFileReader()