class Contacto:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nCorreo: {self.correo}\nTeléfono: {self.telefono}"
    
    def actualizar(self, nombre=None, apellido=None, correo=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if correo:
            self.correo = correo
        if telefono:
            self.telefono = telefono


class GestorContactos:
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("✅ Contacto agregado.")
    
    def eliminar_contacto(self, correo):
        for contacto in self.contactos:
            if contacto.correo == correo:
                self.contactos.remove(contacto)
                print("❌ Contacto eliminado.")
                return
        print("⚠️ No se encontró el contacto.")
    
    def buscar_contacto(self, criterio, valor):
        resultados = []
        for contacto in self.contactos:
            if criterio == "nombre" and valor.lower() in contacto.nombre.lower():
                resultados.append(contacto)
            elif criterio == "correo" and valor.lower() in contacto.correo.lower():
                resultados.append(contacto)
            # Añade más criterios si es necesario...
        
        if resultados:
            print(f"\n🔍 Resultados ({len(resultados)}):")
            for contacto in resultados:
                print(contacto)
        else:
            print("🔎 No hay resultados.")

def mostrar_menu():
    print("\n--- MENÚ GESTOR DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")

def main():
    gestor = GestorContactos()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            print("\n📝 Nuevo contacto:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            gestor.agregar_contacto(Contacto(nombre, apellido, correo, telefono))
        
        elif opcion == "2":
            correo = input("\nIngresa el correo a eliminar: ")
            gestor.eliminar_contacto(correo)
        
        elif opcion == "3":
            criterio = input("\nBuscar por (nombre/correo): ").lower()
            valor = input("Valor a buscar: ")
            gestor.buscar_contacto(criterio, valor)
        
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()