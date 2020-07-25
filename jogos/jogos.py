import forca
import adivinhacao

def escolhe_jogo():
    print(20 * "*")
    print("Escolha o seu jogo!")
    print(20 * "*")

    print("(1)Forca \n"
          "(2)Adivinhação\n")

    jogo = int(input("Qual o jogo?"))

    if (jogo == 1):
        print("Jogando Forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()