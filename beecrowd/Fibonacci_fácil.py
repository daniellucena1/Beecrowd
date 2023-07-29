N = int(input())
S = 0
P = 1
for i in range(N):
    if i == N-1:
        print(S)
    else:
        print(S, end=" ")
        C = S + P
        S = P
        P = C