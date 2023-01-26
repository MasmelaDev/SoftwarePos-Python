import Cliente

class Venta:

    def __init__(self,Cliente,total,numeroVenta,pedido):
        self._total = total
        self._numeroVenta = numeroVenta
        self._Cliente = Cliente
        self._pedido =pedido


    @property
    def pedido(self):
        return self._pedido

    @pedido.setter
    def pedido(self, value):
        self._pedido = value
    @property
    def Cliente(self):
        return self._Cliente

    @Cliente.setter
    def Cliente(self, value):
        self._Cliente = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total= value

    @property
    def numeroVenta(self):
        return self._numeroVenta

    @numeroVenta.setter
    def numeroVenta(self, value):
        self._numeroVenta = value



    def __str__(self):
        return f'Venta: {self._numeroVenta} | {self._Cliente}  |  TOTAL: {self._total}'