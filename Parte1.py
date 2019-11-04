cantidad = int(input("¿cuantos productos va utilizar?"))

lista = []

precio = []

for i in range(cantidad):
    num = str (i + 1)
    nombre = input("ingrese nombre del producto " + num + ":")
    metrado = input("ingrese el metrado del producto " + num + ":")

    producto =[nombre, metrado]
    lista.append(producto)
