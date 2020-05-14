class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if(self.x != other.x):
            return self.x < other.x
        return self.y < other.y;

    def __gt__(self, other):
        if(self.x != other.x):
            return self.x <= other.x
        return self.y <= other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def min(A, B):
        if(A.x != B.x):
            if(A.x <= B.x):
                return A
            return B
        if(A.y <= B.y):
            return A
        return B

    def max(A, B):
        if(A.x != B.x):
            if(A.x >= B.x):
                return A
            return B
        if(A.y >= B.y):
            return A
        return B


def line_intersection(A, B, C, D):
    #generam ecuatiile aferente celor 2 perechi de puncte
    a1 = A.y - B.y
    a2 = C.y - D.y
    b1 = B.x - A.x
    b2 = D.x - C.x
    c1 = B.x*A.y - A.x*B.y
    c2 = D.x*C.y - C.x*D.y

    #calculam determinantul sistemului
    det = a1*b2 - b1*a2

    if(det != 0):
        #daca determinantul e diferit de 0 atunci rezolvam cu metoda cramer
        x = ((B.x*A.y - A.x*B.y)*b2 - (D.x*C.y - C.x*D.y)*b1) / det;
        y = ((D.x*C.y - C.x*D.y)*a1 - (B.x*A.y - A.x*B.y)*a2) / det;
        #verificam daca intersectia celor 2 drepte se afla pe segmentele noastre
        if(x < min(A.x, B.x) or x < min(C.x, D.x) or x > max(A.x, B.x) or x > max(C.x, D.x)):
            print("no intersection")
        else:
            print(x, y)

    #avem un sistem nedeterminat
    elif(b1*c2 - b2*c1 != 0):
        #rangul = 2 => incompatibil
        print("no intersection")

    elif(a1*c2 - a2*c1 != 0):
        #rangul = 2 => incompatibil
        print("no intersection")

    #rangul = 1 => dreptele coincid
    else:
        min1 = Point.min(A, B)
        min2 = Point.min(C, D)
        max1 = Point.max(A, B)
        max2 = Point.max(C, D)

        if(min1 == min2 and max1 == max2):
            #segmentele sunt identice
            print("==")

        elif(max2 < min1):
            #segmentele nu se suprapun
            print("nu exista")

        #calculam intersectia segmentelor
        elif(max2 == min1):
            print(min1.x, min1.y)

        elif(min2 < min1):
            print(min1.x, min1.y, min(max1,max2).x, min(max1, max2).y)

        elif(min1 == min2 and min2 == min(max1, max2)):
            print(min1.x, min1.y)

        elif(min2 < min(max1, max2)):
            print(min2.x, min2.y, min(max1,max2).x, min(max1, max2).y)

        elif(min2 == min(max1, max2)):
            print(min2.x, min2.y)

        else:
            #segmentele nu se suprapun
            print("multimea vida")


a1 = Point(0, 0)
a2 = Point(4, 4)

b1 = Point(4, 0)
b2 = Point(0, 4)

line_intersection(a1, a2, b1, b2)