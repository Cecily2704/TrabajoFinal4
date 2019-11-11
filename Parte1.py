import os
os.system("cls")

#Se colocó el precio de las marcas de cada tipo de cemento, para realizar el presupuesto parcial de cemento.
I1 = [21.50, 22.20, 24.00] 
II1 = 24.00  
V1 = 31.90  
IP1 = [20.00, 20.60, 23.20] 
HS1 = [22.80, 24.20]
GU1 = [20.50, 23.10]
#Se colocó las diferentes marcas de cada tipo de cemento con su precio por una bolsa de 42.5kg, 
# para que el usuario pueda elegir la más conveniente.
I = ["Opción 1: Quisqueya = s/ 21.50","Opción 2: Sol = s/ 22.20","Opción 3: Pacasmayo = s/ 24.00"]
II = ["Andino = s/ 24.00"]
V = ["Pacasmayo = s/ 31.90"]
IP = ["Opción 1: Quisqueya = s/ 20.00", "Opción 2: Yura = s/ 20.60", "Opción 3: Andino = s/ 23.20"]
HS = ["Opción 1: Inka = s/ 22.80", "Opción 2: Andino = s/ 24.20"]
GU = ["Opción 1: APU = s/ 20.50", "Opción 2: Pacasmayo = s/ 23.10"]
#Se colocó este arreglo para organizar los tipos de cemento
Cportland = [[I], [II], [V], [IP], [HS], [GU]]
#Se colocó los tipos de cemento con un número respectivo,  para que el usuario pueda elegir la opción que desea.
tiposc = ["Cemento Portland tipo I: 1","Cemento Portland tipo II: 2","Cemento Portland tipo V: 3",
        "Cemento Portland tipo IP: 4","Cemento Portland tipo HS: 5","Cemento Portland tipo GU: 6"]

arena_fina_A = [0.16, 1.43]
arena_fina = ["Opción 1: Arena (Unicon) = s/ 0.16xkg", "Opción 2: Arena Hades = s/ 1.43xkg"]

piedra1 = 0.15
piedra =["Piedra chancada = s/ 0.15xkg"]

barra_corrugada_1_2_A = [27.70, 27.00]
barra_corrugada_3_8_B = [15.50, 15.50]
barra_corrugada_8mm_C = [11.20, 11.20]
barra_corrugada_1_2 = ["Opción 1: Aceros Arequipa = s/ 27.70", "Opción 2: SiderPeru = s/ 27.00"]
barra_corrugada_3_8 = ["Opción 1: Aceros Arequipa = s/ 15.50", "Opción 2: SiderPeru = s/ 15.50"]
barra_corrugada_8mm = ["Opción 1: Aceros Arequipa = s/ 11.20", "Opción 2: SiderPeru = s/ 11.20"]
acero = [[barra_corrugada_1_2], [barra_corrugada_3_8],[barra_corrugada_8mm]]
tiposac = ["Barra corrugada 1/2 (0.994 kg/m): 1", "Barra corrugada 3/8 (0.560 kg/m): 2", "Barra Corrugada 8mm (0.395 kg/m): 3"]

#Se colocó el precio de la madera por empresa, para realizar el presupuesto parcial de la madera.
madera1 =[46.90, 57.90]
#Se colocó las diferentes empresas que vendene madera con su precio por 16ft, para que el usuario pueda elegir la más conveniente.
madera = ["Opción 1: Maestro_2x3x16 = s/ 46.90", "Opción 2: Sodimac_2x4x16 = s/ 57.90"]

#Se colocó este arreglo para organizar las opciones de productos
listaP = [[Cportland], [arena_fina], [piedra], [acero], [madera]]
#Se colocó los productos con un número respectivo,  para que el usuario pueda elegir la opción que desea.
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
    nombre = int(input("Ingrese el número correspondiente al producto " + num + ": "))
    pos = nombre - 1 

#Proceso
    #Opción cemento, se hizo un presupuesto parcial para cada tipo de cemento
    if listaP[pos] == listaP[0]:
        cantidad_producto1 = int(input("Ingrese la cantidad de bolsas de cemento deseadas para el producto " + num + ": "))
        for tip in tiposc:
            print("Opción",tip)
        c =  int(input("Ingrese la opción de cemento que desea: "))
        pos1 = c - 1
        if Cportland[pos1] == Cportland[0]:
            for cem in I:
                print(cem)
            ce = int(input("Escoja la opción que desea: "))
            ce1 = ce - 1
            pres.append(I[ce1])
            presuce = cantidad_producto1*I1[ce1]
            print("El presupuesto de cemento sería ",presuce, "soles.")
        elif Cportland[pos1] == Cportland[1]:
            for cem in II:
                print(cem)
            pres.append(II[0])
            presuce = cantidad_producto1*II1
            print("El presupuesto de cemento sería ",presuce, "soles.")   
        elif Cportland[pos1] == Cportland[2]:
            for cem in V:
                print(cem)
            pres.append(V[0])
            presuce = cantidad_producto1*V1
            print("El presupuesto de cemento sería ", presuce, "soles.") 
        elif Cportland[pos1] == Cportland[3]:
            for cem in IP:
                print(cem)
            cem = int(input("Escoja la opción que desea: "))
            cem1 = cem - 1
            pres.append(IP[cem1])
            presuce = cantidad_producto1*IP1[cem1]
            print("El presupuesto de cemento sería ", presuce, "soles.") 
        elif Cportland[pos1] == Cportland[4]:
            for cem in HS:
                print(cem)
            ceme = int(input("Escoja la opción que desea: "))
            ceme1 = ceme - 1
            pres.append(HS[ceme1])
            presuce = cantidad_producto1*HS1[ceme1]
            print("El presupuesto de cemento sería ", presuce, "soles.") 
        else:
            for cem in GU:
                print(cem)
            ce_me = int(input("Escoja la opción que desea: "))
            ce_me1 = ce_me - 1
            pres.append(GU[ce_me1])
            presuce = cantidad_producto1*GU1[ce_me1]
            print("El presupuesto de cemento sería ", presuce, "soles.") 
    else:
        presuce = 0


    # Opcion arena fina:
    if listaP[pos] == listaP[1]:
        cantidad_producto2 = int(input("Inrgese la cantidad de kg que necesita: "))
        for arena in arena_fina:
            print(arena)
        arefin = int(input("ingrese la opcion deseada: ")) 
        arefin1 = arefin - 1
        pres.append(arena_fina[arefin1])
        presuare = cantidad_producto2 * arena_fina_A[arefin1]
        print("El presupuesto de la arena fina sería ", presuare, "soles.")
    else:
        presuare = 0
       
    
    # Opcion piedra
    if listaP[pos] == listaP[2]:
        cantidad_producto3 = int(input("Ingrese la cantidad de kg que necesita: "))
        for piedras in piedra:
            print(piedras)
        pres.append(piedra[0])
        presupiedra = cantidad_producto3 * piedra1
        print("El presupuesto de la piedra chancada sería ", presupiedra, "soles.")
    else:
        presupiedra = 0

    
    #Opcion acero
    if listaP[pos] == listaP[3]:
        cantidad_producto4 = int(input("Ingrese la cantidad de barras de 9m de acero deseadas para el producto " + num + ": "))
        for tip in tiposac:
            print ("Opción", tip)       
        ac = int(input("Ingrese la opción de acero deseada: "))
        pos4 = 1 - ac
        if acero[pos4] == acero[0]:
            for ace in barra_corrugada_1_2: 
                print (ace)
            acer = int(input("Escoja la opción que desea: " ))
            acer1 = acer - 1
            pres.append(barra_corrugada_1_2[acer1])
            presu_acer = cantidad_producto4*barra_corrugada_1_2_A[acer1]
            print ("El presupuesto de acero sería", presu_acer, "soles.")
        elif acero[pos4] == acero [1]:
            for ace in barra_corrugada_3_8:
                print (ace)
            ac_er = int(input("Escoja la opción que desea: " ))
            ac_er1 = ac_er - 1
            pres.append(barra_corrugada_8mm[ac_er1])
            presu_acer = cantidad_producto4*barra_corrugada_3_8_B[ac_er1]
            print ("El presupuesto de acero sería", presu_acer, "soles.")
        else:
            for ace in barra_corrugada_8mm:
                print (ace)
            ace_ro = int(input("Escoja la opción que desea: "))
            ace_ro1 = ace_ro - 1
            pres.append(barra_corrugada_8mm[ace_ro1])
            presu_acer = cantidad_producto4*barra_corrugada_8mm_C[ace_ro1]
            print ("El presupuesto de acero sería", presu_acer, "soles.")
    else:
        presu_acer = 0

    #Opción madera, se hizo un presupuesto parcial para cada elección de madera
    if listaP[pos] == listaP[4]:
        cantidad_producto5 = int(input("Ingrese la cantidad de tablas de 16ft: "))
        for viga in madera:
            print(viga)
        ma = int(input("Escoja la opción que desea: "))
        ma1 = ma - 1
        pres.append(madera[ma1])
        presuma = cantidad_producto5 * madera1[ma1]
        print("El presupuesto de madera sería", presuma, "soles.")
    else:
        presuma = 0
# Salida
presupuesto_final = 0
presupuesto_final = presuce + presu_acer + presuare + presupiedra + presuma
print("Usted escogió estas opciones ", pres)
print("El presupuesto final sería ", round(presupuesto_final,2), "soles.")