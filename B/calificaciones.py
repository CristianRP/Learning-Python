#!/usr/bin/env python3
# -*- coding:utf8 -*-
'''
Escriba una función que traduzca una nota del sistmea
de calificacion guatemalateco (0-100) al sistema de
calificacion americano (basado en letras)
'''

def show_menu():
    print("Bienvenido al sitema de conversión de notas Americano".center(100, "*"))


def nota_americana():
    show_menu()
    op = str(input(("Quieres ingresar una nota? (si/no)")))
    while op != 'no':
        try:
            nota = int(input("Nota: "))
        except ValueError:
            print("Tienes que ingresar un número")
            nota = int(input("Nota: "))
        if (round(nota) >= 0 and nota <= 59):
            print('Que mal tienes una F')
        elif (nota >= 60 and nota <= 69):
            print('Que mal tienes una D')
        elif (round(nota) >= 70 and round(nota) <= 79):
            print('Puedes mejorar, tienes una C')
        elif (round(nota) >= 80 and round(nota) <= 89):
            print('Puedes mejorar, tienes una B')
        elif (round(nota) >= 90 and round(nota) <= 100):
            print('Felicidades tienes una A!')
        else:
            print('Nota no valida')
        print("*".center(100, "*"))
        op = str(input("Quieres ingresar otra nota?"))
    print("=".center(100, "="))
    print("Gracias por utilizar el conversor!".center(100, "*"))
    print("=".center(100, "="))

nota_americana()