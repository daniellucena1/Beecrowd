n = int(input())
con = 1

while(con <= n):
    ent = input().split()
    x = int(ent[0])
    y = int(ent[1])
    if y == 0:
        print("divisao impossivel")
    else:
        divisao = x / y
        print("{:.1f}".format(divisao))
    con += 1