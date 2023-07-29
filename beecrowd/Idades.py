n = 0
acm = 0
con = 0
while(n >= 0):
    n = int(input())
    if n > 0:
        acm += n
        con += 1
media = acm/con
print("{:.2f}".format(media))