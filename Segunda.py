jugador_Segunda = {}
def archivo_segundo():
    with open("jugador_dos.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in jugador_Segunda.items():
            write.writerow([key, value])


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