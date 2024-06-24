#Productos personal
import os #Importar comandos del CMD de windows
#import pyfiglet
os.system("cls")
#print(pyfiglet.figlet_format("Tienda Productos Personales"))

archivo = 'productos.txt'
folio = 10000

productos=[] 
ventas=[]



def leer_productos_archivo(archivo):
    # Lista para almacenar los datoslista_datos = []   

    # Abrimos el archivo en modo lectura  r  Read
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            # Eliminamos los espacios en blanco y los saltos de línea
            linea = linea.strip()
            # Dividimos la línea por comas
            productos = linea.split(',')
            # Creamos un diccionario con los datos
            productos.append(productos)
           

    return

def buscar(archivo):
    # Lista para almacenar los datos
    lista_datos = []   

    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            # Eliminamos los espacios en blanco y los saltos de línea
            linea = linea.strip()
            # Dividimos la línea por comas
            archivo = linea.split(',')
            
            # Verificamos si el RUT coincide con el RUT buscado
            if archivo[0] == productos:
                # Retornamos los datos como una lista
                return archivo

    return -1

def eliminar(archivo):
    # Lista para almacenar los datos actualizados
    lista_datos_actualizada = []
    
    existe=buscar(productos)
    
    if existe != -1:
        # Abrimos el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leemos cada línea del archivo
            for linea in file:
                # Eliminamos los espacios en blanco y los saltos de línea
                linea = linea.strip()
                # Dividimos la línea por comas
                archivo = linea.split(',')
                # Verificamos si el RUT no coincide con el RUT a eliminar
                if archivo[0] != rut:
                    # Si no coincide, añadimos el registro a la lista actualizada
                    lista_datos_actualizada.append(linea)
                #else:
                #    sw=0 #rut no existe
        
        # Abrimos el archivo en modo escritura para actualizar el contenido
        # w  write
        with open(archivo, 'w') as file:
            # Escribimos cada registro actualizado en el archivo
            ultima_linea=len(lista_datos_actualizada)
            #print("última línea: ", ultima_linea)
            #os.system("pause")
            c=1
            for linea in lista_datos_actualizada:
                if c != ultima_linea: 
                   file.write(linea + '\n')
                else:
                   file.write(linea)
                c=c+1

        return 1 #eliminado    
    else:
        return -1


















"""
def get_folio():
    elemento= len(ventas)-1
    return (ventas[elemento][0])


def buscar_id (id):
    indice=0
    for prod in productos:
        print(indice,"  ",prod)
        if a[0] == id:
            return indice
        indice=indice+1
    return -1
"""
os.system("pause")
os.system("cls")

opcion=0
while opcion<=4:
    
    print("""
            Sistema de venta
        --------------------------
          1. Vender productos
          2. Reportes
          3. Mantenedores
          4. Salir

          """)

    opcion=int(input("Ingrese una opcion entre el 1-4: "))
    if opcion >= 1 and opcion <= 4:
    
     match opcion:
        case 1:
            while True:
                print("    ventas de productos   ")
                id=input("ingrese ID ")
                a=buscar_id(id)
                if a != -1:
                    print("encontrado en el elemento ", a)
                    producto=productos[a]
                    print(producto[0],"",producto[1],"",producto[2],"",producto[3],"",producto[4],"",producto[5])
                    cantidad=int(input("ingrese cantidad a comprar: "))
                    
                    if cantidad <=producto[6]:
                        print(" stock disponible ")
                        total=cantidad*producto[6]
                        print(f"el total a pagar por {cantidad} productos es {total}")
                        respuesta=input("¿desea realizar la compra s/n: ")
                        if respuesta.lower() == "s":
                            producto[6]=producto[6]-cantidad
                            ventas.append([get_folio(),+1,fecha,id,cantidad,total ])
                    else:
                        print("Error, la cantida ingresada supera el limite de stock")
                respuesta=input("¿Desea comprar otro producto?")
                if respuesta.lower() == "n":
                    break
        case 2: 
             os.system("cls")
             op=0
             while op<=4:
                print("""
                                    REPORTES
                       ----------------------------------
                       1. General de ventas (con total)
                       2. Ventas por fecha especifica (con total)
                       3. Ventas por rango de fecha (con total)
                       4. Salir al menu principal 
                       
                      """)
                op=int(input("Ingrese una opcion 1-4: "))
                
                match op:
                    case 1:
                        print("ventas")
                        fecha=input("ingrese la fecha de venta: ")

                        for venta in ventas:
                            print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                            a = a + venta[4]
                        print("total=",a)


                    case 2:
                        fecha=int(input("ingrese la fecha de venta (dd-mm-aaaa): "))

                        a=0
                        for venta in ventas:
                            if venta[1]== fecha:
                                a = a + venta[2]
                                print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                                print("fecha de venta entregada.")
                                os.system("Pause")


                    case 3:
                        fecha=input("ingrese la fecha de inicio (dd-mm-aaaa): ")
                        fecha=input("ingrese la fecha de termino (dd-mm-aaaa): ")

                        total=0

                        for venta in ventas:
                            fecha_venta= venta[0]

                            if fecha <= fecha_venta and fecha_venta <= fecha:
                                print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                                total = total + venta[4]

                                print("el total es: ",total)
                    
                    case 4:
                        break
                    

                if op==4:
                    break

                
                 
        case 3: 
            os.system("cls")
            op=0
            while op<=6:
                print("""
                        Mantenedor de productos
                      ---------------------------------
                      1. Agregar
                      2. Buscar
                      3. Eliminar
                      4. Modificar
                      5. Listar
                      6. Salir al menú principal
                      
                      """)
                op=int(input("Ingrese una opcion 1-6 "))
                
                match op:
                    case 1:
                        print("\nAgregar\n")
                        id = input("Ingrese la id:  ")
                        Producto=input("Ingrese el producto:  ")
                        Marca=input("Ingresar marca:  ")
                        Modelo=input("Ingrese el modelo:  ")
                        Unidad=int(input("Ingresar unidades:  "))
                        Stock=int(input("Ingresar el stock:  "))
                        Precio=int(input("Ingresar precio:  "))
                                
                        productos.append([id, Producto, Marca, Modelo, Unidad, Stock, Precio])

                    case 2:
                        print("Buscar con funcion")
                        id=input("Ingrese la id del producto al buscar:  ")
                        lista=buscar_id(id)
                        if lista != -1:
                            print(lista)
                        else:
                            print("Error, id no existe")

                        
                    case 3:
                        id = int(input("Ingrese id producto a eliminar:  "))

                        i = 0
                        sw = 0 
                        while i <= (len(productos) - 1):
                            if productos[i][0] == id:
                                sw = 1  
                                productos.pop(i) 
                                break 
                            else:
                                    i += 1 
                        if sw == 0: print("id no existe...")


                    case 4: 
                        print("\n Modificar\n")
                        
                        id=int(input("Ingrese id producto a modificar: "))

                        i = 0
                        sw = 0 
                        while i <= (len(productos) - 1):
                                if productos[i][0] == id:
                                    sw = 1  
                                    print("id encontrado en el indice ", i)
                                    print(productos[i])
                                    id = input("Ingrese el id del producto: ")
                                    Producto = input("Ingrese nombre del producto:  ")
                                    Marca = input("Ingrese la marca:  ")
                                    Modelo = input("Ingrese el modelo:  ")
                                    Unidad = int(input("Ingrese la unidad:  "))
                                    Stock = int(input("Ingrese el stock:  "))
                                    Precio = int(input("Ingrese el precio:  "))
                                    
                                    productos[i][0] = id
                                    productos[i][1] = Producto
                                    productos[i][2] = Marca
                                    productos[i][3] = Modelo
                                    productos[i][4] = Unidad
                                    productos[i][5] = Stock
                                    productos[i][6] = Precio
                                    print("\n Listo! datos modificados")
                                    break 
                                else:
                                    i += 1 
                                if sw == 0: print("id no existe...")

                    case 5:
                        print("Enter para continuar")
                        os.system("pause")
                        sw=0
                        for a in  productos:
                            if a[0] == id:
                                sw=1
                            print ("ID    Producto         Marca     Modelo    Unidad    Stock     Precio")  
                            print (a[0],"  ",a[1],"  ",a[2],"  ",a[3],"   ",a[4],"  ",a[5],"       ",a[6])
                

                os.system("pause")
                if op == 6:
                     break #Salir del while secundario y entra al principal

    if opcion==5:
        break
        
print("Fin del menú")
