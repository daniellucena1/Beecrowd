coluna = int(input())
c = input()
soma = 0
media = 0
matriz = [0] * 12
for i in range(12):
    matriz[i] = [0] * 12
for j in range(12):
    for k in range(12):
        matriz[j][k] = float(input())
if c == "S":
    for m in range(12):
        soma += matriz[m][coluna]
    print("{:.1f}".format(soma))
elif c == "M":
    for m in range(12):
        media += matriz[m][coluna]
    media /= 12
    print("{:.1f}".format(media))