'''Escriba una función que compare una tabla
de especificaciones de hardware de 2 equipos
de cómputo y determine cuál de los 2 tiene mejor capacidad.
'''

def show_menu():
    print(" Comparación de hardware ".center(50, "="))
    print()
    print(" 1. Computadora")
    print(" 2. Memoria RAM")
    print(" 3. Smartphone")
    print(" 4. Fuente de poder")
    print()
    print("=".center(50, "="))

def comparar():
    show_menu()
    eleccion = int(input("Que quieres comparar?"))
    print("=".center(50, "="))
    if (eleccion == 1):
        comparar_pc()
    elif (eleccion == 2):
        comparar_ram()
    elif (eleccion == 3):
        comparar_smartphone()
    elif (eleccion == 4):
        print("poder")

def comparar_pc():
    print("Primer PC".center(50, "="))
    procesador = int(input("Procesador: (GHZ)"))
    print("=".center(50, "="))
    ram = int(input("RAM (GB):"))
    print("=".center(50, "="))
    tarjeta = int(input("Tarjeta gráfica (GB):"))
    print("=".center(50, "="))
    print("Segunda PC".center(50, "="))
    print("=".center(50, "="))
    procesador2 = int(input("Procesador: (GHZ)"))
    print("=".center(50, "="))
    ram2 = int(input("RAM (GB):"))
    print("=".center(50, "="))
    tarjeta2 = int(input("Tarjeta gráfica (GB):"))
    print("=".center(50, "="))
    win = 0
    win2 = 0
    if (max(procesador, procesador2) == procesador):
        win += 1
    elif (max(procesador, procesador2) == procesador2):
        win2 += 1
    if (max(ram, ram2) == ram):
        win += 1
    elif (max(ram, ram2) == ram2):
        win2 += 1
    if (max(tarjeta, tarjeta2) == tarjeta):
        win += 1
    elif (max(tarjeta, tarjeta2) == tarjeta2):
        win2 += 1

    if (max(win, win2) == win):
        print("La primer pc es mejor")
    elif (max(win, win2) == win2):
        print("La segunda pc es mejor")
    else:
        print("Tienen similares caracteristicas")

def comparar_ram():
    print("Primera RAM".center(50, "="))
    print("=".center(50, "="))
    tamanio = int(input("Tamaño de memoria: (GB)"))
    print("=".center(50, "="))
    tipo = str(input("Tipo de memoria: (DDR3, DDR4)"))
    print("=".center(50, "="))
    speed = int(input("Velocidad: (MHz):"))
    print("=".center(50, "="))
    print("Segunda RAM".center(50, "="))
    print("=".center(50, "="))
    tamanio2 = int(input("Tamaño de memoria: (GB)"))
    print("=".center(50, "="))
    tipo2 = str(input("Tipo de memoria: (DDR3, DDR4)"))
    print("=".center(50, "="))
    speed2 = int(input("Velocidad: (MHz):"))
    print("=".center(50, "="))
    win = 0
    win2 = 0
    if (max(tamanio, tamanio2) == tamanio):
        win += 1
    elif (max(tamanio, tamanio2) == tamanio2):
        win2 += 1
    if (tipo.lower() == 'ddr4' and tipo2.lower() == 'ddr2'):
        win += 1
    elif (tipo2.lower() == 'ddr4' and tipo.lower() == 'ddr2'):
        win2 += 1
    elif (tipo2.lower() == 'ddr3' and tipo.lower() == 'ddr2'):
        win2 += 1
    elif (tipo.lower() == 'ddr3' and tipo2.lower() == 'ddr2'):
        win += 1
    elif (tipo2.lower() == 'ddr4' and tipo.lower() == 'ddr3'):
        win2 += 1
    elif (tipo.lower() == 'ddr4' and tipo2.lower() == 'ddr3'):
        win += 1
    else:
        win += 0
        win2 += 0
    if (max(speed, speed2) == speed):
        win += 1
    elif (max(speed, speed2) == speed2):
        win2 += 1

    if (max(win, win2) == win):
        print("La primera RAM es mejor")
    elif (max(win, win2) == win2):
        print("La segunda RAM es mejor")
    else:
        print("Tienen similares caracteristicas")

def comparar_smartphone():
    print("Ingresar primer smartphone")
    print("=".center(50, "="))
    procesador = int(input("Procesador: (GHZ)"))
    print("=".center(50, "="))
    ram = int(input("RAM (GB):"))
    print("=".center(50, "="))
    nucleos = int(input("Cantidad de nucleos: "))
    print("=".center(50, "="))
    camara = int(input("Camára: (PX)"))
    print("=".center(50, "="))
    print("Ingresar segundo smartphone")
    print("=".center(50, "="))
    procesador2 = int(input("Procesador: (GHZ)"))
    print("=".center(50, "="))
    ram2 = int(input("RAM (GB):"))
    print("=".center(50, "="))
    nucleos2 = int(input("Cantidad de nucleos: "))
    print("=".center(50, "="))
    camara2 = int(input("Camára: (PX)"))
    print("=".center(50, "="))
    win = 0
    win2 = 0
    if (max(procesador, procesador2) == procesador):
        win += 1
    elif (max(procesador, procesador2) == procesador2):
        win2 += 1
    if (max(ram, ram2) == ram):
        win += 1
    elif (max(ram, ram2) == ram2):
        win2 += 1
    if (max(nucleos, nucleos2) == nucleos):
        win += 1
    elif (max(nucleos, nucleos2) == nucleos2):
        win2 += 1
    if (max(camara, camara2) == camara):
        win += 1
    elif (max(camara, camara2) == camara2):
        win2 += 1

    if (max(win, win2) == win):
        print("El primer smartphone es mejor")
    elif (max(win, win2) == win2):
        print("El segundo smartphone es mejor")
    else:
        print("Tienen similares caracteristicas")

comparar()