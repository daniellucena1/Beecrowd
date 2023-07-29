n = int(input())
numeros = [int(i) for i in input().split()] [:n]
output = [2,3,4,5]
con2 = 0
con3 = 0
con4 = 0
con5 = 0

for i in range(n):
    if numeros[i]%2 == 0:
        con2 += 1
    if numeros[i]%3 == 0:
        con3 += 1
    if numeros[i]%4 == 0:
        con4 += 1
    if numeros[i]%5 == 0:
        con5 += 1

output2 = [con2, con3, con4, con5]
for i in range(4):
    print(f"{output2[i]} Multiplo(s) de {output[i]}")