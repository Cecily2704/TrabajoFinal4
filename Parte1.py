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

arena_fina_A = [0.16, 1.43]
arena_fina = ["arena (Unicon) = s/ 0.16xkg", "arena Hades = s/ 1.43xkg"]

piedra1 = 0.15
piedra =["piedra chancada = s/ 0.15 solesxkg"]

barra_corrugada_1_2_A = [27.70, 27.00]
barra_corrugada_3_8_B = [15.50, 15.50]
barra_corrugada_8mm_C = [11.20, 11.20]
barra_corrugada_1_2 = ["Aceros Arequipa = s/ 27.70", "SiderPeru = s/ 27.00"]
barra_corrugada_3_8 = ["Aceros Arequipa = s/ 15.50", "SiderPeru = s/ 15.50"]
barra_corrugada_8mm = ["Aceros Arequipa = s/ 11.20", "SiderPeru = s/ 11.20"]
acero = [[barra_corrugada_1_2], [barra_corrugada_3_8],[barra_corrugada_8mm]]
tiposac = ["Barra corrugada 1/2 (0.994 kg/m): 1", "Barra corrugada 3/8 (0.560 kg/m): 2", "Barra Corrugada 8mm (0.395 kg/m): 3"]

madera = ["Maestro_2x3x16 = s/ 46.90", "Sodimac_2x4x16 = s/ 57.90"]

listaP = [[Cportland], [arena_fina], [piedra], [acero], [madera]]
productos = ["Cemento: 1", "Arena: 2", "Piedra: 3", "Acero: 4","Madera: 5"]

#Entrada
pres = []
while True:
    cantidad = int(input("¿Cuántos productos va utilizar?: "))
    if 0 < cantidad < 6:
        break 

for i in range(cantidad):
    num = str (i + 1)
    for pro in productos:
        print("Opción",pro)
    nombre = int(input("Ingrese el número correspondiente al producto " + num + ":"))
    pos = nombre - 1 

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


    # Opcion arena fina:
    if listaP[pos] == listaP[1]:
        cantidad_producto2 = int(input("Inrgese la cantidad de kg que necesita: "))
        for arena in arena_fina:
           print(arena)
           arefin = int(input("ingrese la opcion deseada: ")) 
           arefin1 = arefin - 1
           pres.append(arena_fina[arefin1])
           presuare = cantidad_producto2 * arena_fina_A[arefin1]
           print(presuare)
       
    
    # Opcion piedra
    if listaP[pos] == listaP[2]:
        cantidad_producto3 = int(input("Ingrese la cantidad de kg que necesita: "))
        for piedras in piedra:
            print(piedras)
            pres.append(piedra[0])
            presupiedra = cantidad_producto3 * piedra1
            print (presupiedra)

    
    #Opcion acero
    if listaP[pos] == listaP[3]:
        cantidad_producto4 = int(input("Ingrese la cantidad de barras de 9m de acero deseadas para el producto " + num + ":"))
        for tip in tiposac:
            print ("Opción", tip)       
        ac = int(input("Ingrese la opción de acero deseada:"))
        pos4 = 1 - ac
        if acero[pos4] == acero[0]:
            for ace in barra_corrugada_1_2: 
                print (ace)
            acer = int(input("Escoja la opción que desea:" ))
            acer1 = acer - 1
            pres.append(barra_corrugada_1_2[acer1])
            presu_acer = cantidad_producto4*barra_corrugada_1_2_A[acer1]
            print (presu_acer)
        elif acero[pos4] == acero [1]:
            for ace in barra_corrugada_3_8:
                print (ace)
            ac_er = int(input("Escoja la opción que desea:" ))
            ac_er1 = ac_er - 1
            pres.append(barra_corrugada_8mm[ac_er1])
            presu_acer = cantidad_producto4*barra_corrugada_3_8_B[ac_er1]
            print (presu_acer)
        else:
            for ace in barra_corrugada_8mm:
                print (ace)
            ace_ro = int(input("Escoja la opción que desea:" ))
            ace_ro1 = ace_ro - 1
            pres.append(barra_corrugada_8mm[ace_ro1])
            presu_acer = cantidad_producto4*barra_corrugada_8mm_C[ace_ro1]
            print (presu_acer)


