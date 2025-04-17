class Contacto:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, contacto):
        self.contactos.append(contacto)

    def eliminar(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return
        print('Contacto no encontrado')

    def buscar(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f'Nombre: {contacto.nombre}, Apellido: {contacto.apellido}, Correo: {contacto.email}, Teléfono: {contacto.telefono}')
                return
        print('Contacto no encontrado')

    def actualizar(self, nombre, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_telefono):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.nombre = nuevo_nombre
                contacto.apellido = nuevo_apellido
                contacto.email = nuevo_email
                contacto.telefono = nuevo_telefono
                print('Contacto actualizado')
                return
        print('Contacto no encontrado')
       
def menu_de_opciones():
    agenda = Agenda()
    while True:
        print("**Opciones:**")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Salir")
    
        opcion = int(input("Digite la opción deseada: "))
        
        if opcion == 1:
          nombre = input("Digite el nombre: ")
          apellido = input("Digite el apellido: ")
          email = input("Digite el email: ")
          telefono = input("Digite el telefono: ")
          agenda.agregar(Contacto(nombre, apellido, email, telefono))
          print("el contacto ha sido agregado exitosamente")
          
        elif opcion == 2:
          nombre = input("Nombre del contacto a eliminar: ")
          agenda.eliminar(nombre)
          print("el contacto ha sido eliminado exitosamente")
          
        elif opcion == 3:
          nombre = input("Nombre del contacto a buscar: ")
          agenda.buscar(nombre)
          
        elif opcion == 4:
          nombre = input("Nombre del contacto a actualizar: ")
          nuevo_nombre = input("Nuevo nombre: ")
          nuevo_apellido = input("Nuevo apellido: ")
          nuevo_email = input("Nuevo correo: ")
          nuevo_telefono = input("Nuevo teléfono: ")
          agenda.actualizar(nombre, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_telefono)
          print("el contacto ha sido actualizado exitosamente")
          
        elif opcion == 5:
            print("¡Hasta pronto!")
            break

        else:
          print("Opción no válida.")

if __name__ == "__main__":
    menu_de_opciones()