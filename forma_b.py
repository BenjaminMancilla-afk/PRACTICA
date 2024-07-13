import os
import time
os.system("cls")

# declarar todas las variables de la boleta
# primero los contadores de los productos
cant_menores = 0
cant_adultos = 0
cant_adultos_mayores = 0
# luego los valores de la boleta misma
subtotal = 0
descuento = 0
total = 0

menu_entrada = True
while menu_entrada:
    # alt 92 \
    os.system("cls")
    print("== BUENA VENTURA ==")
    print("1. Menores \t| De 5 a 12 años \t| $2.500")
    print("2. Adultos \t| De 13 a 64 año \t| $5.000")
    print("3. Adulto Mayor | Desde 65 y mas \t| $1.000")
    print("4. Pagar")
    print("5. Anular pedido")
    opcion_entrada = 0

    try:
        opcion_entrada = int(input("Ingresa la opción disponible >> "))
    except:
        print("La opción debe ser numérica")
    
    if opcion_entrada < 1 or opcion_entrada > 5:
        print("La opción fuera de rango, intente nuevamente")
        time.sleep(2)
        os.system("cls")
    else:
        if opcion_entrada == 1:
            try:
                cant_menores += int(input("Ingrese la cantidad de entradas MENORES que necesita >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_entrada == 2:
            try:
                cant_adultos += int(input("Ingrese la cantidad de entradas ADULTOS que necesita >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_entrada == 3:
            try:
                cant_adultos_mayores += int(input("Ingrese la cantidad de entradas ADULTOS MAYORES que necesita >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_entrada == 4:

            if cant_menores == 0 and cant_adultos == 0 and cant_adultos_mayores == 0:
                print("No puedes pagar si no compraste nada")
                time.sleep(2)
                os.system("cls")
            else:
                es_viernes = 0
                try:
                    es_viernes = int(input("Es viernes? 1. SI 2. NO >> "))
                except:
                    print("La opción debe ser numérica")

                if es_viernes == 1:
                    descuento += cant_menores * 2500 * 0.05
                    descuento += cant_adultos * 5000 * 0.1

                print("=== ENTRADAS ===")
                print("---------------------------------------------------")

                if cant_menores > 0:
                    print(f"{cant_menores} entradas Menores \t\t${cant_menores*2500}")
                if cant_adultos > 0:
                    print(f"{cant_adultos} entradas Adultos \t\t${cant_adultos*5000}")
                if cant_adultos_mayores > 0:
                    print(f"{cant_adultos_mayores} entradas Adultos Mayores \t${cant_adultos_mayores*1000}")
                
                print("---------------------------------------------------")
                
                subtotal = cant_menores*2500 + cant_adultos*5000 + cant_adultos_mayores*1000
                print(f"Subtotal \t\t\t ${subtotal}")
                if descuento > 0:
                    print(f"Descuento \t\t\t ${descuento}")
                print("---------------------------------------------------")
                total = subtotal-descuento
                print(f"Total a pagar \t\t\t ${total}")

                input()

        elif opcion_entrada == 5:
            print("PEDIDO ANULADO")
            menu_entrada = False