n = 5
k = 2

# # O(KN) space | O(KN) time
solution = []
for i in range(n):
    for j in range(k):
        solution.append((n, k))

n = 5

# O(N) space | O(N) time
solution = []
for i in range(n):
    for j in range(2):
        solution.append((i, j))
return solution

# SPACE COMPLEXITY - O(2N) -> O(N)
# TIME COMPLEXITY - O(2N) -> O(N)
for i in range(n):
	solution.append(i)

for j in range(n):
	solution.append(j)


def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = mergesort(arr[:mid])
	right = mergesort(arr[mid:])
	..
	..
	merge(left, right)

"""
Call stack = [mergesort([2,6,3,4,5])]

Time complexity - O(nlogn)
Space complexity - O(2N) -> O(N)

Input: [2,6,3,4,5]
Output: [2,3,4,5,6]

O(log n) - time
left = [2,6]
right = [3,4,5]

O(N/2) -> O(N/4) O(1)
Callstack = [mergesort([2,6])] -> O(N/2) -> O(N)
left = mergesort([2]) -> O(N/4) -> O(N)
right = mergesort([6])

Callstack = [mergesort([2,6,3,4,5,1,34,23,1,25,35,2,2,1]), x10] -> Size = 11 

O(N) -> O(N/2) + O(N/4) + O(N/8) ...

O(log N)

N = 8

log_2(8) = 2 x 2 x 2 => 3

INITIAL ARRAY = [1,2,3,4,5,6,7,8] where N = 8

left = mergesort([1,2,3,4]) merge
mergesort([1,2]) merge
mergesort([1]) merge
DEPTH = 3 -> Callstack = 3 Functions LONG
[mergesort([1,2,3,4]),mergesort([1,2]), mergesort([1])] 3 elements long O(LOG N) SPACE to occupy 3 elements

Callstack [EMPTY]
right = mergesort([5,6,7,8]) merge
mergesort([5,6]) merge
mergesort([5]) merge
O(LOG N)

mergesort....
mergesort....

merge O(N) * 6 O(2LOG N)

Time Complexity - Mergesort = O(2N LOG N) -> O(N LOG N)
------- SEPARATE

merge([1,2,3,4], [5,6,7,8]) - 4 + 4 = 8 -> N = N/2 + N/2
Space Complexity - O(N)
Time Complexity - O(N)

Overall space complexity - O(Log N) [call stack] + O(N) [merge] = O(N) because O(N) >> O(log n) for large N
"""

