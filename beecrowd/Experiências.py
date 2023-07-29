n = int(input())
con = 1
total = 0
coelhos = 0
ratos = 0
sapos = 0

while(con <= n):
    ent = input().split()
    a = int(ent[0])
    b = str(ent[1])
    total += a
    if b == "C":
        coelhos += a
    elif b == "R":
        ratos += a
    elif b == "S":
        sapos += a
    con += 1

percentualC = (coelhos * 100) / total
percentualR = (ratos * 100) / total
percentualS = (sapos * 100) / total

print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}".format(total,coelhos,ratos,sapos))
print("Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(percentualC,percentualR,percentualS))