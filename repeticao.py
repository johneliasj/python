from random import randint

# ESTRUTURAS DE REPETIÇÃO

numero_sorteado = randint(0,20)
numero_escolhido = int(input("informe um inteiro entre 0 e 20: "))
i = 0

while i < 5:
    if numero_sorteado != numero_escolhido:
        print("Tente novamente, você errou: ")
        numero_escolhido = int(input("Informe um novo número:"))
        i = i + 1
    else:
        i = 5
    
if numero_escolhido == numero_sorteado:
    print("Parabéns você acertou.")
else:
    print("Não foi dessa vez")
