"""

for i in range(10):
    print(i)
    
for j in range(1,11):
    print(j)
    
for k in range(1, 11, 3):
    print(k)
    
"""
nota = [0,0,0,0]
soma = 0
    
for i in range (3):
        nota[i] = float(input(f"Informe a sua nota {i+1}: "))
        soma = nota[i]+soma

media = soma / (i+1)

for j in range (3):
    print(f"As notas foram: {nota[j]}")
print(f"A média foi: {media}")
    