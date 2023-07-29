while True:
    try:
        l = int(input())
        velocidade = [int(i) for i in input().split()] [:l]
        maior = velocidade[0]
        for i in velocidade:
            if i > maior:
                maior = i
        if maior < 10:
            print("1")
        elif maior >= 10 and maior < 20:
            print("2")
        elif maior >= 20:
            print("3")
    except:
        break