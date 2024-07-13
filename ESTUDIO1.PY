import os
import time
import random
import json
import csv

destinos = ["París", "Londres", "Nueva York", "Tokio", "Sídney", "Roma", "Berlín", "Barcelona"]
viajes = []

def error():
    os.system("cls")
    print("Ingrese una opcion valida")
    time.sleep(2)

def asignarprecios(destinos):
    for destino in destinos:
        preciodestino= random.choice(range(100,100000,100))
        diccionarioviajes={
        "destino": destino,
        "precio": preciodestino
        }
        viajes.append(diccionarioviajes)
        guardar_json("viajes.json", viajes)
    os.system("cls")
    print("Se han asignado los precios correctamente")
    time.sleep(2)

def guardar_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def clasificar(viajes):
    menorprecio=[]
    entreprecio=[]
    mayorprecio=[]
    for viaje in viajes:
        if viaje["precio"] < 30000:
            menorprecio.append(viaje)
        elif viaje["precio"] >= 30000 and viaje["precio"] <= 70000:
            entreprecio.append(viaje)
        elif viaje["precio"] > 70000:
            mayorprecio.append(viaje)
    print("")
    print("MENORES DE 30000")
    print("--------------------")
    print("DESTINOS  |  PRECIOS")
    for viaje in menorprecio:
        print(f'{viaje["destino"]} | {viaje["precio"]}')
    print(f"TOTAL: {len(menorprecio)}")
    print("")
    print("MAYORES DE 30000 Y MENORES A 70000")
    print("--------------------")
    print("DESTINOS  |  PRECIOS")
    for viaje in entreprecio:
        print(f'{viaje["destino"]}|{viaje["precio"]}')
    print(f"TOTAL: {len(menorprecio)}")
    print("")
    print("MAYORES DE 70000")
    print("--------------------")
    print("DESTINOS  |  PRECIOS")
    for viaje in mayorprecio:
        print(f'{viaje["destino"]} | {viaje["precio"]}')
    print(f"TOTAL: {len(menorprecio)}")
    print("")
    time.sleep(2)

def menu():
    print("-----EMPRESA DE VIAJES-----")
    print("[1] Asignar precios aleatiorios")
    print("[2] Clasificar precios")
    print("[3] Ver estadisticas")
    print("[4] Reporte de precios")
    print("[5] Salir del programa")

def main():
    while True:
        opcmenu=0
        menu()
        try:
            opcmenu=int(input("Seleccione una opcion:  "))
        except:
            error()
        if opcmenu < 1 or opcmenu > 5:
            error()
        else:
            if opcmenu == 1:
                asignarprecios(destinos)
            elif opcmenu == 2:
                if len(viajes)==0:
                    os.system("cls")
                    print("No ha asignado ningun precio")
                    time.sleep(2)
                else:
                    clasificar(viajes)
            elif opcmenu == 3:
                if len(viajes)==0:
                    os.system("cls")
                    print("No ha asignado ningun precio")
                    time.sleep(2)
                else:
                    print("[3] Ver estadisticas")
            elif opcmenu == 4:
                if len(viajes)==0:
                    os.system("cls")
                    print("No ha asignado ningun precio")
                    time.sleep(2)
                else:
                    print("[4] Reporte de precios")
            elif opcmenu == 5:
               os.system("cls")
               print("Saliendo del programa")
               print("Creado por Benjamin Mancilla")
               print("12-07-24")
               time.sleep(2)
               break
            
if __name__=="__main__":
    main()