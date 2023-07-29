n = int(input())
con = 1
acm = 0

while(con <= n):
    acm = 0
    x, y = [int(i) for i in input().split()]
    for i in range(x+1,y) or range(y+1,x):
        if i%2 != 0:
            acm += i
    con += 1
    print(acm)