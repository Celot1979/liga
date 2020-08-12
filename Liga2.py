import csv

print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("P R O G R A M A    G E S T I O N    F U T B O L")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
primera = {}
segunda = {}
segundaB = {}
pr=[]


def borrar():
    B = str(input("¿En que categoria deseas borrar el equipo?:\n1.Primera\n2.Segunda\n3.SegundaB"))
    if B== "1":
        id = str(input(" Introducce la ID del equipo: "))
        primera.pop(id)
        with open("primeraB.csv", "w") as csv_file:
            write = csv.writer(csv_file)
            for key, value in primera.items():
                write.writerow([key, value])

    elif B=="2":
        id = str(input(" Introducce la ID del equipo: "))
        segunda.pop(id)
        with open("segunda2.csv", "w") as csv_file:
            write = csv.writer(csv_file)
            for key, value in segunda.items():
                write.writerow([key, value])
    elif B=="3":
        id = str(input(" Introducce la ID del equipo: "))
        segundaB.pop(id)
        for i in range(20):
            id = str(input("ID del equipo: "))
            nombre_equipo = str(input("Nombre del equipo: "))
            segundaB[id] = nombre_equipo
            if id == "salir" or nombre_equipo == "salir":
                añadir_archivo1()
                exit()

def añadir_archivo1():
    with open("primeraB.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in primera.items():
            write.writerow([key, value])

def agregar_equipoB():
    for i in range(20):
        id = str(input("ID del equipo: "))
        nombre_equipo = str(input("Nombre del equipo: "))
        segunda[id] = nombre_equipo
        if id == "salir" or nombre_equipo=="salir":
            añadir_archivo2()
            exit()
        elif id == "borrar" or nombre_equipo=="borrar":
            borrar()
            añadir_archivo2()
            exit()
        #print(segunda)
def añadir_archivo2():
    with open("segunda2.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in segunda.items():
            write.writerow([key, value])


def modificar():
    pregunta=str(input("Selecciona que equipo de que categoria quieres modificar:\nA.Primera División\nB.Segunda Division"
                       "\nC.SegundaB"))
    if pregunta=="A":
        id = input("Ingrese el Id que desea modificar: ")
        primera.pop(id)
        id = input("Ingrese el nuevo ID")
        nombre = input("Ingrese el nuevo nombre")
        primera[id] = nombre
    else:
        print("error")







def modificar():
    opcion = input("Seleccione la categoria del equipo que desea modificar:\nA.Primera\nB.Segunda\nC.SegundaB")
    if opcion == "A":
        id = input("Ingrese el Id que desea modificar: ")
        primera.pop(id)
        id = input("Ingrese el nuevo ID")
        nombre= input("Ingrese el nuevo nombre")
        primera[id]=nombre
    elif opcion == "B":
        id = input("Ingrese el Id que desea modificar: ")
        segunda.pop(id)
        id = input("Ingrese el nuevo ID")
        nombre= input("Ingrese el nuevo nombre")
        segunda[id]=nombre
    elif opcion == "C":
        id = input("Ingrese el Id que desea modificar: ")
        segundaB.pop(id)
        id = input("Ingrese el nuevo ID")
        nombre= input("Ingrese el nuevo nombre")
        segundaB[id]=nombre





#--------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def gestionar_categorias():
    c = str(input("Desea gestionar:\n1.Primera División\n2.Segunda División\n3.SegundaB División\n===>"))
    if c == "1":
        print("OPCIONES: Agregar (ID y nombre del equipo)\n          Escribir -salir-\n          Escribir -borrar-\n"
              "         Escribir -modificar-\n         ===>")
        for i in range(20):
            id = str(input("ID del equipo: "))
            nombre_equipo = str(input("Nombre del equipo: "))
            primera[id] = nombre_equipo
            if id == "salir" or nombre_equipo=="salir":
                añadir_archivo1()
                exit()
            elif id == "borrar" or nombre_equipo=="borrar":
                borrar()
                añadir_archivo1()
                exit()
            elif id == "modificar" or nombre_equipo=="modificar":
               modificar()
               añadir_archivo1()
               exit()


    elif c=="2":
        for i in range(20):
            id = str(input("ID del equipo: "))
            nombre_equipo = str(input("Nombre del equipo: "))
            segunda[id] = nombre_equipo
            if id == "salir" or nombre_equipo=="salir":
                añadir_archivo2()
                exit()
            elif id == "borrar" or nombre_equipo=="borrar":
                borrar()
                añadir_archivo2()
                exit()
            elif id == "modificar" or nombre_equipo=="modificar":
               modificar()
               añadir_archivo1()
               exit()
    elif c=="3":
        for i in range(20):
            id = str(input("ID del equipo: "))
            nombre_equipo = str(input("Nombre del equipo: "))
            segundaB[id] = nombre_equipo
            if id == "salir" or nombre_equipo=="salir":
                añadir_archivo3()
                exit()
            elif id == "borrar" or nombre_equipo=="borrar":
                borrar()
                añadir_archivo3()
                exit()
    else:
        print("Gracias por usar nuestro programa. Esperamos volver a verle pronto")
        exit()
















































































"""if id == "borrar":
    id = input("id: ")
    self.primera.pop(id)
    self.mostrar_equipo()
    exit()"""