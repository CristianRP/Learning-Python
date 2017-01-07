def votacion():
    voto = ''
    count_voto_candidate1 = 0
    count_voto_candidate2 = 0
    count_voto_nulo = 0
    while voto != 'salir':
        menu()
        voto = input("Por quien quieres votar?")
        if ("trump" in voto.lower()):
            count_voto_candidate1 += 1
        elif ("clinton" in voto.lower()):
            count_voto_candidate2 += 1
        elif ("salir" in voto.lower()):
            print("Gracias por votar!")
        else:
            count_voto_nulo += 1
    print("Candidato 1: {0}".format(count_voto_candidate1))
    print("Candidato 2: {0}".format(count_voto_candidate2))
    print("Votos nulos: {0}".format(count_voto_nulo))
    count_candidatos = max(count_voto_candidate1, count_voto_candidate2, count_voto_nulo)
    if (count_voto_candidate1 == count_voto_candidate1):
        print("El ganador es el candidato 1")
    elif (count_candidatos == count_voto_candidate2):
        print("El ganador es el candidato 2")
    else:
        print("La mayoria de votos fue nulo")

def menu():
    print("***---Candidatos---***")
    print("***-----Trump------***")
    print("***----Clinton-----***")
    print("Votaciones 2016")

votacion()