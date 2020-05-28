"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  N/a

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
from collections import deque
import heapq

def getPossibility(isStack, isQueue, isPQ):
    count = 0
    if isStack:
        count += 1
    if isQueue:
        count += 1
    if isPQ:
        count += 1
    return count

try:
    while True:
        numCommands = int(input())

        # initialize potential data structures - if it does not match properly then its not the right structure
        stack, isStack = [], True
        queue, isQueue = deque([]), True
        heap, isPQ = [], True

        for _ in range(numCommands):
            command, value = map(int, input().strip('\n').split(' '))
            if command == 1:
                # throw element into
                stack.append(value)
                queue.appendleft(value)
                heapq.heappush(heap, -value)
            else:
                # if invalid command not possible to find out
                # if the conditions aren't satisfied then they aren't those data structures
                if isStack and len(stack) != 0 and stack[-1] == value:
                    stack.pop()
                else:
                    isStack = False

                if isQueue and len(queue) != 0 and queue[-1] == value:
                    queue.pop()
                else:
                    isQueue = False

                if isPQ and len(heap) != 0 and abs(heap[0]) == value:
                    heapq.heappop(heap)
                else:
                    isPQ = False

        n = getPossibility(isStack, isQueue, isPQ)

        # more than one possibility
        if n > 1:
            print("not sure")
        # one possible
        elif n == 1:
            if isStack:
                print("stack")

            if isQueue:
                print("queue")

            if isPQ:
                print("priority queue")
        # no possbility
        else:
            print("impossible")

except EOFError:
    pass
