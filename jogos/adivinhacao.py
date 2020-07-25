import random

def jogar():
    print("******************************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("******************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil\n"
          "(2) Médio\n"
          "(3)Difícil\n")
    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Você escolheu o número: ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número enter 1 e 100")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou O seu chute foi maior do que o numero secreto \n")
            elif(menor):
                print("Você errou O seu chute foi menor do que o numero secreto \n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
