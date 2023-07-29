a, b, c = [int(i) for i in input().split()]
delta = b**2-4*a*c
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
 X1 = (-b+(delta)**0.5)/(2*a)
 X2 = (-b-(delta)**0.5)/(2*a)

 print('R1 = {:.5f}'.format(X1))
 print('R2 = {:.5f}'.format(X2))