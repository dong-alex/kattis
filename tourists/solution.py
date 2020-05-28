"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (Lowest  common ancestor + distance ) - https://github.com/UAPSPC/Code-Archive/blob/master/graph/lca.cpp

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""

# SEE C++
from collections import defaultdict, deque
import math
import sys

def log2(n):
    c = 0
    while (n >> 1):
        c += 1
        n = n >> 1
    return c

sys.setrecursionlimit(2000000)
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def constructTree(values, start, currentDepth):
    root = Node(start)
    visited.add(start)
    depth[start] = currentDepth

    for value in values[start]:
        if value in visited:
            continue
        parents[value] = start
        child = constructTree(values, value, currentDepth + 1)
        root.children.append(child)
    return root

def getDistance(u, v):
    a = getLCA(u,v)
    return depth[u] + depth[v] - 2*depth[a] + 1

def getLCA(a,b):
    # find the larger depth
    if depth[b] > depth[a]: return getLCA(b,a)

    # the greater depth of a - move node up until we get to the same depth

    # assert depth[a] == depth[b], "depths are not the same"
    # one of a or b is the LCA
    if a == b: return a
    # move them up
    while parents[a] != parents[b]:
        a = parents[a]
        b = parents[b]

    # found LCA
    # assert(parents[a] == parents[b])
    return parents[a]

def testDivisors(n):
    values = []
    for i in range(1, n+1):
        j = 2 * i
        while j < n+1:
            values.append((i, j))
            j += i
    return values

def getDivisors(n):
    values = []

    while n != 0:
        i = 1
        # find all divisors of 10, 9, 8 ...
        while i <= math.sqrt(n):
            if n % i == 0 and i != n:

                if n / i == i:
                    values.append((i, n))
                else:
                    values.append((i, n))
                    if int(n/i) != n: # dont add the same number to each other
                        values.append((int(n/i), n))
                # values.append((i,n))
            i += 1
        n -= 1
    return values

visited = set()
numAttractions = int(input())
height = log2(numAttractions)
depth = [-1 for _ in range(numAttractions + 1)]
parents = [[-1 for _ in range(height + 1)] for _ in range(numAttractions + 1)]
attractions = defaultdict(list)

# adjacency matrix of lists for the possible parents
for _ in range(numAttractions - 1):
    fromStop, toStop = map(int, input().strip('\n').split(' '))
    attractions[fromStop].append(toStop)
    attractions[toStop].append(fromStop)
# root = constructTree(attractions, 1, 1)

# bfs construct

queue = deque([1])
visited.add(1)
depth[1] = 1
while queue:
    current = queue.pop()
    for c in attractions[current]:
        if c in visited:
            continue
        visited.add(c)
        parents[c][0] = current
        depth[c] = depth[current] + 1
        queue.appendleft(c)

# for p in parents:
    # print(p)

# for every height
for d in range(1, height):
    # for every value of the node
    for j in range(1, numAttractions):
        temp = parents[j][d-1] # check the parent up for the element - if it is not -1 then it is valid 
        if temp != -1:
            parents[j][d] = parents[temp][d-1] # set the next level to be the parent of the above

# just set a node as your root
queries = testDivisors(numAttractions)
# set 1 as the root node
total = 0
for i in queries:
    u = i[0]
    v = i[1]
    # distance = getDistance(u, v)
    # total += getDistance(u, v)
print(total)

