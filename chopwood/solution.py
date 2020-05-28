"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  N/A

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import defaultdict, deque
import heapq

numEdges = int(input())
children = defaultdict(int)
seen = set()
heap = []
vColumn = deque([])

# check valid tree
leaf, total = 0, 0
# numbers from 1 -> n+1 inclusive - find the missing numbers and see where they are
for _ in range(numEdges):
    v = int(input())
    seen.add(v)
    vColumn.append(v)
    children[v] += 1

# find missing numbers - initial leafs - use priority queue to go lowest to highest
# there is an error if there are miultiple numEdges but not enough numEdges to compensate
for i in range(1, numEdges + 2):
    # one of the nodes that we havent seen - need to reset the counter if we hit something because the lower leaf can also be seen then
    if i not in seen:
        heapq.heappush(heap, i)

# if the last value is not the biggest -> not valid tree
if vColumn[-1] != numEdges + 1:
    print("Error")
else:
    # missing numbers left is in the heap
    while heap and vColumn:
        nextU = heapq.heappop(heap)
        nextV = vColumn.popleft()
        # this node corresponds to the first edge searched
        print(nextU)
        children[nextV] -= 1
        # add the node V into the heap because it will be the next leaf - ONLY if the number of children it has is none
        if children[nextV] == 0:
            heapq.heappush(heap, nextV)
