"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (tangents on circle) - https://github.com/UAPSPC/Code-Archive/blob/master/2d_geometry/circ_tangents.c
  (solving standard form) - https://bobobobo.wordpress.com/2008/01/07/solving-linear-equations-ax-by-c-0/
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
import math


class Point():
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


def dist2(a):
    return a.x ** 2 + a.y ** 2


def tangents(p):
    tmp = dist2(p)
    para = 1 * 1 / tmp
    perp = 1 * math.sqrt(tmp - 1 * 1) / tmp
    a.x = p.x * para - p.y * perp
    a.y = p.y * para + p.x * perp
    b.x = p.x * para + p.y * perp
    b.y = p.y * para - p.x * perp


numTests = int(input())

cPoint = Point(0, 0)
radius = 1

# circle is always with a point of (0,0) center and radius of 1
while numTests:
    a = Point()
    b = Point()
    x, y = map(int, input().strip('\n').split(' '))
    tangents(Point(x, y))
    # solve (1-t) * p + t * q = (1 - t') p' + t' * q'
    # a and b are the points of tangency on the circle - now we have two points
    # formula - [r(t) = (1-t) * p + t * q] for some point p and q
    # a is x's
    # b is y's

    a1 = "{0:0.9f}".format(a.y - y)
    b1 = "{0:0.9f}".format(x - a.x)
    c1 = "{0:0.9f}".format(-(a.x*y - x*a.y))

    a2 = "{0:0.9f}".format(b.y - y)
    b2 = "{0:0.9f}".format(x - b.x)
    c2 = "{0:0.9f}".format(-(b.x*y - x*b.y))
    print("(" + ','.join([a1, b1, c1]) + "," + ','.join([a2, b2, c2]) + ")")

    numTests -= 1
