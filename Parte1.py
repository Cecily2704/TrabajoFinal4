import os
os.system("cls")

#Cportland = [[I],[II],[V], [IP], [HS], [GU]]
#listaP = [[Cportland], arena, piedra, [acero], madera]
#I = ["quisqueya = s/ 21.50","sol = s/ 22.20","pacasmayo = s/ 24.00"]
#II = ["Andino = s/ 24.00"]
#V = ["Pacasmayo = s/ 31.90"]
#IP = ["Quisqueya = s/ 20.00", "Yura = s/ 20.60", "Andino = s/ 23.20"]
#HS = ["Inka = s/ 22.80", "Andino = s/ 24.20"]
#GU = ["APU = s/ 20.50", "Pacasmayo = s/ 23.10"]

#acero = [[barra_corrugada_1/2], [barra_corrugada_3/8],[barra_corrugada_8mm]]
#barra_corrugada_1/2 = ["Aceros Arequipa = s/ 27.70", SiderPeru = s/ 27.00]
#barra_corrugada_3/8 = ["Aceros Arequipa = s/ 15.50", "SiderPeru = s/ 15.50"]
#barra_corrugada_8mm = ["Aceros Arequipa = s/ 11.20", SiderPeru = s/ 11.20]

#madera = 

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


    

