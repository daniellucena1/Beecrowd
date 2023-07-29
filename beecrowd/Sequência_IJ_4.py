con = 1
J1 = 0.8
J2 = 1.8
J3 = 2.8
I = -0.2
while(con <= 11):
    J1 = J1 + 0.2
    J2 = J2 + 0.2
    J3 = J3 + 0.2
    I = I + 0.2
    print("I={:g} J={:g}".format(I, J1))
    print("I={:g} J={:g}".format(I, J2))
    print("I={:g} J={:g}".format(I, J3))
    con = con + 1