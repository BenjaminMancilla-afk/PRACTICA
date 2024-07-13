import os
import time
import json
import csv

os.system("cls")

def menu():
    print("Mantenedor libro")
    print("[1] Agregar Libro")
    print("[2] Editar Libro")
    print("[3] Eliminar Libro")
    print("[4] Buscar Libro")
    print("[5] Volver")
    opc1=int(input("Selecciona una Opcion:  "))
    return opc1

def secuencia():
    resultado=menu()
    if resultado == 1:
        agregar()

def agregar():
    titulo=input("Ingrese un titulo: ")
    autor=input("Ingrese un autor: ")
    categoria=input("Ingrese una categoria: ")
    ano=input("Ingrese el año de publicacion: ")
    diccionario={
            "titulo":titulo,
            "autor":autor,
            "categoria":categoria,
            "año":ano,
        }
    with open("libros.json","w") as file:
        json.dump([diccionario], file, indent=4)
    with open("libros.json","r") as file:
        datos_json=json.load(file)
    diccionario2={
        "titulo":titulo,
        "autor":autor,
        "categoria":categoria,
        "ano":ano,
    }
    with open("libros.json","w") as file:
        json.dump(diccionario2, file, indent=4)


if __name__ == "__main__":
    secuencia()






