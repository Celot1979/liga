

class Liga():
    primera = {}
    segunda = {}
    segundaB = {}

    def __init__(self, nombre_liga, numero_equipos, categoria):
        self.nombre = nombre_liga
        self.equipos = numero_equipos
        self.categoria = categoria

    def __str__(self):
        return "El nombre de la liga es {}\nLa forman {} equipos\nEn {}".format(self.nombre, self.equipos,
                                                                                self.categoria)
    def añadir_equipos(self, id, nombre_equipo):
        p= str(input("¿Quieres añadir un equipo?: "))
        if p == "si" or p== "si":
            c= str(input("¿Categoria del equipo que queires incluir?: \n1. Primera\n2. Segunda\n3. SegundaB\n ==>"))
            if c == "1":
                for i in range(20):
                    id= str(input("ID del equipo: "))
                    if id == "salir":
                        self.mostrar_equipo()
                        print("Gracias por usar nuestro programa")
                        exit()
                    nombre_equipo= str(input("Nombre del equipo: "))
                    if nombre_equipo == "salir":
                        self.mostrar_equipo()
                        print("Gracias por usar nuestro programa")
                        exit()
                    print("Has agregado con éxito el equipo´")
                    self.primera[id] = nombre_equipo

            elif c == "2":
                for se in range(20):
                    id = str(input("ID del equipo: "))
                    if id == "salir":
                        self.mostrar_equipo()
                        print("Gracias por usar nuestro programa")
                        exit()
                    nombre_equipo = str(input("Nombre del equipo: "))
                    if nombre_equipo == "salir":
                        self.mostrar_equipo()
                        print("Gracias por usar nuestro programa")
                        exit()
                    print("Has agregado con éxito el equipo´")
                    self.segunda[id] = nombre_equipo
            elif c == "3":
                for e in range(20):
                    id = str(input("ID del equipo: "))
                    if id == "salir":
                        self.mostrar_equipo()
                        print("Gracias por usar nuestro programa")
                        exit()
                    nombre_equipo = str(input("Nombre del equipo: "))
                    if nombre_equipo == "salir":
                        self.mostrar_equipo()
                        print("Gracias por usar nuestro programa")
                        exit()
                    print("Has agregado con éxito el equipo´")
                    self.segundaB[id] = nombre_equipo
            else:
                print("Gracias por usar nuestro programa")

#----------------------------------------------------------------------------------------------------------------------

    def mostrar_equipo(self):
        print("Los equipos son : ")
        for i in self.primera.keys():
            print("ID: " + str(i))
            print("Nombre: " + str(self.primera[i]))

# ----------------------------------------------------------------------------------------------------------------------
    def borrar_equipo(self,nombre):
        del self.primera[nombre]

 # ----------------------------------------------------------------------------------------------------------------------
    def modificar (self, nombre_equipo=None):
        opcion = int(input("Seleccione :\n1)Si desea modificar ID\n2)Si desa modificar nombre: "))
        if opcion == 1:
            id =  input("Ingrese el Id que desea modificar: ")
            id = self.primera[id]
            self.borrar_equipo(id)
            id= input("Ingrese el nuevo ID")
            self.añadir_equipos(id, nombre_equipo)
        elif opcion == 2:
            id = input("Ingrese el id de el equipo que desea cambiar el nombre: ")
            id= input("Ingrese el nuevo nombre: ")
            self.primera[id]= nombre_equipo
        print(self.primera[id])
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

class Equipos(Liga):
    jugadores= {}
    def __init__ (self,nombre_liga, numero_equipos, categoria ):
        self.nombre = nombre_liga
        self.equipos = numero_equipos
        self.categoria = categoria
# ----------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return "En la {} tienen {} con su categoria: {}".format(self.nombre, self.equipos, self.categoria)
 # ----------------------------------------------------------------------------------------------------------------------
    def añadir_jugadores(self, id, nombre_jugador, edad, posicion, nacionalidad ):
        r= str(input("Quieres añadir un jugador: "))
        while r == "Si" or r =="si":
            for i in range(1,4):
                id = str(input("Cual es la Id: "))
                if id == "salir":
                    self.mostrar_jugadores()
                    exit()
                nombre_jugador = str(input("¿Cúal es el nombre del jugador?: "))
                edad = int(input("¿Cúal es la edad del jugador?: "))
                posicion= str(input("¿Cúal es la posicion del jugador en el campo?: "))
                nacionalidad= str(input("¿Cúal es la nacionalidad de  jugador?: "))
                self.jugadores[id] = nombre_jugador, edad, posicion, nacionalidad
        if r != "si" or r != "SI":
            print(" Error 506 !!!! Vuelva al principio !!!")
# ----------------------------------------------------------------------------------------------------------------------




    def mostrar_jugadores(self):
        print("Los jugadores del son : ")
        for i in self.jugadores.keys():
            print("ID: " + str(i))
            print("Nombre: " + str(self.jugadores[i][0]))
            print("Edad: " + str(self.jugadores[i][1]))
            print("Posicion: " + str(self.jugadores[i][2]))
            print("Nacionalidad: " + str(self.jugadores[i][3]))
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------------

l = Liga (nombre_liga= "BBVA", numero_equipos= 20, categoria= "Primera Division")
print(l)
l.añadir_equipos(1, "Real Madrid")
l.añadir_equipos(2,"FC.Barcelona")
#l.mostrar_equipo()
#l.mostrar_uno()
#p = Equipos("BBVA",20,"Primera Division")
#print(p)
#p.añadir_jugadores(1,"Pablo", 23, "Portero", "española")
#p.añadir_jugadores()
#p.mostrar_jugadores()

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
