a = 1

while a != 0:

    entrada = input().split()

    a = int(entrada[0])

    if len(entrada) == 3:

        b = int(entrada[1])
        c = int(entrada[2])

        tamanhoDoTerreno = (a*b) / (c/100)

        tamanhoDoTerreno = int(tamanhoDoTerreno**0.5)

        if a != 0:
            print(tamanhoDoTerreno)