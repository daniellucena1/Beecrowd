ent1 = input().split()
a = ent1[0]
inicio = int(ent1[1])
h, m, s = [int(i) for i in input().split(":")]
ent2 = input().split()
b = ent2[0]
final = int(ent2[1])
hf, mf, sf = [int(i) for i in input().split(":")]

h = h * 3600
m = m * 60
hf = hf * 3600
mf = mf * 60
dias = (final - inicio)
total = (dias * 86400) +  hf + mf + sf - h - m - s

dias = total // 86400
segundos = total%86400

horas = segundos // 3600
segundos = segundos%3600

minutos = segundos // 60
segundos = segundos%60

print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(dias,horas,minutos,segundos))