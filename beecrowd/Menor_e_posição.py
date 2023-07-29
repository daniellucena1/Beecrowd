n = int(input())
numeros = [int(i) for i in input().strip().split()] [:n]
menor = numeros[0]
posicao = 0
for i in range(n):
  if numeros[i] < menor:
    menor = numeros[i]
    posicao = i
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")