/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (prime factors) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/primefactor.c
  (number of divisors) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/num_divisors.c
  (scanf vs cin) - https://stackoverflow.com/questions/1042110/using-scanf-in-c-programs-is-faster-than-using-cin
  (sync) - (sync) - https://stackoverflow.com/questions/31162367/significance-of-ios-basesync-with-stdiofalse-cin-tienull

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

#include <iostream>
#include <vector>
#define SIZE 2000001
using namespace std;
int c, i, k, t, num, tests;

vector<int> primes(SIZE, 0);
vector<int> factors(SIZE, 1);
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	for (i = 2; i < SIZE; i++)
	{
		if (!primes[i])
		{
			// following k * p integers are NOT prime - the next for loop iteration will detect a prime if not viisted
			for (k = 2 * i; k < SIZE; k += i)
			{
				c = 0, t = k, primes[k]++;
				// https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/num_divisors.c
				while (t % i == 0)
					c++, t /= i;
				factors[k] *= (c + 1);
			}
		}
	}
	scanf("%d\n", &tests);

	// O(K N) K = 2000001 N = test cases
	// O(K) + O(N) = O(N)
	while (tests--)
		scanf("%d\n", &num), printf("%d\n", factors[num] - primes[num]);
	return 0;
}