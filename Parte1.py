import os
os.system("cls")

I = ["Quisqueya = s/ 21.50","Sol = s/ 22.20","Pacasmayo = s/ 24.00"]
II = ["Andino = s/ 24.00"]
V = ["Pacasmayo = s/ 31.90"]
IP = ["Quisqueya = s/ 20.00", "Yura = s/ 20.60", "Andino = s/ 23.20"]
HS = ["Inka = s/ 22.80", "Andino = s/ 24.20"]
GU = ["APU = s/ 20.50", "Pacasmayo = s/ 23.10"]
Cportland = [[I], [II], [V], [IP], [HS], [GU]]
tiposc = ["Cemento Portland tipo I: 1","Cemento Portland tipo II: 2","Cemento Portland tipo V: 3",
        "Cemento Portland tipo IP: 4","Cemento Portland tipo HS: 5","Cemento Portland tipo GU: 6"]

arena_fina = ["arena (Unicon) = s/ 0.16xkg", "arena Hades = s/ 1.43xkg"]

piedra =["piedra chancada = s/ 0.15 solesxkg"]

barra_corrugada_1_2 = ["Aceros Arequipa = s/ 27.70", "SiderPeru = s/ 27.00"]
barra_corrugada_3_8 = ["Aceros Arequipa = s/ 15.50", "SiderPeru = s/ 15.50"]
barra_corrugada_8mm = ["Aceros Arequipa = s/ 11.20", "SiderPeru = s/ 11.20"]
acero = [[barra_corrugada_1_2], [barra_corrugada_3_8],[barra_corrugada_8mm]]

madera = ["Maestro_2x3x16 = s/ 46.90", "Sodimac_2x4x16 = s/ 57.90"]

listaP = [[Cportland], [arena_fina], [piedra], [acero], [madera]]
productos = ["Cemento: 1", "Arena: 2", "Piedra: 3", "Acero: 4","Madera: 5"]

#Entrada
pres = []
while True:
    cantidad = int(input("¿Cuántos productos va utilizar?"))
    if 0 < cantidad < 6:
        break 

for i in range(cantidad):
    num = str (i + 1)
    print ("Cemento: 1", "Arena: 2", "Piedra: 3", "Acero: 4","Madera: 5")
    nombre = int(input("Ingrese el número correspondiente al producto" + num + ":"))
    metrado = input("Ingrese el metrado del producto " + num + ":")
    pos = 1 - nombre

#Proceso
    #Opción cemento
    if listaP[pos] == listaP[0]:
        for tip in tiposc:
            print("Opción",tip)
        c =  int(input("Ingrese la opción de cemento que desea:"))
        pos1 = c - 1
        if Cportland[pos1] == Cportland[0]:
            for cem in I:
                print(cem)
            ce = int(input("Escoja la opción que desea si Quisqueya: 1 Sol: 2 Pacasmayo: 3 :"))
            ce1 = ce - 1
            pres.append(I[ce1])
        elif Cportland[pos1] == Cportland[1]:
            for cem in II:
                print(cem)
            pres.append(II[0])   
        elif Cportland[pos1] == Cportland[2]:
            for cem in V:
                print(cem)
            pres.append(V[0])
        elif Cportland[pos1] == Cportland[3]:
            for cem in IP:
                print(cem)
            cem = int(input("Escoja la opción que desea si opción Quisqueya: 1, opción Yura: 2 u opción Andino: 3 :"))
            cem1 = cem - 1
            pres.append(IP[cem1])
        elif Cportland[pos1] == Cportland[4]:
            for cem in HS:
                print(cem)
            ceme = int(input("Escoja la opción que desea si opción Inka: 1 u opción Andino: 2 :"))
            ceme1 = ceme - 1
            pres.append(HS[ceme1])
        else:
            for cem in GU:
                print(cem)
            ce_me = int(input("Escoja la opción que desea si opción APU: 1 u opción Pacasmayo: 2 :"))
            ce_me1 = ce_me - 1
            pres.append(GU[ce_me1])




