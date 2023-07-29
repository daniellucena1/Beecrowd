inicio, minI, final, minF = [int(i) for i in input().split()]

inicio = (inicio * 60) + minI
final = (final * 60) + minF
total = final - inicio
horas = total // 60
minT = total%60

if inicio == final:
    horas = 24
    minT = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas,minT))
elif horas == 0:
    minT = total
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minT))
elif inicio > final:
    horas = ((final + 1440) - inicio)//60
    minT = ((final + 1440) - inicio)%60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minT))
elif final > inicio:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minT))