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

decision_usuario= str(input("Qué desea hacer:\n1.Gestionar equipos de fútbol\n2.Gestionar jugadores\nEscriba aquí "
"su respuesta\n==>"))
def borrar():
    B = str(input("¿En que categoria deseas borrar el equipo?:\n1Primera\nSegunda\nSegundaB"))
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



def agregar_equipo():
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











        #print(primera)

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

def agregar_equipoC():
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
        #print(segundaB)
def añadir_archivo3():
    with open("segunda3.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in segundaB.items():
            write.writerow([key, value])



































































"""if id == "borrar":
    id = input("id: ")
    self.primera.pop(id)
    self.mostrar_equipo()
    exit()"""