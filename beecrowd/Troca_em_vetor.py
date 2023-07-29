n = []
con = 0
for i in range(20):
    n.append(i)
    n[i] = int(input())
for j in range(19,-1,-1):
    print("N[{}] = {}".format(con,n[j]))
    con += 1