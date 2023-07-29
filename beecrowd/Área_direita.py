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
    m = 7
    for i in range(5,0,-1):
        for j in range(m,12):
            soma += matriz[i][j]
        m += 1
    m = 7
    for i in range(6,11):
        for j in range(m,12):
            soma += matriz[i][j]
        m += 1
    print("{:.1f}".format(soma))
elif o == "M":
    m = 7
    for i in range(5,0,-1):
        for j in range(m,12):
            media += matriz[i][j]
        m += 1
    m = 7
    for i in range(6,11):
        for j in range(m,12):
            media += matriz[i][j]
        m += 1
    media = media / 30
    print("{:.1f}".format(media))