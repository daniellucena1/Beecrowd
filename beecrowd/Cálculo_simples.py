peça1 = input(). split()
c1 = peça1[0]
n1 = int(peça1[1])
v1 = float(peça1[2])

peça2 = input(). split()
c2 = peça2[0]
n2 = int(peça2[1])
v2 = float(peça2[2])

p1 = n1*v1
p2 = n2*v2

valor = p1+p2
print('VALOR A PAGAR: R$ {:.2f}'.format(valor))