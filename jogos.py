import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("Escolha seu jogo!")
    print("********************************")

    print("{1} Forca")
    print("{2} Advinhacao")

    jogo = int(input("Qual jogo? : "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()