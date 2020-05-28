"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (large n = linear recurrence) - https://eclass.srv.ualberta.ca/mod/page/view.php?id=4083779
  (fast exponentiation) - https://www.johndcook.com/blog/2008/12/10/fast-exponentiation/
  (fast exponentiation imp. as reference) - https://github.com/UAPSPC/Code-Archive/blob/master/arithmetic/fast_exp_mod.c
  (binary exponentiation) - https://cp-algorithms.com/algebra/binary-exp.html
  (fibonacci - recurrence) - http://www.ltcconline.net/greenl/courses/203/MatrixOnVectors/fibonacci.htm

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""
# Fibonacci Sequence - 1 1 2 3 5 8 ... mod 10^9
# linear recurrence for fibonacci would be simply fib(n) = fib(n-1) + fib(n-2) with base cases fib(0) = 0 fib(1) = fib(2) = 1
numTests = int(input())
# mod limit
LIMIT = 1 * 10 ** 9

MAXN = 281474976710656

# github repo - computres b^n mod m
# variation - calculate b^n where b is a 2x2 matrix


# def fastExp(b, n, m):
#   res = 1
#   x = b

#   while n > 0:
#       if n & 1:
#           n -= 1
#           res = (res * x) % m
#       else:
#           n >>= 1
#           x = (x * x) % m
#   return res

# for 2x2 matrices


def matrixMultiply(mat1, mat2):
  solution = [[0, 0], [0, 0]]
  solution[0][0] = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % LIMIT
  solution[0][1] = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % LIMIT
  solution[1][0] = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[0][1]) % LIMIT
  solution[1][1] = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % LIMIT
  return solution


def matrixPower():
  # fast exponentiate with matrixes - store within matrix and refer later - up to 64 bits
  # if there is a 1 in the binary of the power - we need the specific power
  base = [[1, 1], [1, 0]]
  result = [base for _ in range(64)]
  for i in range(1, 64):
      result[i] = matrixMultiply(result[i-1], result[i-1])
  return result


for _ in range(numTests):
  # number of years porpoises are live - independent per sample
  test, years = map(int, input().strip(
      '\n').split(' '))  # years is the power

  # have all constants per bit
  base = [[1, 1], [1, 0]]

  # skip the first exponent because we starte with [[1,1][1,0]]
  # for every 1 in the bit for the years - we multiply it with the current result we have i.e. ((current)^2)^2 etc.
  solution = [[1,0],[0,1]] # base identity matrix to get the first batch of offspring
  # we are off by one - we initially work with fib(1) = fib(0) so we need to normalize the years to be 0 based
  years -= 1
  while years > 0:
      # need a part of 2^i
      if years & 1:
          years -= 1
          # matrix multiply for the constant matrix
          solution = matrixMultiply(solution, base)
      # shift
      else:
        years >>= 1
        base = matrixMultiply(base, base)
  # print(test, solution[0][0]) # fib(n-1) + fib(n-2) was calculated and gave us [f(n), f(n-1)] want only f(n)
  # when we reach more than (1 * 10 ** 9) - then we remove that many porpoises
