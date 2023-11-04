from Product import Product


class JSONFileReader(Product):
    def read(self, file):
        print(f"lectura de archivo JSON {file}")
