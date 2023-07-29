n = int(input())
con = 0
soma = 0

def calculo(price, qtd):
    global soma
    total = price * qtd
    soma += total
    return total

while con < n:
    produto, qtd = [int(i) for i in input().split()]

    if produto == 1001:
        calculo(1.5, qtd)
    elif produto == 1002:
        calculo(2.5, qtd)
    elif produto == 1003:
        calculo(3.5, qtd)
    elif produto == 1004:
        calculo(4.5, qtd)
    elif produto == 1005:
        calculo(5.5, qtd)

    con += 1

print("{:.2f}".format(soma))