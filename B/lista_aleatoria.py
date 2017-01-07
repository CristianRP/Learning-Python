#!/usr/bin/env python3
# -*- coding:utf8 -*-

'''
Escriba una funcion que ordene aleatoriamente
una lista de reproduccion sin repeticion
'''

import struct
import time

lista_reproduccion = {1:'Let Her Go', 2:'Treasure',3:'The Lazy Song',
                      4:'I Want To Break Free', 5:'Bohemian Rhapsody'}

def shuffle_play(lista_reproduccion):
    for i in [randint(1, len(lista_reproduccion)) for _ in range(5)]:
        print(lista_reproduccion[i])

def lastbit(f):
    return struct.pack('!f', f)[-1] & 1

def getrandbits(k):
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= lastbit(time.clock())
    return result

def randint(a, b):
    return a + randbelow(b - a + 1)

def randbelow(n):
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    r = getrandbits(k)
    while r >= n:
        r = getrandbits(k)
    return r

def show_menu():
    print("  Bienvenido a Sfotipy  ".center(100,"="))
    print("Mi lista de reproduccion: ")
    for i in lista_reproduccion:
        print("\t" + lista_reproduccion[i])
    mix = str(input("Suffle play? (yes/no)"))
    while mix != 'no':
        print("Generando reproducción aleatoria...")
        time.sleep(1)
        print(shuffle_play(lista_reproduccion))
        mix = str(input("Generar otra lista aleatoria? si/no"))

show_menu()