from tkinter import CENTER, END, ttk
from CursorDelPool import CursorDelPool
from imprimir import conectarImpresora

def frameClientes(frame):
    global treeClientes
    treeClientes = ttk.Treeview(frame, columns=( 'telefono','direccion','barrio'))
    treeClientes.column('#0', width=200, anchor=CENTER)
    treeClientes.column('#1', width=200, anchor=CENTER)
    treeClientes.column('#2', width=200, anchor=CENTER)
    treeClientes.column('#3', width=200, anchor=CENTER)


    treeClientes.heading('#0', text='Nombre', anchor=CENTER)
    treeClientes.heading('#1', text='Numero', anchor=CENTER)
    treeClientes.heading('#2', text='Direccion', anchor=CENTER)
    treeClientes.heading('#3', text='Barrio', anchor=CENTER)
    treeClientes.place(x=50,y=60,height=600)
    botonActualizar = ttk.Button(frame,text='Actualizar',command=actualizarClientes)
    botonActualizar.place(x=80,y=700,width=100)
    botonBorrarCliente=ttk.Button(frame,text='Borrar Cliente',command=borrarCliente)
    botonBorrarCliente.place(x=200,y=700,width=100)
    botonConectarImpresora = ttk.Button(frame,text='Conectar impresora',command=conectarImpresora)
    botonConectarImpresora.place(x=710,y=20)

def actualizarClientes():
    registros = treeClientes.get_children()
    for i in registros:
        treeClientes.delete(i)
    select = 'SELECT * FROM clientes'
    with CursorDelPool() as cursor:
        cursor.execute(select)
        registros = cursor.fetchall()
        for i in registros:
            treeClientes.insert("", END, text=i[1], values=(i[0],i[2],i[3]))
def borrarCliente():
    for i in treeClientes.selection():
        tel = treeClientes.set(i,'#1')
        delete = f"DELETE FROM clientes WHERE telefono = '{tel}'"
        with CursorDelPool() as cursor:
            cursor.execute(delete)
        treeClientes.delete(i)