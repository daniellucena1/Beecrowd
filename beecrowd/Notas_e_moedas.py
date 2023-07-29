N = float(input())
N *= 100

notasEmoedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

for i in notasEmoedas:
    notas = N//i
    N = N%i
    if i > 100:
        print("{} nota(s) de R$ {},00".format(notas,i))
    else:
        print("{} moeda(s) de R$ {},00".format(notas,i))