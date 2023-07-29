con = 0
par = []
impar = []
con_p = 0
con_i = 0
p = 0
while con < 15:
    n = int(input())
    if n%2 == 0:
        par.append(n)
        con_p += 1
        if con_p == 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par = []
            con_p = 0
    elif n%2 != 0:
        impar.append(n)
        con_i += 1
        if con_i == 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar = []
            con_i = 0
    con += 1
    if con == 15:
        if con_i > 0:
            for j in impar:
                print(f"impar[{p}] = {impar[p]}")
                p += 1
        if con_p > 0:
            p = 0
            for j in par:
                print(f"par[{p}] = {par[p]}")
                p += 1