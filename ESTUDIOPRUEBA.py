import os
import time
os.system("cls")

cantidadCuranto=0
cantidadMariscal=0
cantidadChupe=0
cantidadEmpanadas=0
cantidadPisco=0
cantidadBebidas=0
cantidadJugos=0

menu1=True

while menu1:
    print(f"")
    print(f'')
    print(f'Seleccione una opción:')
    print(f'[1] Ingresar Platos y Bebidas')
    print(f'[2] Anular Compra')
    print(f'[3] Pagar')
    print(f'[4] Salir')
    try:
        opc1=int(input('--->>>'))
        if opc1 == 1:

            menu2=True
            while menu2:
                print(f'')
                print(f'Seleccione sus platos y bebidas: ')
                print(f'Plato/Bedidas Valor [Cantidad]')
                print(f'[1] Curanto $20.000 [{cantidadCuranto}]')
                print(f'[2] Mariscal $12.000 [{cantidadMariscal}]')
                print(f'[3] Chupe Centolla $15.000 [{cantidadChupe}]')
                print(f'[4] Empanadas $3.000 [{cantidadEmpanadas}]')
                print(f'[5] Pisco Sour $5.000 [{cantidadPisco}]')
                print(f'[6] Bebidas Lata $3.000 [{cantidadBebidas}]')
                print(f'[7] Jugos Naturales $2.500 [{cantidadJugos}]')
                print(f'[8] Salir')
                try:
                    opc2=int(input('--->>>'))

                    if opc2 == 1:
                        cantidadCuranto=int(input('Cuantos platos quiere: '))
                    elif opc2 == 2:
                        cantidadMariscal=int(input('Cuantos platos quiere: '))
                    elif opc2 == 3:
                        cantidadChupe=int(input('Cuantos platos quiere: '))
                    elif opc2 == 4:
                        cantidadEmpanadas=int(input('Cuantos platos quiere: '))
                    elif opc2 == 5:
                        cantidadPisco=int(input('Cuantos vasos quiere: '))
                    elif opc2 == 6:
                        cantidadBebidas=int(input('Cuantos latas quiere: '))
                    elif opc2 == 7:
                        cantidadJugos=int(input('Cuantos jugos quiere: '))
                    elif opc2 == 8 :
                        menu2=False
                    else:
                        os.system('cls')
                        print('La opción ingresada no es valida.')
                except:
                    os.system('cls')
                    print(f'La opcion no es valida. Ingrese una correcta' )
        elif opc1 == 2:
            opcionAnular=int(input('Realmente quiere anular la compra, Ingrese [1] SI / [2] NO: '))
            if opcionAnular == 1:
                cantidadCuranto=0
                cantidadMariscal=0
                cantidadChupe=0
                cantidadEmpanadas=0
                cantidadPisco=0
                cantidadBebidas=0
                cantidadJugos=0
                os.system('cls')
                print('Compra anulada.')
                time.sleep(2)
                os.system("cls")
            elif opcionAnular == 2:
                print('Continue la venta.')
                time.sleep(2)
                os.system("cls")
        elif opc1 == 3:
            subtotal=(cantidadCuranto*20000+cantidadMariscal*12000+cantidadChupe*15000+cantidadEmpanadas*3000+cantidadPisco*5000+cantidadBebidas*3000+cantidadJugos*2500)
            if subtotal < 50000:
                descuento=0
                Total=subtotal-descuento
                print(f'')
                print(f'----------------------------------')
                print(f'Detalle de compra')
                print(f'----------------------------------')
                if cantidadCuranto > 0:
                    totalcuranto=cantidadCuranto*20000
                    print(f'- {cantidadCuranto} Curanto ${totalcuranto}')
                if cantidadMariscal > 0:
                    totalMariscal=cantidadMariscal*12000
                    print(f'- {cantidadMariscal} Mariscal ${totalMariscal}')
                if cantidadChupe > 0:
                    totalChupe=cantidadChupe*15000
                    print(f'- {cantidadChupe} Chupe Centolla ${totalChupe}')
                if cantidadEmpanadas > 0:
                    totalEmpanadas=cantidadEmpanadas*3000
                    print(f'- {cantidadEmpanadas} Empanadas ${totalEmpanadas}')
                if cantidadPisco > 0:
                    totalPisco=cantidadPisco*5000
                    print(f'- {cantidadPisco} Pisco ${totalPisco}')
                if cantidadBebidas > 0:
                    totalBebidas=cantidadBebidas*3000
                    print(f'- {cantidadBebidas} Bebidas ${totalBebidas}')
                if cantidadJugos > 0:
                    totalJugos=cantidadJugos*2500
                    print(f'- {cantidadJugos} Jugos ${totalJugos}')
                print(f'----------------------------------')
                print(f'Subtotal {subtotal}')
                print(f'Descuento {descuento}')
                print(f'----------------------------------')
                print(f'Total {Total}')
                time.sleep(2)
                os.system("cls")
            else:
                descuento=round(subtotal*0.1)
                Total=subtotal-descuento
                print(f'----------------------------------')
                print(f'Detalle de compra')
                print(f'----------------------------------')
                if cantidadCuranto > 0:
                    totalcuranto=cantidadCuranto*20000
                    print(f'- {cantidadCuranto} Curanto ${totalcuranto}')
                if cantidadMariscal > 0:
                    totalMariscal=cantidadMariscal*12000
                    print(f'- {cantidadMariscal} Mariscal ${totalMariscal}')
                if cantidadChupe > 0:
                    totalChupe=cantidadChupe*15000
                    print(f'- {cantidadChupe} Chupe Centolla ${totalChupe}')
                if cantidadEmpanadas > 0:
                    totalEmpanadas=cantidadEmpanadas*3000
                    print(f'- {cantidadEmpanadas} Empanadas ${totalEmpanadas}')
                if cantidadPisco > 0:
                    totalPisco=cantidadPisco*5000
                    print(f'- {cantidadPisco} Pisco ${totalPisco}')
                if cantidadBebidas > 0:
                    totalBebidas=cantidadBebidas*3000
                    print(f'- {cantidadBebidas} Bebidas ${totalBebidas}')
                if cantidadJugos > 0:
                    totalJugos=cantidadJugos*2500
                    print(f'- {cantidadJugos} Jugos ${totalJugos}')
                print(f'----------------------------------')
                print(f'Subtotal {subtotal}')
                print(f'Descuento {descuento}')
                print(f'----------------------------------')
                print(f'Total {Total}')
                time.sleep(2)
                os.system("cls")
        elif opc1 == 4:
            menu1=False
        else:
            os.system('cls')
            print('La opción ingresada no es valida.')
            time.sleep(2)
            os.system("cls")
    except:
            os.system('cls')
            print(f'La opcion no es valida. Ingrese una correcta' )
            time.sleep(2)
            os.system("cls")