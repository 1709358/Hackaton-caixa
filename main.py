from functions import *
import pandas as pd
from BD import BD
from Mapa import Mapa
from Ruta import Ruta
from Nodo import Nodo

bd = BD()
bd.conexion()

mapa = Mapa(6)

def menu():
    print("1. Visualizar ruta ")
    print("2. Agregar un pueblo")
    print("3. Salir")

def subMenu1():
    print("¿Qué ruta quieres visualizar?")

def abrir(nomFichero):
    # Abre el fichero en modo lectura
    with open(nomFichero, 'r') as fichero:
        # Lee el contenido del fichero
        contenido = fichero.read()

    # Imprime el contenido del fichero
    print(contenido)

while True:
    menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        subMenu1()
        opcion1 = input()
        abrir(opcion1)
    elif opcion == "2":
        print("Has elegido la opción 2.")
    elif opcion == "3":
        print("Has elegido salir. Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
