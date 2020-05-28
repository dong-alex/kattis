/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (prime factors) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/primefactor.c
  (number of divisors) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/num_divisors.c

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

#include <iostream>

#define MAXN 1500
#define MAXP 5000

int primes[MAXP];
int psize;

using namespace std;

void getPrimes()
{
	int i, j, isprime;

	psize = 0;
	primes[psize++] = 2;
	for (i = 3; i <= MAXN; i += 2)
	{
		for (isprime = j = 1; j < psize; j++)
		{
			if (i % primes[j] == 0)
			{
				isprime = 0;
				break;
			}
			if (1.0 * primes[j] * primes[j] > i)
				break;
		}
		if (isprime)
			primes[psize++] = i;
	}
}

int num_divisors(int n)
{
	int i, count, res = 1;

	for (i = 2; i * i <= n; i++)
	{
		count = 0;
		while (!(n % i))
		{
			n /= i;
			count++;
		}
		if (count)
			res *= (count + 1);
	}
	if (n > 1)
		res *= 2;
	return res;
}

int getPrimeFactorCount(int n)
{
	long count = 0;
	bool done = false;
	for (int i = 0; i < psize; i++)
	{
		done = false;
		while (n % primes[i] == 0)
		{
			if (!done)
			{
				count++;
				done = true;
			}
			n /= primes[i];
		}
		if (1.0 * primes[i] * primes[i] > n)
			break;
	}
	if (n > 1)
	{
		count++;
	}
	return count;
}
int main()
{
	getPrimes();
	int num, tests, solution;

	scanf("%d\n", &tests);
	while (tests--)
	{
		scanf("%d\n", &num), printf("%d\n", (num_divisors(num) - getPrimeFactorCount(num)));
	}
}