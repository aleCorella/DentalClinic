#Menu
import string
import random
global lista
from tkinter import *
from tkinter import ttk
clientes = [] # aca almacenamos los clientes
tratamientos=[]

def menuprincipal():
    print("|==========================================|")
    print("|=============Menu principal===============|")
    print("|=1-opcion1=Mantenimiento de clientes     =|")
    print("|=2-opcion2=Mantenimineto de tratamientos==|")
    print("|=3-opcion3=Facturacion                  ==|")
    print("|=4-opcion4=Cierre de caja               ==|")
    print("|=5-opcion5=salir                        ==|")
    print("|==========================================|")
    opcion = int(input("Digite una opcion:"))
    if opcion == 1:
        mantenimientoclientes();
    if opcion == 2:
        mantenimientotratamientos();
    if opcion == 3:
        facturacion();
    if opcion == 4:
        cierre();
    if opcion == 5:
            salir = str(input("Desea salir reponder si o no:"))
            if salir == "si":
                print("Gracias por visitar nuestra pagina")
            elif salir == "no":
                menuprincipal();
                

# funciones nuevas para eliminar y buscar clientes en la lista de clientes nueva
def removeClient(nombre):
    POSICION_NOMBRE = 0
    for id_cliente in range(len(clientes)):
        cliente = clientes[id_cliente]
        if cliente[POSICION_NOMBRE] == nombre:
            clientes.pop(id_cliente)
            return
    print("El cliente no existe")
    return 0

def getClient(nombre):
    POSICION_NOMBRE = 0
    for cliente in clientes:
        if cliente[POSICION_NOMBRE] == nombre:
            return cliente
    print("El cliente no existe")
    return 0

def getIdOfClient(nombre):
    POSICION_NOMBRE = 0
    for id_cliente in range(len(clientes)):
        cliente = clientes[id_cliente]
        if cliente[POSICION_NOMBRE] == nombre:
            return id_cliente
    print("El cliente no existe")
    return -1
    
def mantenimientoclientes():
    nombre = ""
    numcedula = ""
    telefono = ""
    correo = ""
    codigo = ""
    print("|====================================================|")
    print("|=============Mantenimiento de clientes==============|")
    print("|=1-opcion1=Incluir cliente                         =|")
    print("|=2-opcion2=Modificar Cliente                       =|")
    print("|=3-opcion3=Eliminar cliente                        =|")
    print("|=4-opcion4=Mostrar cliente                         =|")
    print("|=5-opcion5=Menu principal                          =|")
    print("|====================================================|")
    opcion1 = int(input("Digite una opcion:"))
    if opcion1 == 1:
        nombre = str(input("Ingrese su nombre completo: "))
        numcedula = int(input("Ingrese su numero de cedula:"))
        telefono = int(input("Ingrese su numero telefonico:"))
        correo = str(input("Ingrese su correo electronico:"))
        codigo = string.digits
        print(''.join(random.choice(codigo)for i in range(10)))
        
        clienteNuevo = [] # aca guardamos los datos del cliente que estamos agregando
        # en las siguientes lineas guardamos los datos del cliente 
        clienteNuevo.append(nombre)
        clienteNuevo.append(numcedula)
        clienteNuevo.append(telefono)
        clienteNuevo.append(correo)
        clienteNuevo.append(codigo)

        clientes.append(clienteNuevo) # guardamos al nuevo cliente en la lista de clientes
      

        print("Sus datos se han guardado:")
        mantenimientoclientes();
    if opcion1 == 2:
        nombreParaModificar = str(input("Ingrese el nombre de la persona que desea modificar:"))
        id = getIdOfClient(nombreParaModificar)
        if id != -1:
            nombre1=str(input("Ingrese el nuevo nombre completo:"))
            numcedula1=int(input("Ingrese el nuevo numero de cedula:"))
            telefono1=int(input("Ingrese el nuevo numero telefonico:"))
            correo1=str(input("Ingrese el nuevo correo electronico:"))
 
            clientes[id][0] = nombre1
            clientes[id][1] = numcedula1
            clientes[id][2] = telefono1
            clientes[id][3] = correo1
        mantenimientoclientes();
    if opcion1 == 3:
            cliente = int(input("Digite 1 para ELIMINAR al cliente de lo contrario digite 2:"))
            if cliente == 1:
                nombreParaEliminar = str(input("Ingrese el nombre de la persona que desea eliminar:"))
                removeClient(nombreParaEliminar)
                print("El cliente a sido eliminado correctamente")
            if cliente == 2:
                print("El cliente no ha sido eliminado ")
            mantenimientoclientes();
    if opcion1 == 4:
            nombre1=str(input("Ingrese el nombre del cliente que desea buscar:"))
            cliente = getClient(nombre1)
            if cliente != 0:
                print ("Los datos del cliente serian:")
                print  ("El nombre seria: ", cliente[0])
                print  ("El DNI seria: ", cliente[1])
                print  ("El celular seria: ", cliente[2])
                print  ("El correo seria: ", cliente[3])
                print  ("El codigo seria: ", cliente[4])
            else:
                print  ("Ese cliente no se encuentra registrado")
            mantenimientoclientes();
    if opcion1 == 5:
            menuprincipal();
            
def removeTratamiento(nombreTratamiento):
    POSICION_NOMBRE = 0
    for id_tratamiento in range(len(tratamientos)):
        tratamiento = tratamientos[id_tratamiento]
        if tratamiento[POSICION_NOMBRE] == nombreTratamiento:
            tratamientos.pop(id_tratamiento)
            return
    print("El tratamiento no existe")
    return 0

def getTratamiento(nombreTratamiento):
    POSICION_NOMBRE = 0
    for tratamiento in tratamientos:
        if tratamiento[POSICION_NOMBRE] == nombreTratamiento:
            return tratamiento
    print("El tratamiento no existe")
    return 0

def getIdOfTratamiento(nombreTratamiento):
    POSICION_NOMBRE = 0
    for id_tratamiento in range(len(tratamientos)):
        tratamiento = tratamientos[id_tratamiento]
        if tratamiento[POSICION_NOMBRE] == nombreTratamiento:
            return id_tratamiento
    print("El tratamiento no existe")
    return -1
def mantenimientotratamientos():
    print("|========================================================|")
    print("|=============Mantenimiento de tratamientos==============|")
    print("|=1-opcion1=Lista de tratamientos                       =|")
    print("|=2-opcion2=Incluir tratamiento                         =|")
    print("|=3-opcion3=Modificar tratamiento                       =|")
    print("|=4-opcion4=Eliminar tratamiento                        =|")
    print("|=5-opcion5=Menu principal                              =|")
    print("|========================================================|")
    
    opcion2 = int(input("Digite una opcion:"))
    if opcion2 == 1:
        print ("Lista de tratamientos:")
        for tratamiento in tratamientos:
            print ("El tratamiento seria: ", tratamiento[0])
            print ("El encargado seria: ", tratamiento[1])
            print ("El precio seria: ", tratamiento[2])
        mantenimientotratamientos();
    if opcion2 == 2:
        nombreTratamiento = str(input("Ingrese nombre tratamiento:"))
        encargado3 = str(input("Ingrese nombre encargado:"))
        precio3 = int(input("Ingrese precio:"))
        
        tratamiento = []
        tratamiento.append(nombreTratamiento)
        tratamiento.append(encargado3)
        tratamiento.append(precio3)

        tratamientos.append(tratamiento)            
        print("Sus datos se han guardado:")
        mantenimientotratamientos();
    if opcion2 == 3:
        tratamientoParaModificar = str(input("Ingrese el nombre del tratamiento que desea modificar:"))
        id = getIdOfTratamiento(tratamientoParaModificar)
        if id != -1:
            nombre1=str(input("Ingrese el nuevo nombre:"))
            encargado4=str(input("Ingrese el nuevo encargado:"))
            precio4=int(input("Ingrese el nuevo precio:"))
 
            tratamientos[id][0] = nombre1
            tratamientos[id][1] = encargado4
            tratamientos[id][2] = precio4
        mantenimientotratamientos();
            
    if opcion2 == 4:
            tratamiento=int(input("Digite 1 para ELIMINAR al tratameinto de lo contrario digite 2:"))
            if tratamiento == 1:
                tratamientoParaEliminar = str(input("Ingrese el nombre del tratamiento que desea eliminar:"))
                removeTratamiento(tratamientoParaEliminar)
                print("El tratamineto a sido eliminado correctamente")
            if tratamiento == 2:
                print("El tratamiento no a sido eliminado ")
            mantenimientotratamientos();
    if opcion2 == 5:
            menuprincipal();
def facturacion():
    seguir="S"
    while seguir=="S":
            cliente=str(input("Nombre del cliente:"))
            tratamiento=str(input("Nombre de tratamiento:"))
            costo=int(input("Cantidad a pagar:"))
            print("="*10)
            print(cliente)
            print("="*10)
            print(tratamiento)
            print("="*10)
            print("Cantidad a pagar:",costo)
            menuprincipal();
    

def cierre():

    class Interfaz:

        def __init__(self,ventana):
            self.ventana = ventana
            self.productos = ("limpieza dental-₡50000","extraccion de cordales-₡450000","tratamiento de ortondoncia-₡400000","mensualidad ortondoncia-₡150000","reconstrucción sonrisa-₡5500000","tratamiento de caries-₡70000","tratamiento de nervio-₡300000","blanquiamento dental-₡75000")
            self.cajaCantidad = IntVar()
            self.cajaTotal = IntVar()
            self.total = 0
            self.dibujarComponentes()

        def dibujarComponentes(self):
            self.ventana.title("Caja Registrado")
            self.ventana.geometry("650x450")
            Label(self.ventana,text="Selecciona tu producto: ").place(x=10,y=10)
            Label(self.ventana,text="Seleciona la cantidad: ").place(x=10,y=60)
            Label(self.ventana,text="El total es: ").place(x=450,y=400)
            self.combo = ttk.Combobox(self.ventana,state="readonly")
            self.combo.place(x=10,y=35)
            self.combo["values"]=self.productos
            self.combo.current(0)
            Entry(self.ventana,textvariable=self.cajaCantidad).place(x=10,y=85)
            Entry(self.ventana,textvariable=self.cajaTotal).place(x=520,y=400)
            Button(self.ventana,text="Agregar",command=self.agregarProducto).place(x=10,y=110)

            self.tabla = ttk.Treeview(self.ventana,columns=("Cantidad","Subtotal"))
            self.tabla.heading("#0",text="Producto")
            self.tabla.heading("Cantidad",text="Cantidad")
            self.tabla.heading("Subtotal",text="Subtotal")
            self.tabla.place(x=10,y=150)

        def agregarProducto(self):
            texto = self.combo.get()
            #   tratamiento-$   [0] = producto   [1] = 10    
            datos = texto.split("-₡")
            producto = datos[0]
            precio = datos[1]
            cantidad = self.cajaCantidad.get()
            subtotal = int(precio)*int(cantidad)
            self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(subtotal)))
            self.total = self.total + subtotal
            self.cajaTotal.set("₡"+str(self.total))
        
    obj = Interfaz(Tk())
    obj.ventana.mainloop()
              
    menuprincipal();
    
menuprincipal()
