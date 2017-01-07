#!/usr/bin/env python3
# -*- coding:utf8 -*-

'''
Escriba una función que liste los verbos
utilizados en una frase
'''

'''
Frase de ejemplo:
Hoy voy a abrir una caja, asi podré aconsejar a mis hijos sobre esto, cuanto una persona puede amar y aprender a la vez. Tengo que vender cada día para poder sustentar a la familia. Tenemos que luchar juntos y recordar siempre que no tenemos que permitir la derrota
'''

lista_verbos = ['abrir', 'acabar', 'aconsejar', 'amar', 'apoyar', 'aprender', 'ayudar',
 'bailar', 'beber', 'caer' 'cambiar','cantar','cerrar', 'cocinar', 'comenzar',  'vender',
 'venir', 'ver', 'viajar', 'visitar', 'vivir', 'volver', 'volverse','preparar', 'prometer',
 'pulsar', 'quedarse', 'quemar', 'querer', 'recibir', 'salir', 'saltar', 'sentar', 'sentir',
 'ser', 'sonreír', 'tener', 'trabajar', 'traer', 'tratar', 'usar','intentar','ir', 'jugar',
 'lanzar', 'lavar', 'leer', 'limpiar', 'llamar', 'llegar', 'llenar', 'llorar', 'luchar'
 'mandar', 'mejorar', 'mentir', 'mirar', 'morir', 'comer', 'comparar' 'comprar', 'conducir',
 'contar', 'continuar', 'correr','cortar', 'costar','creer','dar','reconocer','recordar'
'repetir','responder','reír', 'saber', 'sacar', 'terminar', 'tirar', 'tocar','permitir',
'poder','poner','preferir','preguntar','explicar','ganar','gritar','hablar','hacer',
'mostrar','mover','necesitar','ocurrir','odiar','ofrecer','olvidar','oír','pagar','pensar',
'perder', 'perdonar']

def listar_verbos():
    print("Listado de verbos en un frase".center(100, "="))
    op = str(input("Quieres ingresar una frase? (Verbos en tiempo presente) (si/no)"))
    print("=".center(100,"="))
    while op != 'no':
        oracion = str(input("Ingresa la frase:"))
        for i in lista_verbos:
            if i in oracion:
                print("\t" + i)

listar_verbos()