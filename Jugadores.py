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
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
def gestionar_jugadores():
    j = str(input("¿De qué categoría quieres gestionar la plantilla?\n1.Primera División\n2.Segunda División"
                  "\n3.SegundaB División\n==>"))
    if j == "1":
        nombre = str(input("\nNombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador[nombre]=edad, posicion, nacionalidad
        archivo_primero()


    elif j == "2":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_Segunda[nombre] = edad, posicion, nacionalidad

    elif j == "3":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_SegundaB[nombre] = edad, posicion, nacionalidad
