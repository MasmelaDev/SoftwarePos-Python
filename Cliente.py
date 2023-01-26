class Cliente:
    def __init__(self,telefono,nombre,direccion,barrio):
        self._telefono= telefono
        self._nombre = nombre
        self._direccion = direccion
        self._barrio = barrio


    def __str__(self):
        return f' {self._telefono} | {self._nombre} | {self._direccion} {self._barrio}'


    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def barrio(self):
        return self._barrio

    @barrio.setter
    def barrio(self, value):
        self._barrio = value