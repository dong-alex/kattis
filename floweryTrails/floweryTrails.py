from collections import defaultdict, deque
from heapq import heappush, heappop

numPoints, numTrails = list(map(int, input().split()))

adjacency = defaultdict(list)
distances = [[2000 for _ in range(numPoints)]
             for __ in range(numPoints)]
vertices = [2000 for _ in range(numPoints)]
# all paths with the minimum distance from 0 to the peak P - 1
for _ in range(numTrails):
    fromStop, toStop, distance = list(map(int, input().split()))

    # skip cycles - never minimum path
    if fromStop == toStop:
        continue

    # adjacency list for neighbors - not directed
    adjacency[fromStop].append((toStop, distance))
    adjacency[toStop].append((fromStop, distance))

    # distances matrix - only keep minimums - want to count how many minimum paths too
    distances[fromStop][toStop] = min(distances[fromStop][toStop], distance)
    distances[toStop][fromStop] = min(distances[toStop][fromStop], distance)
# calculate the shortest path -BFS
# queue = deque()
# queue.append((0, 0, [0]))  # save current path and distance
heap = []
heappush(heap, (0, 0))  # distance, current
visited = set()
parents = defaultdict(list)
vertices[0] = 0
# keep track of the path via parents - trace backwards to find all paths from n-1 to 0
while heap:
    # extract minimum distance
    currentDistance, point = heappop(heap)

    # have we reached the target yet
    if point in visited:
        continue  # continue to find the shortest paths - don't need to go beyond n-1 point

    # add visited after n-1 check because we want to stop at n-1. useless to continue
    visited.add(point)
    # add to visited to prevent going backwards
    # check all the neighbours
    for neighbour, distance in adjacency[point]:
        # relaxation - update the distances[neighbour]
        # if the distances we found are NOT equal or less than skip.
        # if the distances we found are less than - reset the parents - don't care about longer paths
        # if the distances we found are euqal, then append the nodes
        # update the parents
        if currentDistance + distance < vertices[neighbour]:
            vertices[neighbour] = currentDistance + distance
            parents[neighbour] = [point]
            heappush(heap, (vertices[neighbour], neighbour))

        # multiple paths
        elif currentDistance + distance == vertices[neighbour]:
            parents[neighbour].append(point)

print(parents)
# work backwards to gather paths
queue = deque([numPoints-1])
pathDistance = 0
visited.clear()
while queue:
    parent = queue.popleft()

    # check for visited parents - don't want to add more.
    if parent in visited:
        continue

    visited.add(parent)
    for child in parents[parent]:
        # only use the child parent relation as many times as shortest paths to it
        pathDistance += distances[parent][child]
        queue.append(child)

print(2 * pathDistance)
