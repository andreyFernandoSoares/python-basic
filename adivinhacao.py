import random

def jogar():
    inicia_jogo()

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    total_tentativas = define_nivel()


    print("Você tem {} tentativas".format(total_tentativas))

    for rodada in range (1, total_tentativas + 1):

        print("")
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute_int = int(chute_str)

        if (chute_int < 1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute_int
        maior = numero_secreto > chute_int
        menor = numero_secreto < chute_int

        if (acertou):
            print("Você  e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Você errou! Seu chute foi menor que o numero secreto.")

            pontos_perdidos = abs(numero_secreto - chute_int) # 40 - 20 perde 20 pontos
            pontos = pontos - pontos_perdidos

    print("Fim do jogo.")

def inicia_jogo():
    print("")
    print("********************************")
    print("Bem vindo ao jogo de Advinhação")
    print("********************************")

def define_nivel():
    total_tentativas = 0
    print("Qual nivel de dificuldade?")
    print("{1} Facil")
    print("{2} Medio")
    print("{3} Dificil")
    print("Caso adicione outros numeros sera direcionado ao nivel dificil")

    nivel = int(input("Defina um nivel: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 3
    
    return total_tentativas

if (__name__ == "__main__"):
    jogar()