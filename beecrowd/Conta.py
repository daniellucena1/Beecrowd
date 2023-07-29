n = int(input())
con = 0
while con < n:
    termos = int(input())
    S = []
    soma = 0
    for i in range(termos):
        if i%2 == 0:
            S.append(1)
        elif i%2 != 0:
            S.append(-1)
    for i in range(termos):
        soma += S[i]
    print(soma)
    con += 1