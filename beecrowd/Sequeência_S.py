con = 1
S = 0
N = 1
while(con <= 100):
    S = S + 1/(N)
    N = N + 1
    con = con + 1
print("{:.2f}".format(S))