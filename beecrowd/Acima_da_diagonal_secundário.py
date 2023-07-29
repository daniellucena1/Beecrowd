operacao = input()
matriz = [0] * 12
soma = 0
media = 0

for i in range(12):
    matriz[i] = [0] * 12
for j in range(12):
    for k in range(12):
        matriz[j][k] = float(input())
if operacao == "S":
    n = 11
    for i in range(11):
        for j in range(n):
            soma += matriz[i][j]
        n -= 1
    print("{:.1f}".format(soma))
elif operacao == "M":
    n = 11
    for i in range(11):
        for j in range(n):
            media += matriz[i][j]
        n -= 1
    media /= 66
    print("{:.1f}".format(media))