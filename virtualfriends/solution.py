"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (disjoin set and merging) - https://cp-algorithms.com/data_structures/disjoint_set_union.html

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import defaultdict

# parent of itself is itself - initially - if it has not existed


def makeSet(v):
    if v not in parents:
        parents[v] = v
        networkSize[v] += 1
        # print("Creating node for new friend", v, "with network size", networkSize[v])
    return

# O(n) time for the chain


def findSet(v):
    # if we found the parent root - return it
    if (v == parents[v]):
        return v
    # otherwise - move up and see if we find the root (we always will)
        # 7 -> 5 -> 3 -> 2 -> 1
        # then whatever the values moving up - points to the 1
    parents[v] = findSet(parents[v])
    return parents[v]


def unionSet(u, v):
    a = findSet(u)
    b = findSet(v)

    # if the values are not the same - i.e. not merging the same thing - set the parent of one of them to the other
    if a != b:
        # if size of a is less, swap to the bigger network size
        if networkSize[a] < networkSize[b]:
            a, b = b, a
        # a is the parent for b
        parents[b] = a

        # add the leader of the root size with the network size
        networkSize[a] += networkSize[b]
    print(networkSize[a])
    # print("New network size of", networkSize[a])
    # if it does not pass - then both values have the SAME parent - then just point the root to the parent


# union find
numTests = int(input())
for _ in range(numTests):
    numFriendships = int(input())

    parents = defaultdict(int)

    total = 0
    networkSize = defaultdict(int)
    for __ in range(numFriendships):
        friend1, friend2 = input().strip('\n').split(' ')
        # attempt to make a node for the friend - if we have seen them before - don't do anything
        makeSet(friend1)
        makeSet(friend2)

        # attempt to merge the friends
        unionSet(friend1, friend2)
        # as we construct the merges - then we keep the size
