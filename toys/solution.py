"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (Josephus ring survivor references) - https://github.com/UAPSPC/Code-Archive/blob/master/combinatorics/josephus.c

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
numToys, skips = map(int, input().strip('\n').split(' '))
survivor = 0
prev = 0
for i in range(2, numToys+1):
    survivor = (prev + (skips % i)) % i
    prev = survivor
print(survivor)
