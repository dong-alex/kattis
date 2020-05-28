#include <iostream>

using namespace std;

long gcd_ex(long a, long b, long &s, long &t)
{
	long r0 = a, r1 = b, q;
	long s0 = 1, s1 = 0;
	long t0 = 0, t1 = 1;

	//invariant: ri = a*si + b*ti for both i = 0 and i = 1
	while (r1)
	{
		q = r0 / r1;

		r0 -= q * r1;
		swap(r0, r1);

		s0 -= q * s1;
		swap(s0, s1);

		t0 -= q * t1;
		swap(t0, t1);
	}

	//now r0 = gcd(a, b)
	s = s0;
	t = t0;

	return r0;
}

long mod_inverse(long a, long m)
{
	long s, t;

	// split off the candies a amongst m kids - what if m = 1 (1 kid)
	// anything mod 1 is 0 - 1 kid can get all the candies from the bag - return m | X - 1
	a %= m;

	/* can ignore the next line a is never nonnegative
      The current standard ensures that if m > 0 and a < 0 then
      a%m wiint be the negative number r closes to 0 such that m | (a-r).
      example: (-22) % 6 == -4
      http://en.cppreference.com/w/cpp/language/operator_arithmetic
      http://en.cppreference.com/w/cpp/numeric/math/div
    */
	if (a < 0)
		a += m;
	if (gcd_ex(a, m, s, t) > 1)
		return -1;

	// solve for the value
	s %= m;

	if (s < 0)
		s += m;

	return s;
}

int main()
{
	long tests, kids, candies, tempS, tempT, bags;
	scanf("%ld\n", &tests);
	while (tests--)
	{
		scanf("%ld %ld\n", &kids, &candies);
		// kids = 1 - if more than 1 candy per bag - just one bag and COULD give the 1 candy
		if (kids == 1)
		{
			// at least one kid will lose the candy - this kid will lose it
			printf("%d\n", candies > 1 ? 1 : 2);
		}
		else if (candies == 1)
		{
			printf("%ld\n", kids + 1);
		}
		else
		{
			bags = mod_inverse(candies, kids);
			if (bags == -1)
			{
				printf("%s\n", "IMPOSSIBLE");
			}
			else
			{
				printf("%ld\n", bags);
			}
		}
	}
	return 0;
}
