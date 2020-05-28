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


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n+1)]

    # sum the values up - moving up based on subtracting AND two complement of itself
    # gets sum up to and including the index
    def sumValues(self, index):
        out = 0
        # index += 1 # removed because we start at index 1
        while (index > 0):
            out += self.tree[index]
            index -= index & (-index)
        return out

    # adds delta to value at index
    def update(self, index, delta):
        # index += 1 # removed because we start at index 1
        while index <= self.n:
            self.tree[index] += delta

            # bitwise operation - AND the twos complement
            index += index & (-index)

    def construct(self, vals):
        for i in range(self.n):
            self.update(i, vals[i])


# use hashtable to store indices of the elements
elementIndex = defaultdict(int)
numElements = int(input())
elements = []

# Trivial - TLE
# def swap(targetPosition, current):
#     # print("swapping from indices", targetPosition, current)
#     swaps = 0
#     # if the current position is to the right of the target position - need to swap highest index to lowest
#     if current < targetPosition:
#         left = current
#         right = current + 1

#         while right <= targetPosition:
#             aValue = elements[left]
#             bValue = elements[right]
#             elementIndex[aValue], elementIndex[bValue] = elementIndex[bValue], elementIndex[aValue]
#             elements[left], elements[right] = elements[right], elements[left]
#             left += 1
#             right += 1
#             swaps += 1
#     # if the current position is to the left of the target position - need to swap lowest index to highest
#     elif current > targetPosition:
#         right = current
#         left = current - 1

#         while left >= targetPosition:
#             aValue = elements[left]
#             bValue = elements[right]
#             elementIndex[aValue], elementIndex[bValue] = elementIndex[bValue], elementIndex[aValue]
#             elements[left], elements[right] = elements[right], elements[left]

#             left -= 1
#             right -= 1
#             swaps += 1

#     # if they are equal then we don't need to swap anything
#     return swaps


fenwick = FenwickTree(totalLength)

# i is the number relevant to the index - does not matter in the Fenwick Tree because we can just remove the ++ in index above
for i in range(1, numElements + 1):
    element = int(input())
    elements.append(element)
    elementIndex[element] = i  # save the position of the element found
    # update the position by 1 - increased the number of swaps
    fenwick.update(i, 1)

left = 0
right = numElements - 1

oddNumber = 1
evenNumber = numElements
for phase in range(1, numElements+1):
    # odd phases sort on the beginning
    if phase % 2 == 1:
        targetPosition = left
        target = oddNumber
        # the target of the value to shift - we have to shift it all the way to the left
        # -1 because we lose the amount of potential swaps needed - the edges are always 0 swaps and converges
        fenwick.update(elementIndex[target], -1)
        # the swaps required up to the position of the value we are targeting - no need to take difference
        swaps = fenwick.sumValues(elementIndex[target])
        oddNumber += 1
        left += 1

    # even phases sort on the end
    else:
        targetPosition = right
        target = evenNumber
        # same as above - but on the right side - update all swapping positions by reducing the number by 1
        fenwick.update(elementIndex[target], -1)
        # need to take the difference because we will have extra swaps from 0 to the lower bound
        swaps = fenwick.sumValues(numElements) - \
            fenwick.sumValues(elementIndex[target] - 1)
        evenNumber -= 1
        right -= 1
    # print("Current position", targetPosition, "swapping for target", target)
    # first sorting - get the index of the value to swap
    print(swaps)

    # swaps = swap(targetPosition, current) # swaps all elements between indices left and right
    # print(swaps)
    # the value 1 should be moved to index 0 - value of N should move to position n - 1

# test fenwick tree
# array = [2, 2, 3, 4, 1, 6]
# fenwick = FenwickTree(len(array))
# fenwick.construct(array)

# print(fenwick.sumValues(2))
# print(fenwick.tree)
# fenwick.update(0, -2)
# print(fenwick.tree)
# print(fenwick.sumValues(2))
