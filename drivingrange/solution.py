"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (prims-algo for MST) - https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
  (consideration - Kruskals alternative) - https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import defaultdict
from heapq import heappush, heappop
# use MST to find longest path to connect to city
# print IMPOSSIBLE if numCities != cities in the roads - at least one would not be visitable


def getInput(numCities, numRoads):
    total = set()
    adjacency = defaultdict(list)
    for _ in range(numRoads):
        city1, city2, distance = map(int, input().split(' '))
        adjacency[city1].append((distance, city2))
        adjacency[city2].append((distance, city1))

        if city1 not in total:
            total.add(city1)
        if city2 not in total:
            total.add(city2)

    if len(total) != numCities:
        return None
    return adjacency


def getMinimumKey(distances, visitedSet):
    minimum = float('inf')
    nextCity = -1
    # check every city for the smallest distance in distances
    # use that edge next
    for i in range(len(distances)):
        if distances[i] < minimum and i not in visitedSet:
            minimum = distances[i]
            nextCity = i

    return nextCity


def main():

    numCities, numRoads = map(int, input().split(' '))
    adjacency = getInput(numCities, numRoads)

    if not adjacency:
        print("IMPOSSIBLE")
        return 0

    visited = set()

    key = [float('inf') for _ in range(numCities)]

    # pick any city - wouldn't matter
    key[0] = 0

    # distance, city
    heap = [(0, 0)]

    while heap:
        # extract the minimum distance vertex
        distance, city = heappop(heap)

        # visit the city because its already set
        visited.add(city)

        # use heapq just in case shorter distances are found - don't need to iterate through the entire array
        for nextDistance, nextCity in adjacency[city]:
            if nextCity not in visited and nextDistance < key[nextCity]:
                key[nextCity] = nextDistance
                heappush(heap, (key[nextCity], nextCity))

    # starting at the vertex 0 pick the smallest edge
    # for _ in range(numCities):
    #     # get the u vertext for the u->v edge that will be minimum greedily
    #     currentCity = getMinimumKey(distances, visited)

    #     # visited this city
    #     visited.add(currentCity)

    #     # check the distances for all connections
    #     for nextDistance, nextCity in adjacency[currentCity]:

    #         # if it has not visited yet and the new edge beats what was found (initially inf)
    #         if nextCity not in visited and nextDistance < distances[nextCity]:
    #             distances[nextCity] = nextDistance

    # MST maximum is the longest youll ever have to travel
    print(max(key))


main()
