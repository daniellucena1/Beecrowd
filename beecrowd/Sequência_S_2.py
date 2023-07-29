con = 1
S = 1
N = 2
G = 3
while(con <= 20):
    S = S + G / (N)
    G += 2
    N = N * 2
    con = con + 1
print("{:.2f}".format(S))