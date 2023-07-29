a, b, c = [int(i) for i in input().split()]

MaiorAB = (a + b + abs(a - b))/2
MaiorC = (MaiorAB + c + abs(MaiorAB - c))/2

print("{:.0f} eh o maior".format(MaiorC))