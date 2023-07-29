n = int(input())
con = 1
while(con <= n):
    acm = 0
    x = int(input())
    for i in range(1,x):
        if x%i == 0:
            acm += i
    if acm == x:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))
    con += 1