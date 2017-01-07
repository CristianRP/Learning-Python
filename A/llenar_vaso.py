'''Escriba un algoritmo
que “llene un vaso con agua"'''
import time


def llenar_vaso():
    print("=".center(100, "="))
    print("Si quiere llenar su vaso digite la capacidad en ml, si no digite 0".center(100, "="))
    print("=".center(100, "="))
    agua = 100
    op = str(input("Llenar vaso? (si/no)"))
    while op != 'no':
        cant_vaso = int(input("Capacidad del vaso: (ml)"))
        cant_vaso_f = cant_vaso
        count_cant_vaso = (100 * 1) / cant_vaso_f
        porcentaje_llenado = 1
        while agua != (agua - cant_vaso):
            print("Llenando vaso >>>>>>>>>>> {0}% Agua restante: {1}ml"
                  .format(count_cant_vaso,agua))
            time.sleep(1)
            agua -= 1
            cant_vaso -= 1
            porcentaje_llenado += 1
            count_cant_vaso = (100 * porcentaje_llenado) / cant_vaso_f
        print("Vaso llenado".center(100, "="))
        print("Agua restante: {0}".format(agua))
        agua = agua
        print()
        op = str(input("Quieres llenar otro vaso? (si/no)"))

llenar_vaso()