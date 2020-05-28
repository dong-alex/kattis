"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (bits to track state similarity) - https://eclass.srv.ualberta.ca/pluginfile.php/5648541/mod_resource/content/1/pebblesolitaire2.cpp
  (Traveling salesperson concept) - https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import deque, defaultdict
from heapq import heappush, heappop
import numpy


def getDistance(stop1, stop2):
    return abs(stop1[0] - stop2[0]) + abs(stop1[1] - stop2[1])


def calculateDistances(numStops, pokestops):
    adjacency = [[0 for _ in range(numStops+1)] for __ in range(numStops+1)]
    # calculate the distance from origin
    for i in range(numPokestops):
        distance = getDistance([0, 0], pokestops[i])
        adjacency[0][i+1] = distance
        adjacency[i+1][0] = distance

    # calculate the distances between each other
    for i in range(numPokestops):
        for j in range(numPokestops):
            if i != j:
                adjacency[i+1][j+1] = getDistance(pokestops[i], pokestops[j])
    return adjacency


def getInput():
    numPokestops = int(input())
    pokestops = []
    bitStops = {}
    # save the value which represents the pokemon - each pokemon has a unique id at this point
    uniquePokemon = []
    stopShift = 0
    for _ in range(numPokestops):
        stop = input().split(' ')
        x, y, name = int(stop[0]), int(stop[1]), stop[2]
        pokestops.append((x, y, name))
        # if a pokemon does not exist then set that pokestop to occupy position
        if name not in bitStops:
            uniquePokemon.append(1 << stopShift)
            bitStops[name] = 1 << stopShift
            stopShift += 1  # shift by 1 to indicate the stop
        else:
            # if the pokemon did exist - then the bit will not change - though we still add coordinate for possible shortest path i.e. two Flareons
            uniquePokemon.append(bitStops[name])
    # after all of the shifts - our costs C(S, i) contains the sets in uniquePokemon along with ending at some i
    cost = [[float('inf') for _ in range(numPokestops+1)]
            for __ in range(1 << stopShift)]
    return numPokestops, pokestops, cost, uniquePokemon, stopShift


numPokestops, pokestops, cost, bitPokemon, shift = getInput()
adjacency = calculateDistances(numPokestops, pokestops)
cost[0][0] = 0  # 0 distance on the origin

# solve for null set - starting at 0 and distance from orgin to all nodes - base case
# distance from 0 to i
for i in range(numPokestops):
    x, y, name = pokestops[i]
    # C(i, Set) = distance
    cost[bitPokemon[i]][i+1] = adjacency[0][i+1]
# keeps track of all the possible visited
onesDictionary = defaultdict(list)
for i in range((1 << shift)):
    onesDictionary[bin(i).count("1")].append(i)
lastNodeVisited = 0
for setSize in range(shift + 1):
    for visitingState in onesDictionary[setSize]:  # This is S in C(S,i)
        currentMin = float('inf')
        possibleValues = []

        for i in range(numPokestops):  # This is i in C(S,i)
            bit = bitPokemon[i]

            # visiting set should be with i
            if bit & visitingState == 0:
                continue
            setWithoutStop = visitingState - bit
            # these are the stops within the visitingState
            for j in range(numPokestops):
                bitJ = bitPokemon[j]
                if i == j or bitJ & visitingState == 0:
                    continue
                # min(C(S-{i}, j) + distance(j, i))
                if cost[setWithoutStop][j+1] + adjacency[i+1][j+1] < cost[visitingState][i+1]:
                    cost[visitingState][i+1] = cost[setWithoutStop][j+1] + \
                        adjacency[i+1][j+1]
                    possibleValues.append(cost[visitingState][i+1])
        # look for minimum pokestop for this specific state
        # look for the pokestop that would be visited
lowest = min(cost[(1 << shift) - 1])
# for line in cost:
# print(line)
print(lowest + adjacency[0][lastNodeVisited+1])

# determine path of this node

# dfs ?
solution = []


def getMinimumDistance(currentStop, visitedState):
    if bin(visitedState).count("1") == 1:
		# base cost and if there are multiple stops take the minimum to the current stop we are at
        index = cost[visitedState].index(
            min(cost[visitedState][currentStop+1]))
        solution.append(index)
        return

    for i in range(numPokestops):
        if i != currentStop and bitPokemon[i] & visitedState == 1:
            edge = adjacency[i][currentStop]
            nextState = visitedState - bitPokemon[currentStop]
            print("Next state", pokestops[i])
			minimumIndex = getMinimumDistance(i, nextState) + edge)
			newCost = cost[nextState][]
            minimum = min(minimum, getMinimumDistance(i, nextState) + edge)
    return


solution = []
initialState = (1 << shift) - 1
shortestDistance = float('inf')
for i in range(numPokestops):
    shortestDistance = min(shortestDistance, getMinimumDistance(
        i, initialState))
print("Shortest distance found", shortestDistance)
