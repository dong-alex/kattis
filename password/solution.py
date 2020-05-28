"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  ( expected value ) - https://en.wikipedia.org/wiki/Expected_value

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""

numPasswords = int(input())

passwords = []
for _ in range(numPasswords):
    word, prob = input().strip('\n').split(' ')
    passwords.append((word, float(prob)))

passwords.sort(key=lambda x: x[1], reverse=True)
probability = 0
for i in range(len(passwords)):
    probability += (i+1) * passwords[i][1]
    # expected = summation of p(x) * x [value of x represented by number of tries done]
print('%.4f' % probability)
