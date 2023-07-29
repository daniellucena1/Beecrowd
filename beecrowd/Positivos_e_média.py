x = 0
con = 1
acm = 0
while(con <= 6):
    a = float(input())
    if a > 0:
        x += 1
        acm = acm + a
    con += 1
media = acm / x
print("{} valores positivos".format(x))
print("{:.1f}".format(media))