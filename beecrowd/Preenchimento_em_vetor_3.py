x = float(input())
n = []
con = 0
while con < 100:
    n.append(x)
    x /= 2
    con += 1
for i in range(100):
    print("N[{}] = {:.4f}".format(i,n[i]))