n = int(input())
con = 0
while con < n:
    desafiados = [str(i) for i in input().split()]
    nome = desafiados[0]
    forca = int(desafiados[1])

    if nome == 'Thor':
        print("Y")
    elif nome != 'Thor':
        print("N")
    con += 1