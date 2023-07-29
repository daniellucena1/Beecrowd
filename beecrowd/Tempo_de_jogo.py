ent = input().split()
inicio = int(ent[0])
final = int(ent[1])

if inicio > final:
    total = (final + 24) - inicio
    print("O JOGO DUROU {} HORA(S)".format(total))
elif final > inicio:
    total = final - inicio
    print("O JOGO DUROU {} HORA(S)".format(total))
else:
    total = 24
    print("O JOGO DUROU {} HORA(S)".format(total))