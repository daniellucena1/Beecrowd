nome = input()
salário = float(input())
vendas = float(input())
comissão = (15/100)*vendas
total = salário + comissão
print('TOTAL = R$ {:.2f}'.format(total))