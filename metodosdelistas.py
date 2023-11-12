# > MÉTODOS DE LISTAS

lista = [1, 2, 3, 4, 15, 26]
print(lista)

#append / adiciona no final
lista.append(30)
print("append: ", lista)


# insert / adiciona na posição escolhida
lista.insert(2, 5)
print("insert: ", lista)


# extend concatena duas lista, adcioando a segunda ao final da primeira
lista2 = [1, 2, 3]
lista.extend(lista2)
print("extend: ", lista)


# pop 
lista.pop()             #remove o último 
print("pop ", lista)
lista.pop(0)            #remove o argumento especificado
print("pop 0: ", lista)


# remove
lista.remove(3)         #remove o primeiro elemento igual ao especificado
print("remove: ", lista)


#coumt
print("count: ", lista.count(2))


#index 
print("index: ", lista.index(5))


#sort 
lista.sort()
print("sort: ", lista)

lista.sort(reverse=True)
print("sort reverse: ", lista)



# funções com listas

#len
print("len: ", len(lista))

#sum
print("sum: ", sum(lista))

#max
print("max: ", max(lista))

#min
print("min: ", min(lista))
