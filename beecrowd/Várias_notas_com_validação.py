n = 2
nova = 0
con = 0
acm = 0
while(nova != 2):
    nova = 0
    n = eval(input())
    if n < 0 or n > 10:
        print("nota invalida")
    elif n >= 0 and n <= 10:
        acm += n
        con += 1
    if con == 2:
        media = acm / 2
        print("media = {:.2f}".format(media))
        con = 0
        acm = 0
        while(nova < 1 or nova > 2):
            print("novo calculo (1-sim 2-nao)")
            nova = int(input())