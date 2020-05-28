"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (fenwick tree for update/query swaps) - https://github.com/UAPSPC/Code-Archive/blob/master/data_structures/fenwick_tree.cpp

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import defaultdict

# Kattis boundaries - n+1 because we have 0 was root value in Fenwick Tree + indexing
totalLength = 100001

# use hashtable to store indices of the elements
elementIndex = defaultdict(int)
numElements = int(input())
elements = []
swapsNeeded = [0 for _ in range(numElements)]
# i is the number relevant to the index - does not matter in the Fenwick Tree because we can just remove the ++ in index above
for i in range(1, numElements + 1):
    element = int(input())
    elements.append(element)
    elementIndex[element] = i  # save the position of the element found
    swapsNeeded[element-1] = abs(i - element)
    # update the position by 1 - increased the number of swaps

print(swapsNeeded)
# expected position of elements are at element - 1 index = number of swaps needed
left = 0
right = numElements - 1

oddNumber = 1
evenNumber = numElements
for phase in range(1, numElements+1):
    # odd phases sort on the beginning
    if phase % 2 == 1:
        targetPosition = left
        target = oddNumber
        oddNumber += 1
        left += 1

    # even phases sort on the end
    else:
        targetPosition = right
        target = evenNumber
        evenNumber -= 1
        right -= 1
    # print("Current position", targetPosition, "swapping for target", target)
    # first sorting - get the index of the value to swap
    # print(swaps)
