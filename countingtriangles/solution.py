"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (line segment intersection) - https://github.com/UAPSPC/Code-Archive/blob/master/2d_geometry/isect_lineseg.c

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def isDistinct(i1, i2, i3):
    EPS = 1*(10**-8)
    if abs(i1.x - i2.x) < EPS or abs(i1.y - i2.y) < EPS:
        return False
    if abs(i2.x - i3.x) < EPS or abs(i2.y - i3.y) < EPS:
        return False
    if abs(i1.x - i3.x) < EPS or abs(i1.y - i3.y) < EPS:
        return False
    return True


def getIntersection(line1, line2, intersection):
    EPS = 1*(10**-8)

    a, b = line1
    c, d = line2

    num1 = (a.y - c.y) * (d.x - c.x) - (a.x - c.x) * (d.y - c.y)
    num2 = (a.y - c.y) * (b.x - a.x) - (a.x - c.x) * (b.y - a.y)
    denom = (b.x - a.x) * (d.y - c.y) - (b.y - a.y) * (d.x - c.x)

    if abs(denom) >= EPS:
        r = num1 / denom
        s = num2 / denom

        if 0 - EPS <= r and r <= 1+EPS and 0 - EPS <= s and s <= 1 + EPS:
            intersection.x = a.x + r * (b.x - a.x)
            intersection.y = a.y + r * (b.y - a.y)
            return 1
        return 0

    if abs(num1) >= EPS:
        return 0

    if a.x > b.x or (a.x == b.x and a.y > b.y):
        t = a
        a = b
        b = t

    if c.x > d.x or (c.x == d.x and c.y > d.y):
        t = c
        c = d
        d = t

    if a.x == b.x:
        if b.y == c.y:
            intersection = b
            return 1
        elif a.y == d.y:
            intersection = a
            return 1
        elif b.y < c.y or d.y < a.y:
            return 0
    else:
        if b.x == c.x:
            intersection = b
            return 1
        elif a.x == d.x:
            intersection = a
            return 1
        elif b.x < c.x or d.x < a.x:
            return 0
    return -1


while True:
    numSegments = int(input())

    # end of the test cases file
    if numSegments == 0:
        break

    lines = []
    solution = 0
    # otherwise grab the data
    for _ in range(numSegments):
        x1, y1, x2, y2 = map(float, input().split(' '))
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        lines.append((point1, point2))

    # calculate all possible triplet of line segments then check if they have required intersections
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            for k in range(j+1, len(lines)):
                intersection1 = Point(-1, -1)
                intersection2 = Point(-2, -2)
                intersection3 = Point(-3, -3)
                line1 = lines[i]
                line2 = lines[j]
                line3 = lines[k]
                totalIntersections = getIntersection(line1, line2, intersection1) + getIntersection(
                    line1, line3, intersection2) + getIntersection(line2, line3, intersection3)
                # if there are no 3 intersections for these 3 triangles then continue
                if totalIntersections < 3:
                    continue
                else:
                    # EPS = 1*(10**-8)
                    # if (intersection1.x - intersection2.x > EPS or intersection1.y - intersection2.y > EPS):
                    #     continue
                    # chance we can get same intersection i.e. 5.1477247832040165 2.834198995892287
                    # print(intersection1.x, intersection1.y)
                    # print(intersection2.x, intersection2.y)
                    # print(intersection3.x, intersection3.y)
                    if isDistinct(intersection1, intersection2, intersection3):
                        solution += 1
                # line i, line j, line k

                # lines i doesnt intersect line j or line k then continue
                # lines j doesnt intersect line k then continue

    # 3 intersections - each line will have 2 intersections (AC) (AB) (BC) || (CA) (BA) (CA)
    print(solution)
