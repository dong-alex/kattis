/*
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

*/

#include <iostream>

#define MAXN 46340
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

bool isDivisible(long long fac, long long num)
{
	// faster checks.
	if ((fac == 0 && num != 1) || num == 0)
	{
		return false;
	}

	if ((fac == 0 && num == 1) || num == 1)
	{
		return true;
	}
	// for every prime - check how many primes needed per - if fPrimes < nPrimes - return false
	// check primes ** 2 <= num - sqrt(n)
	long long temp = num;
	for (int i = 0; i < psize; i++)
	{

		// skip primes that are not divisible - no point of checking
		if (num % primes[i] != 0)
		{
			continue;
		}

		int count = 0;

		// handle num count - denominator
		while (num % primes[i] == 0)
			count++, num /= primes[i];

		// handle fac count - numerator
		long long d = primes[i];
		while (d <= fac)
			count -= fac / d, d *= primes[i];

		// if we have more values in denominator than the numerator - non-divisible
		if (count > 0)
			return false;

		if (1.0 * primes[i] * primes[i] > temp || 1.0 * primes[i] * primes[i] > fac)
			break;
	}

	// if num is not represented as a prime - we are left with 1 (that we excluded!) - check if this is part of the primes used in factorial i.e. num < factorial
	return !(num != 1 && num > fac);
}

int main()
{
	getPrimes();
	long long fac, num;
	while (scanf("%lld %lld", &fac, &num) == 2)
	{
		if (isDivisible(fac, num))
		{
			cout << num << " divides " << fac << "!" << endl;
		}
		else
		{
			cout << num << " does not divide " << fac << "!" << endl;
		}
	}
}