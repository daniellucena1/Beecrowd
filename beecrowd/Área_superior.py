o = input()
matriz = [0] * 12
soma = 0
media = 0
for i in range(12):
    matriz[i] = [0] * 12
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
if o == "S":
    n = 0
    m = 12
    for i in range(0,5):
        n += 1
        m -= 1
        for j in range(n,m):
            soma += matriz[i][j]
    print("{:.1f}".format(soma))
elif o == "M":
    n = 0
    m = 12
    for i in range(0,5):
        n += 1
        m -= 1
        for j in range(n,m):
            media += matriz[i][j]
    media = media / 30
    print("{:.1f}".format(media))