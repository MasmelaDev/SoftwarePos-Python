import tkinter as tk
from tkinter import  ttk
from pedidos import framePedido
from caja import actCaja, actPendientes, frameCaja
from clientes import actualizarClientes, frameClientes

ventana = tk.Tk()
ventana.geometry('900x1200')
ventana.title('SANDCIBATTA')


control_tabulador = ttk.Notebook(ventana)
control_tabulador.config(height=900,width=1000)

#FRAME PEDIDOS
pedidos= ttk.Frame(control_tabulador)
control_tabulador.add(pedidos, text='Pedidos')
pedidos.columnconfigure(0,weight=1)
pedidos.columnconfigure(1,weight=3)
framePedido(pedidos)

#FRAME CAJA
caja = ttk.Frame(control_tabulador)
control_tabulador.add(caja,text='Caja')
frameCaja(caja)

#FRAME CLIENTES
clientes = ttk.Frame(control_tabulador)
control_tabulador.add(clientes,text='Clientes')
frameClientes(clientes)


control_tabulador.pack()

actualizarClientes()
actPendientes()
actCaja()
ventana.mainloop()
