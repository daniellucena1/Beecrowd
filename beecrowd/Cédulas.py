valor = int(input())
cedulas = [100,50,20,10,5,2,1]
print(valor)
for i in cedulas:
    notas = valor//i
    valor = valor%i
    print("{} nota(s) de R$ {},00".format(notas,i))