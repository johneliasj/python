# ESTRUTURA DE DADOS > LISTAS

# Criação de listas 
notas = [7.9, 8.10, 9.5]
lista = []                      # Vazia
lista = list                    # Criação
lista = [25, "HbO", False, 100, 50, 60]
lista2 = [100, 50, 589, 954, 60, 70]
lista_de_lista = [lista, notas, 142]

print(lista_de_lista[1], lista_de_lista[0])

print(lista_de_lista[-1])
print(lista[0:5])
print(lista[-5:5])
print(lista[0:5],2)

for i in range(len(lista)):
    for j in range(len(lista2)):
        print(lista[i], lista2[j])