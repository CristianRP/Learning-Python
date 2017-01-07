#!/usr/bin/env python3
# -*- coding:utf8 -*-

def draw_triangulo_pascal(n):
    list = [[1], [1, 1]]
    for i in range(1, n):
        values_linea = [1]
        for j in range(0, len(list[i]) - 1):
            values_linea.extend([list[i][j] + list[i][j + 1]])
        values_linea += [1]
        list.append(values_linea)
    return list

def show_menu():
    try:
        print("  Dibujar triangunlo de PASCAL  ".center(100, "="))
        n = int(input("Ingresa la cantidad de values_lineas para el triangulo de pascal: "))
        pascal = draw_triangulo_pascal(n)
        for x in pascal:
            print(str(x).center(50, " "))
    except:
        print("=".center(100, "="))
        print("Tienes que ingresar un número no un caracter".center(100, "="))
        print("=".center(100, "="))

show_menu()