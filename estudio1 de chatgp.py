import random
import csv
import math
from collections import Counter

# Datos iniciales
destinos = ["París", "Londres", "Nueva York", "Tokio", "Sídney", "Roma", "Berlín", "Barcelona"]
costos_destinos = {destino: random.randint(100, 1000) for destino in destinos}

reservas = [
    {"cliente": "Juan Pérez", "destino": "París", "cantidad": 2},
    {"cliente": "María García", "destino": "Londres", "cantidad": 3},
    {"cliente": "Carlos López", "destino": "Nueva York", "cantidad": 1},
    {"cliente": "Ana Martínez", "destino": "Tokio", "cantidad": 4},
    {"cliente": "Pedro Rodríguez", "destino": "Sídney", "cantidad": 2}
]

def asignar_costos():
    global costos_destinos
    costos_destinos = {destino: random.randint(100, 1000) for destino in destinos}
    print("Costos aleatorios asignados a los destinos turísticos.")

def clasificar_destinos():
    menores_300 = []
    entre_300_y_700 = []
    superiores_700 = []

    for destino, costo in costos_destinos.items():
        if costo < 300:
            menores_300.append((destino, costo))
        elif 300 <= costo <= 700:
            entre_300_y_700.append((destino, costo))
        else:
            superiores_700.append((destino, costo))

    print("Clasificación de destinos por costo:")
    
    print("Menores a $300")
    print(f"TOTAL: {len(menores_300)}")
    print("Nombre del destino  Costo")
    print("---------------------------")
    for destino, costo in menores_300:
        print(f"{destino:<20} ${costo}")
    print("")

    print("Entre $300 y $700")
    print(f"TOTAL: {len(entre_300_y_700)}")
    print("Nombre del destino  Costo")
    print("---------------------------")
    for destino, costo in entre_300_y_700:
        print(f"{destino:<20} ${costo}")
    print("")

    print("Superiores a $700")
    print(f"TOTAL: {len(superiores_700)}")
    print("Nombre del destino  Costo")
    print("---------------------------")
    for destino, costo in superiores_700:
        print(f"{destino:<20} ${costo}")
    print("")

def ver_estadisticas():
    total_reservas = len(reservas)
    if total_reservas == 0:
        print("No hay reservas para mostrar estadísticas.")
        return

    destinos_reservados = [reserva["destino"] for reserva in reservas]
    destino_mas_reservado = Counter(destinos_reservados).most_common(1)[0][0]
    
    total_personas = sum(reserva["cantidad"] for reserva in reservas)
    promedio_personas = total_personas / total_reservas
    
    valores_reserva = [costos_destinos[reserva["destino"]] * reserva["cantidad"] for reserva in reservas]
    multiplicacion_valores = math.prod(valores_reserva)
    media_geometrica = multiplicacion_valores ** (1 / total_reservas)
    
    print("Estadísticas de reservas:")
    print(f"Total de reservas: {total_reservas}")
    print(f"Destino más reservado: {destino_mas_reservado}")
    print(f"Promedio de personas por reserva: {promedio_personas:.2f}")
    print(f"Media Geométrica del valor de reserva: {media_geometrica:.2f}")

def reporte_reservas():
    print("Reporte de reservas:")
    print("Nombre del cliente  Destino turístico  Cantidad de personas  Costo total")
    print("-------------------------------------------------------------------------")
    for reserva in reservas:
        destino = reserva["destino"]
        cantidad = reserva["cantidad"]
        costo_total = costos_destinos[destino] * cantidad
        print(f"{reserva['cliente']:<20} {destino:<20} {cantidad:<20} ${costo_total}")

    with open('reporte_reservas.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre del cliente', 'Destino turístico', 'Cantidad de personas', 'Costo total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for reserva in reservas:
            destino = reserva["destino"]
            cantidad = reserva["cantidad"]
            costo_total = costos_destinos[destino] * cantidad
            writer.writerow({'Nombre del cliente': reserva['cliente'], 'Destino turístico': destino,
                             'Cantidad de personas': cantidad, 'Costo total': costo_total})

    print("El reporte ha sido exportado a 'reporte_reservas.csv'.")

def mostrar_menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Asignar costos aleatorios a los destinos")
        print("2. Clasificar destinos por costo")
        print("3. Ver estadísticas de reservas")
        print("4. Reporte de reservas")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            asignar_costos()
        elif opcion == "2":
            clasificar_destinos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_reservas()
        elif opcion == "5":
            print("Gracias por usar el programa. Desarrollado por [Tu Nombre].")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

# Iniciar el menú
mostrar_menu()
