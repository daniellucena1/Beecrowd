n = int(input())
con = 0
while con < n:
    entrada = input().split()
    jo1, jo2 = [int(i) for i in input().split()]
    pessoa1 = {
        'Nome':'',
        'jogada':''
    }
    pessoa2 = {
        'Nome':'',
        'jogada':''
    }
    pessoa1['Nome'] = entrada[0]
    pessoa1['jogada'] = entrada[1]
    pessoa2['Nome'] = entrada[2]
    pessoa2['jogada'] = entrada[3]
    total = jo1 + jo2
    if total%2 == 0:
        if pessoa1['jogada'] == 'PAR':
                print(pessoa1['Nome'])
        else:
            print(pessoa2['Nome'])
    elif total%2 != 0:
        if pessoa1['jogada'] == 'IMPAR':
            print(pessoa1['Nome'])
        else:
            print(pessoa2['Nome'])
    con += 1