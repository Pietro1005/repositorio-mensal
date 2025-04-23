import random

numero_secreto = random.randint(1, 100)

tentativas = 0
acertou = False

print("Bem vindo ao jogo de advinhação")
print("Eu estou pensando em um numero de 1 a 100, tente advinhar!")

while not acertou:
    palpite = int(input("Qual é o seu palpite? "))

    tentativas += 1

    if palpite < numero_secreto:
        print("O numero escolhido é maior. Tente novamente!")
    elif palpite > numero_secreto:
        print("O número escolhido é menor. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
        acertou = True