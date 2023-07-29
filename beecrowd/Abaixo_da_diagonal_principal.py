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
    for i in range(12):
        n = 1
        for j in range(n,12):
            if i == j or j < i:
                soma += 0
            else:
                soma += matriz[j][i]
                n += 1
    print("{:.1f}".format(soma))
elif operacao == "M":
    for i in range(12):
        n = 1
        for j in range(n,12):
            if i == j or j < i:
                media += 0
            else:
                media += matriz[j][i]
                n += 1
    media /= 66
    print("{:.1f}".format(media))