from tkinter import messagebox, ttk,END,CENTER
import tkinter as tk
from tkinter.simpledialog import askinteger
from Cliente import Cliente
from CursorDelPool import CursorDelPool
from Producto import Producto
from Venta import Venta
from caja import *
from imprimir import imprimirTicket

#FRAME frame
pedido = {}
numeroVenta = 0
def framePedido(frame):

    #TITULO
    tituloLabel = ttk.Label(frame,text='PEDIDO')
    tituloLabel.grid(columnspan=2,column=0,row=0,pady=15)

    #TELEFONO
    telefonoLabel = ttk.Label(frame,text='Telefono:',)
    global telefonoEntry
    telefonoEntry = ttk.Entry(frame,width=40)
    telefonoLabel.grid(row=1,column=0,sticky='w',padx=10,ipady=5)
    telefonoEntry.grid(row=2,column=0,sticky='w',padx=10,ipady=5)
    #NOMBRE
    nombreLabel = ttk.Label(frame,text='Nombre:',)
    global nombreEntry
    nombreEntry = ttk.Entry(frame,width=40)
    nombreLabel.grid(row=4,column=0,sticky='w',padx=10,ipady=5)
    nombreEntry.grid(row=5,column=0,sticky='w',padx=10, ipady=5)

    #DIRECCION
    direccionLabel = ttk.Label(frame,text='Direccion:',)
    global direccionEntry
    direccionEntry = ttk.Entry(frame,width=40)
    direccionLabel.grid(row=6,column=0,sticky='w',padx=10,ipady=5)
    direccionEntry.grid(row=7,column=0,sticky='w',padx=10,ipady=15)

    #BARRIO
    barrioLabel = ttk.Label(frame, text='Barrio:', )
    global barrioEntry
    barrioEntry = ttk.Entry(frame, width=40)
    barrioLabel.grid(row=8, column=0, sticky='w', padx=10, ipady=5)
    barrioEntry.grid(row=9, column=0, sticky='w', padx=10, ipady=15)

    #OBSERVACIONES
    observacionLabel = ttk.Label(frame,text='Observaciones:',)
    global observacionEntry
    observacionEntry = ttk.Entry(frame,width=40)
    observacionLabel.grid(row=10,column=0,sticky='w',padx=10,ipady=5)
    observacionEntry.grid(row=11,column=0,sticky='w',padx=10,ipady=25)


    #FUNCION INSERTAR CLIENTE
    

    botonBuscarCliente = ttk.Button(frame,text='Buscar cliente',command=buscarCliente)
    botonBuscarCliente.grid(row=3,column=0,sticky='w',pady=5,padx=10,ipady=5)


    # TREE PEDIDO
    global treePedido
    treePedido = ttk.Treeview(frame, columns=('sandwich', 'precio'))
    treePedido.column('#0', width=100, anchor=CENTER)
    treePedido.column('#1', width=300, anchor=CENTER)
    treePedido.column('#2', width=100, anchor=CENTER)
    treePedido.heading('#0', text='Cant', anchor=CENTER)
    treePedido.heading('#1', text='Sandwich', anchor=CENTER)
    treePedido.heading('#2', text='Precio', anchor=CENTER)
    treePedido.grid(rowspan=8,row=1,column=1,padx=10)

 

   
    treePedido.bind('<<TreeviewSelect>>', item_selected)

    
    #TABULADOR PRODUCTOS
    productosTabulador = ttk.Notebook(frame)
    sandwiches = ttk.Frame(productosTabulador)
    productosTabulador.add(sandwiches,text='Sandwiches')
    productosTabulador.grid(row=12,column=1, ipadx=100,ipady=70)
    sandwiches.columnconfigure(0,weight=1)
    sandwiches.columnconfigure(1,weight=1)
    sandwiches.columnconfigure(2,weight=1)
    sandwiches.rowconfigure(0,weight=1)
    sandwiches.rowconfigure(1,weight=1)
    sandwiches.rowconfigure(2,weight=1)
    sandwiches.rowconfigure(3,weight=1)


    totalLabel = ttk.Label(sandwiches, text='TOTAL PEDIDO:')
    totalLabel.grid(column=2, row=0, pady=5)
    global totalEntry
    totalEntry = ttk.Entry(sandwiches, state='readonly', width=7)
    totalEntry.grid(column=3, row=0, pady=5)
    domicilioLabel = ttk.Label(sandwiches, text='VALOR DOMICILIO:')
    domicilioLabel.grid(column=0, row=0)
    global domicilioEntry
    domicilioEntry = ttk.Entry(sandwiches, width=7)
    domicilioEntry.grid(column=1, row=0)

    

    botonBrisket = ttk.Button(sandwiches, text='Brisket', command=lambda *args: pulsar(Producto(16000, 'Brisket', 'sandwich')))
    botonBrisket.grid(column=0, row=1)
    botonPernil = ttk.Button(sandwiches, text='Pernil', command=lambda *args: pulsar(Producto(14000, 'Pernil', 'sandwich')))
    botonPernil.grid(column=1, row=1)
    botonArgentino = ttk.Button(sandwiches, text='Argentino', command=lambda *args: pulsar(Producto(11000, 'Argentino', 'sandwich')))
    botonArgentino.grid(column=2, row=1)
    botonHawaiano = ttk.Button(sandwiches, text='Hawaiano', command=lambda *args: pulsar(Producto(14000, 'Hawaiano', 'sandwich')))
    botonHawaiano.grid(column=0, row=2)
    botonPollo = ttk.Button(sandwiches, text='Pollo', command=lambda *args: pulsar(Producto(14000, 'Pollo', 'sandwich')))
    botonPollo.grid(column=1, row=2)
    botonCostilla = ttk.Button(sandwiches, text='Costilla', command=lambda *args: pulsar(Producto(14000, 'Costilla', 'sandwich')))
    botonCostilla.grid(column=2, row=2)
    botonPulledPork = ttk.Button(sandwiches, text='Pulled Pork',command=lambda *args: pulsar(Producto(14000, 'Pulled Pork', 'sandwich')))
    botonPulledPork.grid(column=1, row=3)

    gaseosas = ttk.Frame(productosTabulador)
    productosTabulador.add(gaseosas, text='Gaseosas')
    gaseosas.columnconfigure(0, weight=1)
    gaseosas.columnconfigure(1, weight=1)
    gaseosas.columnconfigure(2, weight=1)
    gaseosas.rowconfigure(0, weight=1)
    gaseosas.rowconfigure(1, weight=1)
    gaseosas.rowconfigure(2, weight=1)
    gaseosas.rowconfigure(3, weight=1)

    botonCocaColaGrande= ttk.Button(gaseosas, text='CocaCola 1.5', command=lambda *args: pulsar(Producto(6000, 'Coca cola 1.5','Gaseosa')))
    botonCocaColaGrande.grid(column=0, row=1)
    botonCocaColaPersonal = ttk.Button(gaseosas, text='Cocacola Personal', command=lambda *args: pulsar(Producto(3000, 'CocaCola Personal','Gaseosa')))
    botonCocaColaPersonal.grid(column=1, row=1)
    botonSpriteGrande = ttk.Button(gaseosas, text='Sprite 1.5', command=lambda *args: pulsar(Producto(6000, 'Sprite 1.5','Gaseosa')))
    botonSpriteGrande.grid(column=2, row=1)
    botonSpritePersonal = ttk.Button(gaseosas, text='Sprite Personal', command=lambda *args: pulsar(Producto(3000, 'Spite Personal','Gaseosa')))
    botonSpritePersonal.grid(column=0, row=2)
    botonPremioGrande = ttk.Button(gaseosas, text='Premio 1.5', command=lambda *args: pulsar(Producto(6000, 'Premio 1.5','Gaseosa')))
    botonPremioGrande.grid(column=1, row=2)
    botonPremioPersonal = ttk.Button(gaseosas, text='Premio Personal', command=lambda *args: pulsar(Producto(3000, 'Premio Personal','Gaseosa')))
    botonPremioPersonal.grid(column=2, row=2)
    botonCuatroGrande = ttk.Button(gaseosas, text='Cuatro 1.5', command=lambda *args: pulsar(Producto(6000, 'Cuatro 1.5','Gaseosa')))
    botonCuatroGrande.grid(column=1, row=3)
    botonCuatroPersonal = ttk.Button(gaseosas, text='Cuatro Personal', command=lambda *args: pulsar(Producto(3000, 'Cuatro Personal','Gaseosa')))
    botonCuatroPersonal.grid(column=0, row=3)
    botonSalsaExtra = ttk.Button(gaseosas, text='Salsa ajo', command=lambda *args: pulsar(Producto(400, 'Copita salsa','Gaseosa')))
    botonSalsaExtra.grid(column=2, row=3)

    enviar = ttk.Button(frame,text='Enviar venta',command=enviarVenta)
    enviar.grid(row=12, column=0,sticky='n',pady=10)
    
#FUNCION INSERTAR CLIENTE
def insertarCliente():
    if buscarCliente(2):
        yesno = messagebox.askyesno('Base datos', 'Desea agregar el cliente a la base de datos ?')
        if yesno:
            try:
                telefono = telefonoEntry.get()
                nombre = nombreEntry.get().upper()
                direccion = direccionEntry.get().upper()
                barrio = barrioEntry.get().upper()

                insert = f"INSERT INTO clientes(telefono, nombre, direccion, barrio) VALUES('{telefono}', '{nombre}', '{direccion}', '{barrio}')"
                with CursorDelPool() as cursor:
                    cursor.execute(insert)
            except Exception as e:
                messagebox.showerror('Error', f'error {e}')

#FUNCION BUSCAR CLIENTE
def buscarCliente(modo=1):
    telefono = telefonoEntry.get()
    select = f"SELECT * FROM clientes WHERE telefono = '{telefono}'"
    try:
        with CursorDelPool() as cursor:
            cursor.execute(select)
            registros = cursor.fetchall()
            if registros == []:
                raise Exception
    except Exception as e:
        if modo == 1:
            messagebox.showerror('Error', 'No se ha encontrado el cliente en la base de datos')
        elif modo == 2:
            return True
    else:
        if modo == 1:
            nombreEntry.delete(0,END)
            direccionEntry.delete(0,END)
            barrioEntry.delete(0,END)

            nombreEntry.insert(tk.INSERT, registros[0][1])
            direccionEntry.insert(tk.INSERT, registros[0][2])
            barrioEntry.insert(tk.INSERT, registros[0][3])
        elif modo == 2:
            return False

#VALIDACION ENTRY TELEFONO
def validarEntry(entry):

    varEntryS = entry
    try:
        varEntryI =int(varEntryS.replace(" ",""))
        if type(varEntryI) != int:
            raise Exception
        elif len(varEntryS) != 11:
            raise Exception
        else:
            return True
    except Exception as e:
        print(e)
        messagebox.showerror('Error','Verifica que el formato del numero sea correcto y que no haya letras')

def item_selected(event):
    for selected_item in treePedido.selection():
        finalTotal = 0
        p = treePedido.set(selected_item, '#1')
        print(p)
        del pedido[p]
        treePedido.delete(selected_item)
    finalTotal = 0
    for i in treePedido.get_children():
        celda = int(treePedido.set(i, "#2"))
        finalTotal += celda

        totalEntry.config(state=tk.NORMAL)
        totalEntry.delete(0, tk.END)
        totalEntry.insert(tk.INSERT, finalTotal)
        totalEntry.config(state='readonly')

#FUNCION PARA AGREGAR PRODUCTO PULSANDO EL BOTON
def pulsar(producto):
    cant = askinteger('Cantidad', 'Cantidad: ')
    total = cant * producto.precio
    for i in treePedido.get_children():
        e = treePedido.set(i,"0")
        print(e)
        if e == producto.nombre:
            messagebox.showwarning('cuidado', 'Ya agregaste ese sandwich')
            raise Exception

    treePedido.insert("", END, text=cant, values=(producto.nombre, total))
    pedido[producto.nombre] = f'{cant} - {producto.nombre} - {total}'
    print(pedido)
    finalTotal = 0
    for i in treePedido.get_children():
        celda = int(treePedido.set(i, "#2"))
        finalTotal += celda
        totalEntry.config(state=tk.NORMAL)
        totalEntry.delete(0, tk.END)
        totalEntry.insert(tk.INSERT, finalTotal)
        totalEntry.config(state='readonly')

#FUNCIONES ENVIAR VENTA
def enviarVenta():
    try:
        if validarEntry(telefonoEntry.get()):
            
            subtotal = int(totalEntry.get())
            domi = int(domicilioEntry.get())
            total = subtotal + domi
            cliente = Cliente(telefonoEntry.get(), nombreEntry.get(), direccionEntry.get(),barrioEntry.get())
            observaciones = observacionEntry.get()
            formatPedido = ''
            formatPedido2=''
            for i in pedido.values():
                formatPedido += f'{i}\n'
                formatPedido2 += f' {i} /'
            global numeroVenta
            numeroVenta += 1
            ventaMayor = numeroVentaMayor()
            venta = Venta(cliente,subtotal,ventaMayor,formatPedido2)
            # imprimirTicket(venta,formatPedido,observaciones,total,domi)
            with CursorDelPool() as cursor:
                insert_ventas = f"INSERT INTO pendientes(id_ventas,cliente, total, pedido) VALUES('{venta.numeroVenta}', '{venta.Cliente.__str__()}', '{venta.total}','{venta.pedido}')"
                cursor.execute(insert_ventas)
            messagebox.showinfo('info', 'VENTA REALIZADA')
            insertarCliente()
            reinicioVenta()

            actPendientes()
    except Exception as e:
        messagebox.showerror('Error','Verifica que esten todos los campos llenos y la impresora este conectada')
        print(f'error {e}')

def numeroVentaMayor():
    global numeroVenta
    selectVentas = 'SELECT id_ventas FROM ventas'
    selectPendientes = 'SELECT id_ventas FROM pendientes'
    with CursorDelPool() as cursor:
        cursor.execute(selectVentas)
        ventas = cursor.fetchall()
        cursor.execute(selectPendientes)
        pendientes = cursor.fetchall()
        ventasYpendientes = ventas + pendientes
    for i in ventasYpendientes:
        if numeroVenta <= int(i[0]):
            numeroVenta = int(i[0])+1
    return numeroVenta

def reinicioVenta():
    finalTotal=0
    pedido.clear()
    registros = treePedido.get_children()
    for i in registros:
        treePedido.delete(i)