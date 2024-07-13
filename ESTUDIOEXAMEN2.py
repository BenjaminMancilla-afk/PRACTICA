import os
import time
import json
import random
import csv

productos = ["Café Americano", "Té Chai","Croissant", "Jugo Naranja", "Panini de Pavo y Queso", "Pastel de Zanahoria", "Espresso Doble", "Batido de Frutas", "Muffin", "Ensalada", "Chocolate Caliente", "Tarta de Frambuesa", "Sándwich de Huevo", "Galletas de Avena", "Frappé de Caramelo"]
dulces = []

def asignarvalor(productos):
    for producto in productos:
        valorbruto=random.choice(range(3000,8000,100))
        utilidad = round(valorbruto*0.40)
        iva= round((valorbruto+utilidad)*0.19)
        valorventa = valorbruto+iva+utilidad
        diccionarioproductos={
        "nombre": producto,
        "valor_bruto": valorbruto,
        "utilidad": utilidad,
        "iva": iva,
        "valor_venta": valorventa
        }
        dulces.append(diccionarioproductos)
        guardar_json("dulces.json", dulces)
        os.system("cls")
    print("Ha ingresado los precios correctamente")
    time.sleep(1)

def guardar_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def clasificar(dulces):
    menorprecio=[]
    entreprecio=[]
    mayorprecio=[]
    for dulce in dulces:
        if dulce["valor_bruto"] < 5000:
            menorprecio.append(dulce)
        elif dulce["valor_bruto"] >= 5000 and dulce["valor_bruto"] <= 7000:
            entreprecio.append(dulce)
        elif dulce["valor_bruto"] > 7000:
            mayorprecio.append(dulce)
    print("")
    print(f"MENOR A 5000")
    print(f"TOTAL: {len(menorprecio)}")
    print("PRECIO |  PRECIO DE VENTA")
    for dulce in menorprecio:
        print(f'{dulce["nombre"]}  |  {dulce["valor_bruto"]}')
    print("")
    print(f"MAYOR A 5000 Y MENOR A 7000")
    print(f"TOTAL: {len(entreprecio)}")
    print("PRECIO |  PRECIO DE VENTA")
    for dulce in entreprecio:
        print(f'{dulce["nombre"]}  |  {dulce["valor_bruto"]}')
    print("")
    print(f"MAYOR A 7000")
    print(f"TOTAL: {len(mayorprecio)}")
    print("PRECIO |  PRECIO DE VENTA")
    for dulce in mayorprecio:
        print(f'{dulce["nombre"]}  |  {dulce["valor_bruto"]}')
    print("")

def estadisticas():
    menorprecio=0
    mayorprecio=0
    promedioprecios=0
    sumaprecio=0
    mediageometrica=0
    multiplicacionprecio=1
    precios=[]
    for precio in dulces:
        precios.append(precio["valor_venta"])
    cantidadprecios=len(precios)
    mayorprecio=max(precios)
    menorprecio=min(precios)
    for precio in precios:
        sumaprecio += precio
        multiplicacionprecio *= precio
    promedioprecios=round(sumaprecio / cantidadprecios)
    mediageometrica = round(multiplicacionprecio ** (1 / cantidadprecios))
    print(f"MAYOR PRECIO: {mayorprecio}")
    print(f"MENOR PRECIO: {menorprecio}")
    print(f"PROMEDIO PRECIO: {promedioprecios}")
    print(f"MEDIA GEOMETRICA: {mediageometrica}")

def error():
    os.system("cls")
    print("Ingrese una opcion correcta")
    time.sleep(2)

def menu():
    print("---Venta---")
    print("1. Asignar valores aleatorios ")
    print("2. Clasificar productos")
    print("3. Ver estadísticas. ")
    print("4. Reporte de productos ")
    print("5. Salir del programa")

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
            if opcmenu==1:
                asignarvalor(productos)
            elif opcmenu==2:
                if len(dulces) == 0:
                    os.system("cls")
                    print("No ha ingresado ningun precio")
                    time.sleep(2)
                else:
                    clasificar(dulces)
            elif opcmenu==3:
                estadisticas()
            elif opcmenu==4:
                print("")
            elif opcmenu==5:
                os.system("cls")
                print("Saliste del programa")
                print("Hecho por Benjamin Mancilla")
                print("11-07-24")
                time.sleep(2)
                break

if __name__=="__main__":
    main()
