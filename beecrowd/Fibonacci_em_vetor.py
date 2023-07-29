testes = int(input())
impressao = []
numeros = []
con = 0
while con < testes:
    N = int(input())
    numeros.append(N)
    S = 0
    P = 1
    for i in range(N):
        C = S + P
        S = P
        P = C
    impressao.append(S)
    con += 1
for j in range(testes):
    print(f"Fib({numeros[j]}) = {impressao[j]}")