import math
import functools

def tuple_comp(a, b):
    if(a.x < b.x):
        return -1
    if(a.x > b.x):
        return 1
    #==
    if(a.y < b.y):
        return -1
    if(a.y > b.y):
        return 1

    return 0

class point:
    def __init__(self, a, b, name):
        self.x = a
        self.y = b
        self.id = name

def equal_points(a, b):
    if(a.x == b.x and a.y == b.y):
        return True
    else:
        return False

def colinear(a, b, c):
    if(equal_points(a, b) or equal_points(a, c) or equal_points(b, c)): #if some points are equal then theyre colinear (we only have 3 points)
        return True
    #check if area = 0
    if(a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y) == 0):
        return True
    else:
        return False

def area(a, b, c):
    return abs((a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)) / 2.0)

def point_in_triangle(target, a, b, c):
    #calculate the 3 areas and see if they sum up to main area
    a0 = area(a, b, c)
    a1 = area(target, b, c)
    a2 = area(target, a, c)
    a3 = area(target, a, b)

    if(abs(a0 - (a1 + a2 + a3)) <= 0.0001): #we depend on floating point precision
        return True
    else:
        return False

def cross_product(a, b, c):
    if((b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y) < 0):
        #to the left
        return True
    else:
        #to the right (or colinear but we dont need it for 4 points)
        return False



#main

p1 = point(0, 0, "p1")
p2 = point(1, 1, "p2")
p3 = point(3, 3, "p3")
p4 = point(2, 2, "p4")


I = []
J = []

#line case
if(colinear(p1, p2, p3) and colinear(p2, p3, p4)):
    points = [p1, p2, p3, p4]
    #sortam punctele si le distribuim alternant celor 2 multimi
    points.sort(key = functools.cmp_to_key(tuple_comp))
    I.append(points[0].id)
    I.append(points[2].id)
    J.append(points[1].id)
    J.append(points[3].id)

#triangle case, we brute force every case (4 cases in total)
elif(point_in_triangle(p1, p2, p3, p4)):
    #p1 apartine triunghiului
    I.append("p1")
    J.append("p2")
    J.append("p3")
    J.append("p4")
elif(point_in_triangle(p2, p1, p3, p4)):
    #p2 apartine triunghiului
    I.append("p2")
    J.append("p1")
    J.append("p3")
    J.append("p4")
elif(point_in_triangle(p3, p2, p1, p4)):
    #p3 apartine triunghiului
    I.append("p3")
    J.append("p2")
    J.append("p1")
    J.append("p4")
elif(point_in_triangle(p4, p2, p3, p1)):
    #p4 apartine triunghiului
    I.append("p4")
    J.append("p2")
    J.append("p3")
    J.append("p1")

#square case
else:
    #convex hull specific pentru 4 puncte
    points = [p1, p2, p3, p4]
    points.sort(key = lambda point:point.x) #sortam dupa x

    hull = []

    hull.append(points[0]) #we add the leftmost point to our hull

    curr = 0

    leftmost = 1

    #convex hull
    for itr in range(0, 4):
        if(cross_product(points[curr], points[itr], points[leftmost])):
            leftmost = itr #new bound

    curr = leftmost

    while(curr != 0): #repeat until we reach origin
        hull.append(points[curr])

        leftmost = (curr + 1) % 4; #circular loop over our points

        for itr in range(0, 4):
            if(cross_product(points[curr], points[itr], points[leftmost])):
                leftmost = itr #new bound

        curr = leftmost

    #distribuim punctele alternant deoarece acestea se gasesc in ordine in hull[]
    I.append(hull[0].id)
    I.append(hull[2].id)
    J.append(hull[1].id)
    J.append(hull[3].id)

print(I, J)