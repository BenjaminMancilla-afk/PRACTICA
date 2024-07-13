import json
import random
import csv

# Función para cargar empleados desde JSON
def cargar_empleados():
    try:
        with open('empleados.json', 'r') as file:
            empleados = json.load(file)
    except FileNotFoundError:
        empleados = []
    return empleados

# Función para guardar empleados en JSON
def guardar_empleados(empleados):
    with open('empleados.json', 'w') as file:
        json.dump(empleados, file, indent=4)

# Función para generar ID de empleado automáticamente
def generar_id_empleado(empleados):
    if not empleados:
        return 100000
    else:
        ids = [emp['id_empleado'] for emp in empleados]
        return max(ids) + 1

# Función para registrar un nuevo empleado
def registrar_usuario(empleados):
    id_empleado = generar_id_empleado(empleados)
    nombre = input("Ingrese el nombre del informático: ")
    apellido = input("Ingrese el apellido del informático: ")
    edad = random.randint(22, 45)
    id_cargo = random.choice(['C1', 'C2'])  # Asignación aleatoria de cargo
    if id_cargo == 'C1':
        sueldo_base = random.randint(2000000, 3000000)
    else:
        sueldo_base = random.randint(800000, 2000000)

    nuevo_empleado = {
        'id_empleado': id_empleado,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'id_cargo': id_cargo,
        'sueldo_base': sueldo_base
    }
    empleados.append(nuevo_empleado)
    guardar_empleados(empleados)
    print(f"Empleado registrado correctamente con ID: {id_empleado}")

# Función para buscar un usuario por ID
def buscar_usuario(empleados, id_buscado):
    for emp in empleados:
        if emp['id_empleado'] == id_buscado:
            print(f"ID: {emp['id_empleado']}")
            print(f"Nombre: {emp['nombre']}")
            print(f"Apellido: {emp['apellido']}")
            print(f"Edad: {emp['edad']}")
            print(f"ID Cargo: {emp['id_cargo']}")
            print(f"Sueldo Base: {emp['sueldo_base']}")
            return
    print("Empleado no encontrado.")

# Función para editar un usuario por ID
def editar_usuario(empleados, id_editar):
    for emp in empleados:
        if emp['id_empleado'] == id_editar:
            while True:
                print("Editar usuario, seleccione el campo a editar:")
                print("[1] Nombre")
                print("[2] Apellido")
                print("[3] Edad")
                print("[4] ID Cargo")
                print("[5] Sueldo Base")
                print("[6] Guardar y salir")
                opcion = input("Seleccione una opción: ")
                if opcion == '1':
                    emp['nombre'] = input("Nuevo nombre: ")
                elif opcion == '2':
                    emp['apellido'] = input("Nuevo apellido: ")
                elif opcion == '3':
                    emp['edad'] = int(input("Nueva edad: "))
                elif opcion == '4':
                    emp['id_cargo'] = input("Nuevo ID Cargo: ")
                elif opcion == '5':
                    emp['sueldo_base'] = int(input("Nuevo sueldo base: "))
                elif opcion == '6':
                    guardar_empleados(empleados)
                    print("Empleado editado exitosamente.")
                    return
                else:
                    print("Opción no válida.")

    print("Empleado no encontrado.")

# Función para eliminar un usuario por ID
def eliminar_usuario(empleados, id_eliminar):
    for i, emp in enumerate(empleados):
        if emp['id_empleado'] == id_eliminar:
            del empleados[i]
            guardar_empleados(empleados)
            print("Empleado eliminado correctamente.")
            return
    print("Empleado no encontrado.")

# Función para listar todos los usuarios y exportar a CSV
def listar_usuarios(empleados):
    if not empleados:
        print("No hay empleados registrados.")
        return

    print("Lista de empleados:")
    for emp in empleados:
        print(f"ID: {emp['id_empleado']}, Nombre: {emp['nombre']}, Apellido: {emp['apellido']}, Edad: {emp['edad']}, ID Cargo: {emp['id_cargo']}, Sueldo Base: {emp['sueldo_base']}")

    exportar_csv = input("¿Desea exportar los datos a un archivo CSV? (S/N): ")
    if exportar_csv.upper() == 'S':
        with open('empleados.csv', 'w', newline='') as csvfile:
            fieldnames = ['id_empleado', 'nombre', 'apellido', 'edad', 'id_cargo', 'sueldo_base']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for emp in empleados:
                writer.writerow(emp)

        print("Datos exportados correctamente a empleados.csv")

# Función principal del programa
def main():
    empleados = cargar_empleados()

    while True:
        print("\n=== Menú ===")
        print("1. Registrar Usuario")
        print("2. Buscar un usuario")
        print("3. Editar usuario")
        print("4. Eliminar un usuario")
        print("5. Listar todos los usuarios y exportar a CSV")
        print("6. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(empleados)
        elif opcion == '2':
            id_buscar = int(input("Ingrese el ID del empleado a buscar: "))
            buscar_usuario(empleados, id_buscar)
        elif opcion == '3':
            id_editar = int(input("Ingrese el ID del empleado a editar: "))
            editar_usuario(empleados, id_editar)
        elif opcion == '4':
            id_eliminar = int(input("Ingrese el ID del empleado a eliminar: "))
            eliminar_usuario(empleados, id_eliminar)
        elif opcion == '5':
            listar_usuarios(empleados)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
