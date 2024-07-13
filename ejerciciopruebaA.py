import os
import time
os.system("cls")

#variables
opc1=0
sectores=["centro", "colina", "industrias", "Santiago"]
nombres=""
direcciones=""
comuna=""
cant_5kg=0
cant_15kg=0
cant_45kg=0

#funciones
def erroringreso():
    os.system("cls")
    print("-------------------------")
    print("La opcion ingresada no es valida")
    print("-------------------------")
    time.sleep(2)


menu1=True
while menu1:
    print("-------------------------")
    print("Seleccione una opcion: ")
    print("[1] Registrar pedido")
    print("[2] Listar todos los pedidos")
    print("[3] Imprimir hoja de ruta")
    print("[4] Salir")
    print("-------------------------")

    try:
        opc1=int(input("--->>> "))
    except:
        erroringreso()

    if opc1 < 1 or opc1 > 4:
        erroringreso()
    elif opc1==1:
        print("-------------------------")
        print("Ingrese los datos del pedido: ")
        nombre=input("Ingrese el nombre del cliente:  ")
        direccion=input("Ingrese la direccion del cliente:  ")
        print("Selecione su sector: ")
        index = 1
        for sector in sectores:
            print(f"[{index}] {sector}")
            index +=1 
        indexsector=int(input("--->>>  "))
        comuna=sectores,{indexsector-1}
        print(comuna)
    elif opc1==2:
        print("")
    elif opc1==3:
        print("")
    elif opc1==4:
        os.system("cls")
        print("-------------------------")
        print("Saliste del menu")
        print("-------------------------")
        time.sleep(2)




