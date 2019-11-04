import os
os.system("cls")

I = ["Quisqueya = s/ 21.50","Sol = s/ 22.20","Pacasmayo = s/ 24.00"]
II = ["Andino = s/ 24.00"]
V = ["Pacasmayo = s/ 31.90"]
IP = ["Quisqueya = s/ 20.00", "Yura = s/ 20.60", "Andino = s/ 23.20"]
HS = ["Inka = s/ 22.80", "Andino = s/ 24.20"]
GU = ["APU = s/ 20.50", "Pacasmayo = s/ 23.10"]
Cportland = [[I], [II], [V], [IP], [HS], [GU]]

arena_fina = ["arena (Unicon) = s/ 0.16xkg", "arena Hades = s/ 1.43xkg"]

piedra =["piedra chancada = s/ 0.15 solesxkg"]

barra_corrugada_1_2 = ["Aceros Arequipa = s/ 27.70", "SiderPeru = s/ 27.00"]
barra_corrugada_3_8 = ["Aceros Arequipa = s/ 15.50", "SiderPeru = s/ 15.50"]
barra_corrugada_8mm = ["Aceros Arequipa = s/ 11.20", "SiderPeru = s/ 11.20"]
acero = [[barra_corrugada_1_2], [barra_corrugada_3_8],[barra_corrugada_8mm]]

madera_viga = ["Maestro_2x3x16 = s/ 46.90", "Sodimac_2x4x16 = s/ 57.90"]
madera = [[madera_viga]]

listaP = [[Cportland], [arena_fina], [piedra], [acero], [madera]]

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
    #print("Escoja la opción del producto:")
    #Opción cemento
    if listaP[pos] == listaP[0]:
        print("Cemento Portland tipo I: 1","Cemento Portland tipo II: 2","Cemento Portland tipo V: 3",
        "Cemento Portland tipo IP: 4","Cemento Portland tipo HS: 5","Cemento Portland tipo GU: 6")
        c =  int(input("Ingrese la opción deseada:"))
        pos1 = 1 - c
        if Cportland[pos1] == Cportland[0]:
            print("Quisqueya = s/ 21.50","Sol = s/ 22.20","Pacasmayo = s/ 24.00")
            ce = int(input("Escoja la opción que desea:","Quisqueya: 1", "Sol: 2","Pacasmayo: 3"))
            ce1 = 1 - ce
            pres.append(I[ce1])


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Opcion acero
    elif listaP[pos] == listaP[3]:
        print("Barra Corrugada 1/2: 1", "Barra Corrugada 3/8: 2", "Barra Corrugada 8mm: 3")
        ac = int(input("Ingrese la opcion deseada"))
        pos4 = 1 - ac
        if acero[pos4] == acero[0]:
            print (acero)
            ace = int(input("Escoja la opción que desea:", ""))



