n = 15
con = 0
acm = 0
while(con < 2):
    n = eval(input())
    if n >= 0 and n <= 10:
        acm += n
        media = acm/2
        con += 1
    else:
        print("nota invalida")
    if con == 2:
        print("media =", media)