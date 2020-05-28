"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (prime factors) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/primefactor.c
  (factorial prime factors) - https://math.stackexchange.com/questions/642216/factorials-and-prime-factors

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
# i.e. 9 divides 6!
# 6 * 5!
# 6 * 5 * 4!
# ....
# 30 * 24 = 720

# 9 = 3^2 factors 720 / 3 so its good because 9 can be represented as 3^2
# Theoretically every n >= 2 interger can be represented by prime numbers

# i.e. 27 divides 6!
# 27 prime numbers greater than 1 is = {2,3,5,7,11,13,15,17 ...} we only care about lowest ?
# 6! = 720
# 27 = 3^3

# 5! = (2 ** 2 * 2)(3)(5)
# 6! = {2,3,5} = (2^4)(3^2)(5^1) =  16 * 45 = 720
# (2^4)(3^2)(5^1) / (3^3) = (2^4)(5^1) / 3 = not whole - not divisible

# idea
# get prime factors of num and fac without the factorial
# cancel out all factors
# remainder powers below = not divislbe
# no remainder = divisible

# we only care about the shortest of the divisors
# i.e. starting from 2 and so on - the moment the divisors don't match - then its not possible
# if we ran out then its possible

from collections import defaultdict
import math

# largest value to store log(2 ** 31)
MAXN = 46340
MAXP = 5000

primes = [0 for _ in range(5000)]
psize = 0
# seive of eras.


def getPrimes():
    # reference the global value and uses it
    global psize
    primes[psize] = 2
    psize += 1
    for i in range(3, MAXN + 1, 2):
        isprime = 1
        for j in range(1, psize):
            if (i % primes[j] == 0):
                isprime = 0
                break
            if 1.0 * primes[j] * primes[j] > i:
                break
        if isprime:
            primes[psize] = i
            psize += 1

# get primary factors of n


# def getPFactor(n):
#     factorials = defaultdict(int)
#     for i in range(0, psize):
#         # while this specific prime fits in - divides it off and as a factor
#         while n % primes[i] == 0:
#             factorials[primes[i]] += 1
#             n /= primes[i]
#         if 1.0 * primes[i] * primes[i] > n:
#             break
#     # remainder is left out to the last value - itself
#     if n > 1:
#         factorials[n] = 1
#     return factorials


# def getFactorialPrimes(n):
#     factorials = defaultdict(int)
#     # check all primes
#     # 6! = (2 ** 3 * 2 * 1)
#     for i in range(0, psize):
#         # while i can get a whole prime out of the number - continue doing so
#         divisor = primes[i]
#         while n // divisor != 0:
#             # get how many time 2 ^ 1 fits then 2 ^ 2 until 0
#             factorials[primes[i]] += n // divisor
#             divisor = divisor ** 2

#         if 1.0 * primes[i] * primes[i] > n:
#             break
#     return factorials


try:
    getPrimes()
    # psize is number of primes calculated
    while (True):
        fac, num = map(int, input().strip('\n').split(' '))
        temp = num
        # returns array of prime factors - each spot is the prime factor
        # 3 ^ 2 is [3, 3 ...]
        # fPrimes = getFactorialPrimes(fac)
        # nPrimes = getPFactor(num)

        undivisible = False

        for i in range(0, psize):
            count = 0
            while num % primes[i] == 0:
                count += 1
                num /= primes[i]

            # this is the denominator - needs to contain something
            if count == 0:
                continue

            # when it does contain something - check the primes to the factorial
            # while floor(n/p) != 0
            divisor = primes[i]
            while divisor <= fac:
                count -= fac // divisor
                divisor *= divisor

            # denominator had more count of the prime[i] than the numerator = non - divisible
            if count > 0:
                undivisible = True
                break

            if 1.0 * primes[i] * primes[i] > num or 1.0 * primes[i] * primes[i] > fac:
                break

        if num > 1:
            undivisible = True

        if undivisible:
            print(str(temp) + " does not divide " + str(fac) + "!")
        else:
            print(str(temp) + " divides " + str(fac) + "!")
except:
    pass
