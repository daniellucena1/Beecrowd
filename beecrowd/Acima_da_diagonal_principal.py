tipo = input()
soma = 0

matriz = [0] * 12

for i in range(12):
    matriz[i] = [0] * 12

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

n = 0

for i in range(11):
    n += 1
    for j in range(n,12):
        soma += matriz[i][j]

if tipo == "S":
    print("{:.1f}".format(soma))
elif tipo == "M":
    media = soma/66
    print("{:.1f}".format(media))