import csv
jugador_P = {}
jugador_S = {}
jugador_B = {}
def archivo_primero():
    with open("jugador_uno.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in jugador_p.items():
            write.writerow([key, value])

def gestionar_jugadores():
    j = str(input("¿De qué categoría quieres gestionar la plantilla?\n1.Primera División\n2.Segunda División"
                  "\n3.SegundaB División"))
    if j == "1":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_P[nombre] = edad, posicion, nacionalidad
        archivo_primero()
        #if nombre == "salir" or nombre == "Salir":


    elif j == "2":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_S[nombre] = edad, posicion, nacionalidad

    elif j == "3":
        nombre = str(input("Nombre del Jugador: "))
        edad = str(input("Edad: "))
        posicion = str(input("Posicion: "))
        nacionalidad = str(input("Nacionalidad: "))
        jugador_B[nombre] = edad, posicion, nacionalidad
