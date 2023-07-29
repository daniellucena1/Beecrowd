num_testes = int(input())
con = 0 

while(con < num_testes):
    num = int(input())
    acm = 0
    for i in range(1,num+1):
        if num%i == 0: 
            acm += 1 
    if acm == 2:
        print("{} eh primo".format(num))
    elif num > 2:
        print("{} nao eh primo".format(num))
    con += 1