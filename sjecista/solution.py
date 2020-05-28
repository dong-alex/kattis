"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (binomial theorem) - https://github.com/UAPSPC/Code-Archive/blob/master/combinatorics/binomial.c
  (combination w/ binomial) - https://en.wikipedia.org/wiki/Combination
  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

# consider n = 4, we get one intersection

# if n = 5 and we have 4 vertices from there, there will be an intersection from it

# vertices = {1,2,3,4,5}
# if set = {1,2,3,4} then we have 1 intersection
# if set = {1,2,3,5} then we have 1 intersection

# calculate how many combinations of 4 vertices in the set then that will be intersections for 5
# if n == 3 then we get 0 because we need 2 line segments from 4 points to create an intersection

# only going to 100th degree
binomial = [[0 for _ in range(100)] for _ in range(100)]

# converted from C++ programming repo
def getBinomial(vertices):
    for k in range(0, 100):
        binomial[k][0] = 1
        binomial[k][k] = 1
        for i in range(1, k):
            binomial[k][i] = binomial[k-1][i-1]+binomial[k-1][i]

vertices = int(input())
if vertices <= 3:
	print(0)
else:
	# get number of combinations of 4
	getBinomial(vertices)
	print(binomial[vertices][4])