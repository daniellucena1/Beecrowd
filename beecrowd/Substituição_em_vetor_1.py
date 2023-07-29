vetor = []
for i in range(10):
    vetor.append(i)
for i in range(10):
    vetor[i] = int(input())
    if vetor[i] <= 0:
        vetor[i] = 1
    print(f"X[{i}] = {vetor[i]}")