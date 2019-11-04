import os
os.system("cls")

while True:
    cantidad = int(input("¿Cuántos productos va utilizar?"))
    if 0 < cantidad < 6:
        break 

lista = []

precio = []

for i in range(cantidad):
    num = str (i + 1)
    nombre = input("Ingrese el nombre del producto " + num + ":")
    metrado = input("Ingrese el metrado del producto " + num + ":")

    producto =[nombre, metrado]
    lista.append(producto)
