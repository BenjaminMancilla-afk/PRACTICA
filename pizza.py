import os
os.system("cls")

cantidadtradicional=0
cantidadpeperoni=0
cantidadallcarnes=0

MenuInicio=True
Menurapid=True

while MenuInicio:
    try:
        print(f"Bienvenidos a la pizzeria PizzaDuoc")
        print(f"[1] Elegir pizzas a comprar")
        print(f"[2] Pagar")
        print(f"[3] Anular compra")
        print(f"[4] Salir")
        opc1=int(input("--->>>"))
        if opc1 == 1:
                while Menurapid:
                    try:
                        print(f"Bienvenidos a la pizzeria PizzaDuoc")
                        print(f"[1] Pizza Tradicional $12000 [{cantidadtradicional}]")
                        print(f"[2] Pizza Peperoni $14000 [{cantidadpeperoni}]")
                        print(f"[3] Pizza All carnes $17000 [{cantidadallcarnes}]")
                        print(f"[4] Salir")
                        opc2=int(input("--->>>"))

                        if opc2 == 1:
                            cantidadtradicional=int(input("¿Cuantas pizzas quiere?"))
                        elif opc2 == 2:
                            cantidadpeperoni=int(input("¿Cuantas pizzas quiere?"))
                        elif opc2 == 3:
                            cantidadallcarnes=int(input("¿Cuantas pizzas quiere?"))
                        elif opc2 == 4:
                            Menurapid=False 
                        else:
                            print("Ingrese una opcion valida")        
                    except:
                        print("Eliga una de las opciónes correctas")
        elif opc1 == 3:
                anularcompra=int(input("¿Seguro que quiere anular la compra? [1]SI / [2]NO"))
                if anularcompra==1:
                    cantidadtradicional=0
                    cantidadpeperoni=0
                    cantidadallcarnes=0                       
        elif opc1 == 4:
            menu1=False

    except:
            print("Eliga una de las opciónes correctas")