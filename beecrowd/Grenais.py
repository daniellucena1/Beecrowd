acmgremio = 0
acminter = 0
novo = 0
empate = 0
grenais = 0
while(novo != 2):
    inter, gremio = [int(i) for i in input().split()]
    if inter > gremio:
        acminter += 1
        grenais += 1
    elif inter < gremio:
        acmgremio += 1
        grenais += 1
    elif gremio == inter:
        empate += 1
        grenais += 1
    print("Novo grenal (1-sim 2-nao)")
    novo = int(input())
    if novo == 2:
        print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(grenais,acminter,acmgremio,empate))
        if acminter > acmgremio:
            print("Inter venceu mais")
        elif acminter < acmgremio:
            print("Gremio venceu mais")