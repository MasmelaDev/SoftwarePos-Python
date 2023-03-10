# Software POS, sistema de ventas para negocio

> ### Importante - Software para uso exclusivo de sistemas operativos linux (Creado para restaurante Sandcibatta)

## Instalacion



- instala las dependencias 

`$ pip install -r requirements.txt`

- Usa PostgresSQL Para la base de datos, Ejecuta el script el cual crea la base de datos: script.sql

- Modifica los datos en el Conexion.py

```python
    class Conexion:
        _DATABASE = 'test_db'
        _USERNAME = 'postgres'
        _PASSWORD = 'admin'
        _HOST = '127.0.0.1'
        _DB_PORT = '5432'
        _MIN_CON = 1
        _MAX_CON = 5
        _pool = None
```

## Uso de la impresora

- Modifica en imprimir.py la conexion de la impresora con los datos de tu impresora pos
```python
   c = Usb(0x0483, 0x5720)
```
- descomenta la linea en pedidos.py la cual imprime el ticket 

```python
    #imprimirTicket(venta,formatPedido,observaciones,total,domi)
```