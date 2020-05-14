a1 = [0,0,2]
a2 = [0,0,2]
a3 = [0,0,1]

if(a1 == a2 or a1 == a3 or a2 == a3):
    print('puncte col')
    if(a1 == a2):
        print("A1 = 1 * A2 + 0 * A3")
    if(a1 == a3):
        print("A1 = 1 * A3 + 0 * A2")
    if(a2 == a3):
        print("A2 = 1 * A3 + 0 * A1")

else:

    #Pt ca punctele sa fie coliniare trebuie sa existe a a.i.: A1A3 = a*A1A2
    for i in range(0,3):
        try:
            #generam cele 3 solutii pentru a in functie de x,y,z
            a = (a3[i] - a1[i]) / (a2[i] - a1[i])

        except:
            continue

        x31 = a3[0] - a1[0]             #x3-x1
        y31 = a3[1] - a1[1]             #y3-y1
        z31 = a3[2] - a1[2]             #z3-z1

        ax21 = a * (a2[0] - a1[0])      #a*(x2-x1)
        ay21 = a * (a2[1] - a1[1])      #a*(y2-y1)
        az21 = a * (a2[2] - a1[2])      #a*(z2-z1)

        #daca a exista atunci:
        if x31 == ax21 and y31 == ay21 and z31 == az21:
            print('puncte coliniare')
            print('A3 = (1 - ' + str(a)+ ')*A1 + ' + str(a) + '*A2')    #combinatia baricentrica de forma A3 = (1-a)*A1 + a*A2
            break

    #daca nu gasim a => punctele sunt necoliniare
    print('puncte necoliniare')