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
