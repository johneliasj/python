# > ESTRUTURAS CONDICIONAIS

"""
    Imagine que você queira imprimir "Aprovado", caso o estudante tenha média >= 7, e reprovado se < 7.
"""

media = 9
presenca = 70
aprovado = bool
invalido = bool


if media < 0 or media > 10 or presenca > 100 or presenca < 0:
    invalido = True
elif presenca < 70:
    aprovado = False
elif media < 5:
    aprovado = False
elif media >= 7:
    aprovado = True

    

if invalido == True:
    print(" Dados inválidos.")
elif aprovado == True:
    print("Aprovado.")
elif aprovado == False:
    print("Reprovado.")
else:
    print("Recuperação")

"""
idade = 17

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

nota = float(input("Qual foi a sua média de 0 a 10: "))
if nota < 0 or nota > 10:
    print("Nota Inválida")
elif nota < 5:
    print("Reprovado")
elif nota < 7:
    print("Recuperação.")
else:
    print("Aprovado.")

"""