class Agenda:
    contactos = {}

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return "Esta agenda pertenece a {} y puedes contactarlo en {}".format(self.nombre, self.telefono)

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def mostrar_todos(self):
        print("Los contactos son: ")
        for i in self.contactos.keys():
            print("Nombre: " + str(i))
            print("Telefono: " + str(self.contactos[i]))

    def borrar_contacto(self, nombre):

        del self.contactos[nombre]

    def modificar(self):
        opcion = int(input("seleccione 1) si desea modificar nombre y 2) si desea modificar telef"))

        if opcion == 1:
            nombre = input("Ingrese el contacto a cambiar: ")
            numero = self.contactos[nombre]
            self.borrar_contacto(nombre)
            nombre = input("Ingrese el nuevo nombre: ")
            self.agregar_contacto(nombre, numero)
            print(primera)

        elif opcion == 2:
            nombre = input("Ingrese el nombre de la persona que desea cambiar telefono: ")
            numero = input("Ingrese el nuevo numero: ")
            self.contactos[nombre] = numero

        print(self.contactos[nombre])


Manuel = Agenda(nombre="Manuel", telefono=4454)
print(Manuel)

Manuel.agregar_contacto("Daniel", 465456)

Manuel.agregar_contacto("Juan", 5464)
Manuel.agregar_contacto("Pilar", 567890)

#Manuel.mostrar_un_contacto("Daniel")
#Manuel.mostrar_todos()
#Manuel.borrar_contacto(input("Nombre: "))
#Manuel.mostrar_todos()
# 1
Manuel.modificar()

#---------------------------------------------------------------------------------------------------------------------
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
    gestionar=str(input("\n1 Agregar equipos de fútbol\n2 Borrar Equipo de fútbol\n3 Mostrar equipo de futbol"
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
                                ce = str(input(" Qué opción desea realizar: \n1.Agregar equipo,\n2.Borrar equipo\n3.Mostrar equipos\n Mostrar equipos\n4.==>"))

            if ce == "2":
                print("Deseas borrar un equipo")
                id = str(input(" Introducce la ID del equipo: "))
                primera.pop(id)
                print(primera)

""" Queda averiguar como a salir se pueda escoger nuevamente el menú e ir a borrar"""

