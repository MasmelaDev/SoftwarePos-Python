from tkinter import messagebox
from escpos.printer import Usb
import time

try:
        c = Usb(0x0483, 0x5720)
except Exception as e:
                messagebox.showerror("error","no se pudo conectar la impresora, verifica que este conectada y encendida")

def conectarImpresora():
        try:
                global c
                c = Usb(0x0483, 0x5720)
                messagebox.showinfo("info","Impresora conectada con exito")

        except Exception as e:
                messagebox.showerror("error","no se pudo conectar la impresora, verifica que este conectada y encendida")

def imprimirTicket(venta,pedido,observaciones,total,domi):
        c.set(align="center",bold=True,width=2,height=2,custom_size=True)
        c.image("./img.png")
        c.text(f'Sandcibatta\n')
        c.ln(2)
        c.set(align="left")
        c.text(f'venta: {venta.numeroVenta}')
        c.text(f'{time.strftime("                               %I:%M:%S")}')
        c.ln(2)
        c.set(align="center",bold=True)
        c.text('Datos del pedido\n')
        c.ln(1)
        c.set(align="left")
        c.set(bold=True)
        c.text(f'Telefono: ')
        c.set(bold=False)
        c.text(f'{venta.Cliente.telefono}\n')
        c.set(bold=True)
        c.text('Cliente: ')
        c.set(bold=False)
        c.text(f'{venta.Cliente.nombre}\n')
        c.set(bold=True)
        c.text('Direccion: ')
        c.set(bold=False)
        c.text(f'{venta.Cliente.direccion}\n')
        c.set(bold=True)
        c.text('Barrio: ')
        c.set(bold=False)
        c.text(f'{venta.Cliente.barrio}\n')
        c.ln(1)
        c.set(align="center",bold=True)
        c.text('________________________________________________\n')
        c.ln(1)
        c.set(align="center",width=2,height=2,custom_size=True)
        c.text(pedido)
        c.ln(3)
        c.set(align="right",bold=True)
        c.text('SUBTOTAL: ')
        c.set(align="right",bold=False)
        c.text(f'  $ {venta.total}\n')
        c.set(align="right",bold=True)
        c.text('Valor Domicilio: ')
        c.set(align="right",bold=False)
        c.text(f'   $ {domi}\n')
        c.set(align="right",bold=True)
        c.text('TOTAL: ')
        c.set(align="right",bold=False)
        c.text(f'  $ {total}\n')
        c.cut()
        if observaciones !="":
                c.set(align="center",width=2,height=2,custom_size=True)
                c.text(f'{observaciones}\n')
                c.cut()
                