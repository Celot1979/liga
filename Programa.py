from Liga2 import agregar_equipo, agregar_equipoB,agregar_equipoC
from Liga2 import añadir_archivo1,añadir_archivo2,añadir_archivo3,borrar







decision_usuario= str(input("Qué desea hacer:\n1.Gestionar equipos de fútbol\n2.Gestionar jugadores\nEscriba aquí "
"su respuesta\n==>"))
if decision_usuario== "1":
    gestionar = str(input("\n1 Agregar equipos de fútbol\n2 Borrar Equipo de fútbol\n3 Mostrar equipo de futbol"
    "4 Modificar -nombre o id- de Equipo\n ==>"))
    if gestionar=="1":
        c = str(
            input("\n¿Categoria del equipo que quieres incluir?: \n1. Primera\n2. Segunda\n3. SegundaB\n4.Salir\n==>"))
        if c == "1":
            agregar_equipo()
            añadir_archivo1()
        elif c== "2":
            agregar_equipoB()
            añadir_archivo2()

        elif c == "3":
            agregar_equipoC()
            añadir_archivo3()


    elif gestionar =="2" :
        B= str(input("¿En que categoria deseas borrar el equipo?:\n1Primera\nSegunda\nSegundaB" ))
        borrar()
    else:
        decision_usuario = str(
            input("Qué desea hacer:\n1.Gestionar equipos de fútbol\n2.Gestionar jugadores\nEscriba aquí "
                  "su respuesta\n==>"))
