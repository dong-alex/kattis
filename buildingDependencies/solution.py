"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (general topological sorting) - https://www.geeksforgeeks.org/topological-sorting/
  (kahns algo for indegrees usage) - https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
  (topological visualization like dependencies - just remove unnecessary dependencies) - https://www.cs.usfca.edu/~galles/visualization/TopoSortIndegree.html

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import defaultdict, deque

num = int(input())

adjacency = defaultdict(list)
degrees = defaultdict(int)
for i in range(num):
    files = input()
    filename = files.split(':')[0]
    dependencies = files.split(':')[1].split(' ')[1:]
    # map the dependencies to the file being affected
    for dependency in dependencies:
        adjacency[dependency].append(filename)
# not including the file changed
# changed file to start with
changed = input()

# check for any dependencies of this and remove it because its unnecessary
# any dependencies that are not visited from gmp - remove them from the list of the other dependencies
affiliatedDependencies = set()
stack = [changed]

while stack:
    current = stack.pop()

    if current in affiliatedDependencies:
        continue

    affiliatedDependencies.add(current)

    for neighbour in adjacency[current]:
        stack.append(neighbour)

# refresh adjacency list
degrees = defaultdict(int)
newAdjacency = defaultdict(list)
# remove all dependencies NOT in the affiliated ones
for key, value in adjacency.items():
    if key not in affiliatedDependencies:
        continue

    for item in value:
        if item in affiliatedDependencies:
            newAdjacency[key].append(item)
            degrees[item] += 1

# print(degrees)
# print(newAdjacency)
# dfs traversal for topological sorting - starting at the changed dependencies
stack = [changed]
topologicalSort = [changed]
visited = set()
# handle indegrees that are very far in
"""
9
gmp:
solution: set map queue test2
base:
set: base gmp
map: base gmp
test1: test3
test2: test1
test3: set
queue: base
gmp

returns:

gmp
set
map
solution
test3
test1
test2

requires tests to go first before solution - indegrees must be dropped to be next
"""


def dfs(start):
    stack = [start]
    while stack:
        current = stack.pop()
        # got to the bottom
        for neighbour in newAdjacency[current]:
            degrees[neighbour] -= 1

            if degrees[neighbour] == 0:
                visited.add(neighbour)
                topologicalSort.append(neighbour)
                stack.append(neighbour)


dfs(changed)


for i in range(len(topologicalSort)):
    print(topologicalSort[i])

# bfs

# print(newAdjacency)
# queue = deque([changed])

# while queue:
#     current = queue.pop()
#     if current in visited:
#         continue

#     degrees[current] -= 1
#     if degrees[current] == 0:
#         topologicalSort.append(current)
#         visited.add(current)

#     for neighbor in newAdjacency[current]:
#         queue.appendleft(neighbor)

# for i in range(len(topologicalSort)):
#     print(topologicalSort[i])
# print(topologicalSort)

# dfs recursive

# topologicalFirst = []
# visited = set()


# def dfs(current):

#     if current in visited:
#         return

#     visited.add(current)

#     for neighbour in adjacency[current]:

#         dfs(neighbour)
#     topologicalFirst.append(current)

#     return


# dfs(changed)

# while topologicalFirst:
#     print(topologicalFirst.pop())
"""

gmp -> map
base \-^
      \     \
        > set > solution

"""
