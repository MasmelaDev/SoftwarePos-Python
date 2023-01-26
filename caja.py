
from tkinter import CENTER, END, messagebox, ttk
import tkinter as tk
from tkinter.simpledialog import askstring
from CursorDelPool import CursorDelPool


def frameCaja(frame):


    # TREE PEDIDOS PENDIENTES
    labelPendientes= ttk.Label(frame,text="PENDIENTES")
    labelPendientes.place(x=450,y=15)

    global treePendientes
    treePendientes = ttk.Treeview(frame, columns=('total','venta','domiciliario'))
    treePendientes.column('#0', width=530, anchor=CENTER)
    treePendientes.column('#1', width=130, anchor=CENTER)
    treePendientes.column('#2', width=100, anchor=CENTER)
    treePendientes.column('#3', width=160, anchor=CENTER)

    treePendientes.heading('#0', text='Cliente', anchor=CENTER)
    treePendientes.heading('#1', text='Total', anchor=CENTER)
    treePendientes.heading('#2', text='Venta', anchor=CENTER)
    treePendientes.heading('#3', text='Domiciliario', anchor=CENTER)
    treePendientes.place(x=0,y=40)
    botonActPendientes = ttk.Button(frame,command=actPendientes,text='Actualizar')
    botonActPendientes.place(x=50,y=300,width=180)

    botonConfirmarPago = ttk.Button(frame,command=confirmarPago,text='Confirmar pago')
    botonConfirmarPago.place(x=250,y=300,width=180)

    botonAsignarDomiciliario = ttk.Button(frame,command=asignarDomiciliario,text='Asignar Domiciliario')
    botonAsignarDomiciliario.place(x=450,y=300,width=180)

    botonBorrarPendientes = ttk.Button(frame,command=borrarPendientes,text='Borrar')
    botonBorrarPendientes.place(x=650,y=300,width=180)

    labelCaja= ttk.Label(frame,text="VENTAS CONFIRMADAS")
    labelCaja.place(x=400,y=400)
    global treeCaja
    treeCaja = ttk.Treeview(frame, columns=('total','venta'))
    treeCaja.column('#0', width=530, anchor=CENTER)
    treeCaja.column('#1', width=130, anchor=CENTER)
    treeCaja.column('#2', width=100, anchor=CENTER)

    treeCaja.heading('#0', text='Cliente', anchor=CENTER)
    treeCaja.heading('#1', text='Total', anchor=CENTER)
    treeCaja.heading('#2', text='Venta', anchor=CENTER)
    treeCaja.place(x=60,y=450)

    labelBase = ttk.Label(frame,text='Base:')
    labelBase.place(x=50, y=690)
    global baseVar
    baseVar = tk.StringVar()
    baseVar.set('0')
    global entryBase
    entryBase = ttk.Entry(frame,width=8,textvariable=baseVar)
    entryBase.place(x=145, y=690)
    labelTotalVentas = ttk.Label(frame,text='Total Ventas:')
    labelTotalVentas.place(x=50, y=720)
    global entryTotalVentas
    entryTotalVentas = ttk.Entry(frame,width=8,state='readonly')
    entryTotalVentas.place(x=145,y=720)
    labelTotalCaja = ttk.Label(frame,text='Total Caja:')
    labelTotalCaja.place(x=50,y=750)
    global entryTotalCaja
    entryTotalCaja = ttk.Entry(frame,width=8, state='readonly')
    entryTotalCaja.place(x=145,y=750)

    botonActCaja = ttk.Button(frame,command=actCaja,text='Actualizar caja')
    botonActCaja.place(x=70,y=780)
    botonBorrar = ttk.Button(frame,text='Borrar venta',command=borrarVenta)
    botonBorrar.place(x=600,y=690)
    botonBorrarVentas = ttk.Button(frame,text='Borrar ventas',command=borrarVentas)
    botonBorrarVentas.place(x=720,y=690)


def actPendientes():
        registros_pendientes = treePendientes.get_children()
        for i in registros_pendientes:
            treePendientes.delete(i)
        with CursorDelPool() as cursor:
            select_ventas = 'SELECT * FROM pendientes'
            cursor.execute(select_ventas)
            registros_pendientes = cursor.fetchall()
            for i in registros_pendientes:
                tablaPendientes = treePendientes.insert("", END, text=i[1], values=(i[2],i[0],i[4]))
                treePendientes.insert(tablaPendientes, END, text=i[3])

def asignarDomiciliario():
        for selected_item in treePendientes.selection():
            id_venta = treePendientes.set(selected_item, '#2')
            domiciliario = askstring("DOMICILIARIO",'Nombre:')
            insert = f"UPDATE pendientes SET domiciliario='{domiciliario}' WHERE id_ventas='{id_venta}'"
            with CursorDelPool() as cursor:
                cursor.execute(insert)
        actPendientes()

def borrarPendientes():
        if messagebox.askyesno("Borrar","Estas seguro que quieres borrar el pedido"):
            for selected_item in treePendientes.selection():
                id_venta = treePendientes.set(selected_item, '#2')
                delete = f"DELETE FROM pendientes WHERE id_ventas = '{id_venta}'"
                with CursorDelPool() as cursor:
                    cursor.execute(delete)
                treePendientes.delete(selected_item)
            # registros = treePedido.get_children()
            # for i in registros:
            #     treePedido.delete(i)
            # pedido.clear()
        else:
            pass



def confirmarPago():
    for selected_item in treePendientes.selection():
        id_venta = treePendientes.set(selected_item, '#2')
        delete = f"DELETE FROM pendientes WHERE id_ventas = '{id_venta}'"
        select = f"SELECT * FROM pendientes WHERE id_ventas ='{id_venta}'"
        
        with CursorDelPool() as cursor:
            cursor.execute(select)
            registros_pendientes = cursor.fetchall()
            insert = f"INSERT INTO ventas(id_ventas,cliente, total, pedido) VALUES('{registros_pendientes[0][0]}', '{registros_pendientes[0][1]}', '{registros_pendientes[0][2]}','{registros_pendientes[0][3]}')"
            cursor.execute(insert)
            cursor.execute(delete)
        treePendientes.delete(selected_item)
        actCaja()
        messagebox.showinfo("REALIZADO",'PAGO CONFIRMADO Y ENVIADO A VENTAS')
def actCaja():
    registros_caja = treeCaja.get_children()
    for i in registros_caja:
        treeCaja.delete(i)
    with CursorDelPool() as cursor:
        select_ventas = 'SELECT * FROM ventas'
        cursor.execute(select_ventas)
        registros_caja = cursor.fetchall()

        for i in registros_caja:
            tablaVenta = treeCaja.insert("", END, text=i[1], values=(i[2],i[0]))
            treeCaja.insert(tablaVenta, END, text=i[3])
    sumaVentas = 0
    for i in treeCaja.get_children():
        celda = int(treeCaja.set(i, "#1"))
        sumaVentas += celda

    entryTotalVentas.config(state=tk.NORMAL)
    entryTotalVentas.delete(0, END)
    entryTotalVentas.insert(tk.INSERT, sumaVentas)
    entryTotalVentas.config(state='readonly')

    totalCaja = int(entryBase.get()) + int(entryTotalVentas.get())
    entryTotalCaja.config(state=tk.NORMAL)
    entryTotalCaja.delete(0,END)
    entryTotalCaja.insert(tk.INSERT,totalCaja)
    entryTotalCaja.config(state='readonly')

def borrarVenta():
    for selected_item in treeCaja.selection():
        id_venta = treeCaja.set(selected_item, '#2')
        delete = f"DELETE FROM ventas WHERE id_ventas = '{id_venta}'"
        with CursorDelPool() as cursor:
            cursor.execute(delete)
        treeCaja.delete(selected_item)
    # registros = treePedido.get_children()
    # for i in registros:
    #     treePedido.delete(i)
    # pedido.clear()
    sumaVentas = 0
    for i in treeCaja.get_children():
        celda = int(treeCaja.set(i,"#1"))
        sumaVentas+=celda


    entryTotalVentas.config(state=tk.NORMAL)
    entryTotalVentas.delete(0, END)
    entryTotalVentas.insert(tk.INSERT, sumaVentas)
    entryTotalVentas.config(state='readonly')

    totalCaja = int(entryBase.get()) + int(entryTotalVentas.get())
    entryTotalCaja.config(state=tk.NORMAL)
    entryTotalCaja.delete(0, END)
    entryTotalCaja.insert(tk.INSERT, totalCaja)
    entryTotalCaja.config(state='readonly')

def borrarVentas():
    delete = f"DELETE FROM ventas"
    if messagebox.askyesno("Borrar","Estas seguro que quieres borrar las ventas"):
        with CursorDelPool() as cursor:
            cursor.execute(delete)
        actCaja()
    else:
        pass