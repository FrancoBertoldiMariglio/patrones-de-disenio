from Product import Product


class CSVFileReader(Product):
    def read(self, file):
        print(f"lectura de archivo CSV {file}")
