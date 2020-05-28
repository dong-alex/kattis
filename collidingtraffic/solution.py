"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (closest pair in C++) - https://github.com/UAPSPC/Code-Archive/blob/master/2d_geometry/closest_pair.c

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""

# colliding = distance within each other
# given position - direction - speed (use t as parameter for intersection)
# if they come within a given distance of each other = collision - not intersection
# find all intersections and when they occur - then up to then find for some time - see if distance is within it then collision

# degrees given as the direction

# boundaries
# 1000 boats
# -1000, 1000 edges
# speed 0.001 - 1000
# degrees 0 - 360 (from north)
import math
from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getLines(boats):
    lines = []

    for boat in boats:
        x, y, rotation, speed = boat
        nextX = x + (speed * math.cos(rotation))
        nextY = y + (speed * math.sin(rotation))

        lines.append((Point(x, y), Point(nextX, nextY)))

    return lines


def getDistanceFromTwoPoints(a, b):
    return math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))


def getIntersection(line1, line2, intersection):
    EPS = 1*(10**-8)

    a, b = line1
    c, d = line2

    # cramers rule det A' / det A
    num1 = (a.y - c.y) * (d.x - c.x) - (a.x - c.x) * (d.y - c.y)
    denom = (b.x - a.x) * (d.y - c.y) - (b.y - a.y) * (d.x - c.x)

    if abs(denom) >= EPS:
        r = num1 / denom
        intersection.x = a.x + r * (b.x - a.x)
        intersection.y = a.y + r * (b.y - a.y)
        return 1

    if abs(num1) >= EPS:
        return 0
    return -1


testCases = int(input())

# check each test case
for _ in range(testCases):
    numBoats, collisionDistance = map(float, input().strip('\n').split(' '))
    numBoats = int(numBoats)
    boats = []
    for i in range(numBoats):
        x, y, rotation, speed = map(float, input().strip('\n').split(' '))
        boats.append((x, y, math.radians(rotation), speed,))
    lines = getLines(boats)
    # for line in lines:
    #     print(line[0].x, line[0].y, line[1].x, line[1].y)

    # for each t value
    