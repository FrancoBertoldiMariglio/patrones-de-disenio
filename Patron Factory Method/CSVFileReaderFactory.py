from Creator import Creator
from CSVFileReader import CSVFileReader


class CSVFileReaderFactory(Creator):
    def create_reader(self):
        return CSVFileReader()