import os
import time
import random
import json
import csv

os.system("cls")

modelos = [ "rio", "forte", "optima", "stinger", "soul", "seltos", "sportage", "sorento", "felluride", "carnival"]
modeloprecio = []

def error():
    os.system("cls")
    print("Ingrese una opcion valida")
    time.sleep(2)

def asignarprecios(modelos):
    for modelo in modelos:
        precioModelo = random.choice(range(7000000,12500000,100000))
        auto = {
            "modelo": modelo,
            "precio": precioModelo
        }
        modeloprecio.append(auto)
    guardar_json (" modeloprecio.json ", modeloprecio)
    os.system("cls")
    print("Se crearon los precios de manera exitosa")
    time.sleep(2)

def guardar_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data , file , indent=4 , ensure_ascii=False)

def estadisticas(modeloprecio):
    mayorprecio=0
    menorprecio=0
    promedioprecios=0
    mediageometrica=0
    sumaprecios=0
    multiplicacionprecios=1
    precios=[]
    for precio in modeloprecio:
        precios.append(precio["precio"])
    cantidadprecio=len(precios)
    mayorprecio=max(precios)
    menorprecio=min(precios)
    for precio in precios:
        sumaprecios += precio
        multiplicacionprecios *= precio
    promedioprecios= round(sumaprecios / cantidadprecio)
    mediageometrica = round(multiplicacionprecios ** (1 / cantidadprecio))

    print(f"Mayor precio: {mayorprecio}")
    print(f"Menor precio: {menorprecio}")
    print(f"Promedio precio: {promedioprecios}")
    print(f"Media geometrica de los precios: {mediageometrica}")

def report(modeloprecio):
    iva=0
    descuento=0
    preciofinal=0
    sumaprecio=0
    reportcsv=[]
    for modelo in modeloprecio:
        iva=round(modelo["precio"]*0.19)
        descuento=round(modelo["precio"]*0.07)
        preciofinal=modelo["precio"]+iva-descuento
        modelopreciofinal={
            "modelo": modelo["modelo"],
            "precio": modelo["precio"],
            "iva": iva,
            "descuento": descuento,
            "preciofinal": preciofinal
        }
    reportcsv.append(modelopreciofinal)
    guardar_csv("reportcsv.csv", reportcsv)

def guardar_csv(file_path, data):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow("modelo", "precio", "iva", "descuento", "preciofinal")
        for modelo in data:
            writer.writerow([modelo["modelo"], modelo["precio"], modelo["iva"], modelo["descuento"], modelo["preciofinal"]])

def clasificar(modeloprecio):
    mayorprecio=[]
    entreprecio=[]
    menorprecio=[]
    for modelo in modeloprecio:
        if modelo["precio"] < 9000000:
            menorprecio.append(modelo)
        elif modelo["precio"] >= 9000000 and modelo["precio"] <= 11000000:
            entreprecio.append(modelo)
        elif modelo["precio"] > 11000000:
            mayorprecio.append(modelo)
    print("")
    print("-----Menor a 9000000-----")
    print(f"MODELO  |  PRECIO")
    for modelo in menorprecio:
        print(f'{modelo["modelo"]}  |  {modelo["precio"]}')   
    print("")
    print("-----Mayor a 9000000 y Menor a 11000000-----")
    print(f"MODELO  |  PRECIO")
    for modelo in entreprecio:
        print(f'{modelo["modelo"]}  |  {modelo["precio"]}')
    print("")
    print("-----Mayor a 11000000-----")
    print(f"MODELO  |  PRECIO")
    for modelo in mayorprecio:
        print(f'{modelo["modelo"]}  |  {modelo["precio"]}')


def menu():
    print("-----EMPRESA DE AUTOS-----")
    print("[1] Asignar precios aleatiorios")
    print("[2] Clasificar precios")
    print("[3] Ver estadisticas")
    print("[4] Reporte de precios")
    print("[5] Salir del programa")

def main():
    #Funcion Principal
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
            if opcmenu==1:
                asignarprecios(modelos)
            elif opcmenu==2:
                if len(modeloprecio) == 0:
                    os.system("cls")
                    print("No ha asignado ningun precio")
                    time.sleep(2)
                else:
                    clasificar(modeloprecio)
            elif opcmenu==3:
                if len(modeloprecio) == 0:
                    os.system("cls")
                    print("No ha asignado ningun precio")
                    time.sleep(2)
                else:
                    estadisticas(modeloprecio)
            elif opcmenu ==4:
                if len(modeloprecio) == 0:
                    os.system("cls")
                    print("No ha asignado ningun precio")
                    time.sleep(2)
                else:
                    report(modeloprecio)
            elif opcmenu == 5:
                os.system("cls")
                print("Cerrando programa...")
                print("Programa hecho por Benjamin Mancilla")
                print("11-07-2024")
                time.sleep(2)
                break

if __name__ == "__main__":
    main()