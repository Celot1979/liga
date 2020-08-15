import csv
jugador = {}
jugador_Segunda = {}
jugador_SegundaB = {}
def archivo_primero():
    with open("jugador_uno.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in jugador.items():
            write.writerow([key, value])

def archivo_segundo():
    with open("jugador_dos.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in jugador_Segunda.items():
            write.writerow([Key, value])

def archivo_segundoB():
    with open("jugador_tres.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in jugador_Segunda.items():
            write.writerow([Key, value])

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

def borrar_jugador():
    jb= str(input("¿ Quieres borrar un jugador: Si / No \n==>"))
    if jb == "si" or jb == "Si":
        nombre= str(input(" Introduce el nombre del jugador:"))
        jugador.pop(nombre)
        with open("jugador_uno.csv", "w") as csv_file:
            write = csv.writer(csv_file)
            for Key, value in jugador.items():
                write.writerow([Key, value])
    elif jb == "no" or jb == "No":
        archivo_primero()
        pass
    else:
        print(" Error 405")
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

def modificar_jugador():
    modif= str(input("Qué desea modificar: (nombre), (edad), (posicion), (nacionalidad"))
    if modif == "nombre" or modif == "Nombre":
        nombre = str(input("Ingresa el nombre que deseas modificar"))
        jugador.pop(nombre)
        nombre = str(input("Ingrese el nuevo nombre"))
        jugador[nombre] = nombre
        archivo_primero()
#Agrega el nobre dos veces. Quizás tendremos que ir poniendo uno a uno los campos que no se han modificado





#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
def gestionar_jugadores():
    j = str(input("¿De qué categoría quieres gestionar la plantilla?\n1. Primera División\n2. Segunda División"
                  "\n3. SegundaB División\n==>"))

    if j == "1":
        for i in range(20):
            nombre = str(input("\nNombre del Jugador: "))
            edad = str(input("Edad: "))
            posicion = str(input("Posicion: "))
            nacionalidad = str(input("Nacionalidad: "))
            jugador[nombre] = edad, posicion, nacionalidad
            seguir= str(input("¿Quiere seguir añadiendo jugadores?: SI/No"))
            if seguir == "si" or seguir == "Si":
                archivo_primero()
                pass
            elif seguir == "no" or seguir == "No":
                seguir_dos=str(input(" Qué opción desea ejecutar?: (Borrar)/(modificar)/(salir)\n ==>"))
                if seguir_dos == "borrar" or seguir_dos == "Borrar":
                    borrar_jugador()
                    archivo_primero()
                    seguir_tres = str(input("¿Quieres seguir añadiendo jugadores? Si / No"))
                    if seguir_tres == "si" or seguir_tres == "Si":
                        pass
                    else:
                        exit()
                elif seguir_dos == "modificar" or seguir_dos == "Modificar":
                    modificar_jugador()









    """if j == "1":
        nombre = str(input("\nNombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador[nombre]=edad, posicion, nacionalidad
        archivo_primero()
        borrar_jugador()
        archivo_primero()




    elif j == "2":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_Segunda[nombre] = edad, posicion, nacionalidad
        archivo_segundo()

    elif j == "3":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_SegundaB[nombre] = edad, posicion, nacionalidad
        archivo_segundoB()"""
