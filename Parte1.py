import os
os.system("cls")

#Cportland = [I,II,V, IP, HS]
#listaP = [[Cportland], arena, piedra, acero, madera]

#piedra =[piedra chancada = 0.15 soles el kg]
#arena fina = [arena (Unicon) = 0.16 soles el kg, arena (Hades) = 1.43 soles el kg]


precio = []
while True:
    cantidad = int(input("¿Cuántos productos va utilizar?"))
    if 0 < cantidad < 6:
        break 

for i in range(cantidad):
    num = str (i + 1)
    print ("Cemento: 1", "Arena:2", "Piedra:3", "Acero:4","Madera:5")
    nombre = int(input("Ingrese el número correspondiente al producto" + num + ":"))
    metrado = input("Ingrese el metrado del producto " + num + ":")
    pos = 1 - nombre


    

