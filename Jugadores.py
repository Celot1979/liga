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
            write.writerow([key, value])

def archivo_segundoB():
    with open("jugador_tres.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in jugador_SegundaB.items():
            write.writerow([key, value])






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
        exit()


def borrar_jugador_dos():
    bs = str(input("¿ Quieres borrar un jugador: Si / No \n==>"))
    if bs == "si" or bs == "Si":
        nombre = str(input(" Introduce el nombre del jugador:"))
        jugador_Segunda.pop(nombre)
        with open("jugador_dos", "w") as csv_file:
            write = csv.writer(csv_file)
            for Key, value in jugador_Segunda.items():
                write.writerow([Key, value])
    elif bs == "no" or bs == "No":
        archivo_segundo()
        pass
    else:
        print(" Error 405")
        exit()

def borrar_jugador3():
    bsB = str(input("¿ Quieres borrar un jugador: Si / No \n==>"))
    if bsB == "si" or bsB == "Si":
        nombre = str(input(" Introduce el nombre del jugador:"))
        jugador_SegundaB.pop(nombre)
        with open("jugador_tres", "w") as csv_file:
            write = csv.writer(csv_file)
            for Key, value in jugador_SegundaB.items():
                write.writerow([Key, value])
    elif bsB == "no" or bsB == "No":
        archivo_segundoB()
        pass
    else:
        print(" Error 405")
        exit()




#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

def modificar_jugador():
    modif= str(input("¿Desea modificar  el registro de un jugador? "))
    if modif == "si" or modif == "Si":
        nombre = str(input("Ingresa el nombre que deseas modificar ==> "))
        jugador.pop(nombre)
        nombre = str(input("Ingrese el nuevo nombre ==> "))

        edad= str(input("¿Cúal es su edad? ==> "))
        posicion= str(input("Cúal es la posición en el campo? ==>  "))
        nacionalidad = str(input("¿Nacionalidad? ==> "))
        jugador[nombre] = edad, posicion, nacionalidad
        archivo_primero()
        repregunta= str(input("Desea modificar el registro de otro jugador? ==> "))
        if repregunta == "si" or repregunta == "Si":
            modificar_jugador()
            archivo_primero()
        elif repregunta == "no" or repregunta == "No":
            archivo_primero()
            exit()
        else:
            print("ERROR 750")
            exit()

    elif modif == "No" or modif == "no":
        exit()
    else:
        print(" ERROR  750 ")
        archivo_primero()
        exit()

def modificar_jugadorSegunda():
    mod= str(input("¿Desea modificar  el registro de un jugador? "))
    if mod == "si" or mod == "Si":
        nombre = str(input("Ingresa el nombre que deseas modificar ==> "))
        jugador_Segunda.pop(nombre)
        nombre = str(input("Ingrese el nuevo nombre ==> "))

        edad= str(input("¿Cúal es su edad? ==> "))
        posicion= str(input("Cúal es la posición en el campo? ==>  "))
        nacionalidad = str(input("¿Nacionalidad? ==> "))
        jugador_Segunda[nombre] = edad, posicion, nacionalidad
        archivo_segundo()
        repregunta= str(input("Desea modificar el registro de otro jugador? ==> "))
        if repregunta == "si" or repregunta == "Si":
            modificar_jugadorSegunda()
            archivo_segundo()
        elif repregunta == "no" or repregunta == "No":
            archivo_segundo()
            exit()
        else:
            print("ERROR 750")
            exit()

    elif mod == "No" or mod == "no":
        exit()
    else:
        print(" ERROR  750 ")
        archivo_segundo()
        exit()

def modificar_jugadorSegundaB():
    mod= str(input("¿Desea modificar  el registro de un jugador? "))
    if mod == "si" or mod == "Si":
        nombre = str(input("Ingresa el nombre que deseas modificar ==> "))
        jugador_SegundaB.pop(nombre)
        nombre = str(input("Ingrese el nuevo nombre ==> "))

        edad= str(input("¿Cúal es su edad? ==> "))
        posicion= str(input("Cúal es la posición en el campo? ==>  "))
        nacionalidad = str(input("¿Nacionalidad? ==> "))
        jugador_SegundaB[nombre] = edad, posicion, nacionalidad
        archivo_segundoB()
        repregunta= str(input("Desea modificar el registro de otro jugador? ==> "))
        if repregunta == "si" or repregunta == "Si":
            modificar_jugadorSegundaB()
            archivo_segundoB()
        elif repregunta == "no" or repregunta == "No":
            archivo_segundoB()
            exit()
        else:
            print("ERROR 750")
            exit()

    elif mod == "No" or mod == "no":
        exit()
    else:
        print(" ERROR  750 ")
        archivo_segundoB()
        exit()












#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
def gestionar_jugadores():
    j = str(input("¿De qué categoría quieres gestionar la plantilla?\n1. Primera División\n2. Segunda División"
                  "\n3. SegundaB División\n==>"))

    if j == "1":
        for i in range(20):
            nombre = str(input("\nNombre del Jugador: ==> "))
            edad = str(input("Edad: "))
            posicion = str(input("Posicion: ==> "))
            nacionalidad = str(input("Nacionalidad: ==> "))
            jugador[nombre] = edad, posicion, nacionalidad
            seguir= str(input("¿Quiere seguir añadiendo jugadores?: SI/No ==> "))
            if seguir == "si" or seguir == "Si":
                archivo_primero()
                pass
            elif seguir == "no" or seguir == "No":
                seguir_dos=str(input(" Qué opción desea ejecutar?: (Borrar)/(modificar)/(salir)\n ==>"))
                if seguir_dos == "borrar" or seguir_dos == "Borrar":
                    borrar_jugador()
                    archivo_primero()
                    seguir_tres = str(input("¿Quieres seguir añadiendo jugadores? Si / No ==> "))
                    if seguir_tres == "si" or seguir_tres == "Si":
                        pass
                    else:
                        exit()
                elif seguir_dos == "modificar" or seguir_dos == "Modificar":
                    modificar_jugador()
                elif seguir_dos == "salir" or seguir_dos == "Salir":
                    archivo_primero()
                    exit()
            else:
                print(" ERROR  750 ")
                break
    elif j == "2":
        for e in range(20):
            nombre = str(input("\nNombre del Jugador: ==> "))
            edad = str(input("Edad: "))
            posicion = str(input("Posicion: ==> "))
            nacionalidad = str(input("Nacionalidad: ==> "))
            jugador_Segunda[nombre] = edad, posicion, nacionalidad
            con = str(input("¿Quiere seguir añadiendo jugadores?: SI/No ==> "))
            if con == "si" or con == "Si":
                archivo_segundo()
                pass
            elif con == "no" or con == "No":
                seguir_dos = str(input(" Qué opción desea ejecutar?: (Borrar)/(modificar)/(salir)\n ==>"))
                if seguir_dos == "borrar" or seguir_dos == "Borrar":
                    borrar_jugador_dos()
                    archivo_segundo()
                    seguir_tres = str(input("¿Quieres seguir añadiendo jugadores? Si / No ==> "))
                    if seguir_tres == "si" or seguir_tres == "Si":
                        pass
                    else:
                        exit()
                elif seguir_dos == "modificar" or seguir_dos == "Modificar":
                    modificar_jugadorSegunda()
                elif seguir_dos == "salir" or seguir_dos == "Salir":
                    archivo_segundo()
                    exit()
            else:
                print(" ERROR  750 ")
                break















        

