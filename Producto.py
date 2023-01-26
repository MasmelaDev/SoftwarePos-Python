class Producto:
    def __init__(self,precio,nombre,categoria):
        self._precio = precio
        self._nombre = nombre
        self._categoria = categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def categotia(self):
        return self._categoria

    @categotia.setter
    def categoria(self,value):
        self._categoria = value