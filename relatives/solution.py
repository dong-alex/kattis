"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (Euler Phi) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/eulerphi.c
  (Euler Phi information) - https://cp-algorithms.com/algebra/phi-function.html
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""

# returns number of positive intgers less than N relatively prime to N
# computes via factorization of n ( decomposing n into a product of its prime numbers i.e. p1 ** a1 + p2 ** a2 etc.)


def eulerPhi(n):
    i = 2
    res = 1

    # equivalent to i < sqrt(n)
    while i*i <= n:
        count = 0
        # count how many times 'i' goes into our value n - these are not our prime because they are now divisible
        # i is the x in a = x*y and count is the y
        while n % i == 0:
            n /= i
            count += 1

        # exactly p ** k / p numbers between 1 and p ** k
        if count > 0:
            res *= (pow(i, count) - pow(i, count - 1))

        i += 1
    if n > 1:
        # the EulerPhi of a prime number is just n - 1 (all the values from 1 -> n excluding itself)
        res *= n - 1
    return res


try:
    while (True):
        n = int(input())
        solution = eulerPhi(n)
        if solution > 1:
            print(int(solution))

except:
    pass
