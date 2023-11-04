from Product import Product


class XMLFileReader(Product):
    def read(self, file):
        print(f"lectura de archivo XML {file}")
