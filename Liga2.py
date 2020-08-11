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
decision_usuario= str(input("Qué desea hacer:\n1.Gestionar equipos de fútbol\n2.Gestionar jugadores\nEscriba aquí su respuesta\n==>"))
if decision_usuario == "1":
    gestionar=str(input("Que acción desea realizar: \n1 Agregar equipos de fútbol\n2 Borrar Equipo de fútbol\n3 Mostrar equipo de futbol"
                        "4 Modificar -nombre o id- de Equipo\n ==>"))
    if gestionar == "1":
        c = str(input("\n¿Categoria del equipo que quieres incluir?: \n1. Primera\n2. Segunda\n3. SegundaB\n Salir\n==>"))
        if c == "1":
            print(" Ha decidido registrar equipos de 1º División ")
            ce= str(input(" Qué opción desea realizar: \n1.Agregar equipo,\n2.Borrar equipo\n3.Mostrar equipos\n Mostrar equipos\n4.==>"))
            if ce == "1":
                for i in range(20):
                    id = str(input("ID del equipo: "))
                    nombre_equipo = str(input("Nombre del equipo: "))
                    primera[id] = nombre_equipo
                    print(primera)
                    with open("primeraB.csv", "w") as csv_file:
                        write = csv.writer(csv_file)
                        for key, value in primera.items():
                            write.writerow([key, value])
                    if id == "salir" or nombre_equipo=="salir":
                        print(primera)
                        with open("primeraB.csv", "w") as csv_file:
                            write = csv.writer(csv_file)
                            for key, value in primera.items():
                                write.writerow([key, value])
                                pass


                                ce = str(input(" Qué opción desea realizar: \n1.Agregar equipo,\n2.Borrar equipo\n3.Mostrar equipos\n Mostrar equipos\n4.==>"))

            if ce == "2":
                print("Deseas borrar un equipo")
                id = str(input(" Introducce la ID del equipo: "))
                primera.pop(id)
                print(primera)












































"""if id == "borrar":
    id = input("id: ")
    self.primera.pop(id)
    self.mostrar_equipo()
    exit()"""