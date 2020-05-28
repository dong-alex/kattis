"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (get the rectangle coordinates) - https://github.com/UAPSPC/Code-Archive/blob/master/2d_geometry/rotate_2d.c
  (convex hull) - https://github.com/UAPSPC/Code-Archive/blob/master/2d_geometry/convex_hull.cpp
  (python cross) - https://stackoverflow.com/questions/1984799/cross-product-of-two-vectors-in-python

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""

# TODO - does not work - use C++
import math
from functools import cmp_to_key


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def rotatePoint(point, origin, theta):
    EPS = 1 * (10 ** -10)

    m = [[0, 0], [0, 0]]
    r = Point(-1, -1)
    m[0][0] = m[1][1] = math.cos(2 * math.pi - theta)
    m[0][1] = -math.sin(2 * math.pi - theta)
    m[1][0] = -m[0][1]

    point.x -= origin.x
    point.y -= origin.y

    r.x = m[0][0] * point.x + m[0][1] * point.y + origin.x
    r.y = m[1][0] * point.x + m[1][1] * point.y + origin.y

    if abs(r.x) < EPS:
        r.x = 0
    if abs(r.y) < EPS:
        r.y = 0
    return r


def signedArea(p):
    # 2x2 only
    def cross(a, b):
        return a.x * b.y - b.x * a.y

    totalArea = 0
    i = len(p) - 1
    for j in range(0, len(p)):
        totalArea += cross(p[i], p[j])
        i = j
    return totalArea / 2.0


def convex(poly):
    EPS = 1 * (10 ** -10)

    def polarCompare(p1, p2):
        EPS = 1 * (10 ** -10)

        direction = crossProductDir(p1, p2, P0)

        if direction == 'CW':
            return True
        elif direction == 'CCW':
            return False
        else:
            d = norm(Point(p1.x - P0.x, p1.y - P0.y)) - \
                norm(Point(p2.x - P0.x, p2.y - P0.y))

            if abs(d) < EPS:
                return False
            elif d < 0.0:
                return True
            else:
                return False

    def norm(p1):
        return math.sqrt(pow(p1.x, 2) + pow(p1.y, 2))

    # 2x2 only
    def cross(a, b):
        return (a.x * b.y) - (a.y * b.x)

    def crossProductDir(p1, p2, p0):
        EPS = 1 * (10 ** -10)

        res = cross(Point(p1.x - p0.x, p1.y - p0.y),
                    Point(p2.x - p0.x, p2.y - p0.y))

        if abs(res) < EPS:
            return 'CL'
        elif res > 0.0:
            return 'CW'
        else:
            return 'CCW'

    if len(poly) <= 1:
        return poly

    hull = []

    minimum = 0
    P0 = poly[0]

    # find lowest y and then lowest y
    for i in range(1, len(poly)):
        if poly[i].y < P0.y or abs(poly[i].y - P0.y) < EPS and poly[i].x < P0.x:
            minimum = i
            P0 = poly[i]

    # put P0 into start of poly
    poly[minimum] = poly[0]
    poly[0] = P0
    hull.append(P0)

    print(poly)
    poly = [poly[0]] + list(sorted(poly[1:], key=cmp_to_key(polarCompare)))
    print(poly)
    # print(hull[-1].x, hull[-1].y)

    for i in range(1, len(poly)):
        if norm(Point(poly[i].x - P0.x, poly[i].y - P0.y)) > EPS:
            break

    if i == len(poly):
        return hull

    hull.append(poly[i])
    i += 1
    # print(hull[-2].x, hull[-2].y, hull[-1].x, hull[-1].y)

    while i < len(poly):
        while len(hull) > 1 and crossProductDir(poly[i], hull[-1], hull[-2]) != 'CCW':
            hull.pop()

        hull.append(poly[i])
        i += 1
    return hull


numTests = int(input())
for _ in range(numTests):
    numBoards = int(input())
    convexPoints = []
    totalArea = 0
    for __ in range(numBoards):
        x, y, width, height, angle = map(float, input().strip('\n').split(' '))
        totalArea += width * height
        width *= 0.5
        height *= 0.5
        point1 = Point(x + width, y + height)
        point2 = Point(x + width, y - height)
        point3 = Point(x - width, y - height)
        point4 = Point(x - width, y + height)
        origin = Point(x, y)

        point1 = rotatePoint(point1, origin, math.radians(angle))
        point2 = rotatePoint(point2, origin, math.radians(angle))
        point3 = rotatePoint(point3, origin, math.radians(angle))
        point4 = rotatePoint(point4, origin, math.radians(angle))

        convexPoints.extend([point1, point2, point3, point4])

    hull = convex(convexPoints)
    for k in hull:
        print("(" + str(k.x) + "," + str(k.y) + ")")
    print("{:.1f} %".format(((totalArea / signedArea(hull)) * 100)))
