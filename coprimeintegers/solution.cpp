/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (prime factors) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/primefactor.c
  (factorial prime factors) - https://math.stackexchange.com/questions/642216/factorials-and-prime-factors
  (iterative GCD) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/gcd.cpp
  (num theor slides) - https://eclass.srv.ualberta.ca/pluginfile.php/5719021/mod_resource/content/1/403_numtheory_2020_nopause.pdf
  (euler phi prime < N) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/eulerphi.c

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

#define MAXN 10000001
using namespace std;

vector<vector<bool>> visited(MAXN, vector<bool>(MAXN, false));

int GCD(int a, int b)
{
	while (b)
	{
		a %= b;
		swap(a, b);
	}
	return a;
}

int phi(int n, int lower, int upper)
{
	int i, count, res = 1;

	for (i = 2; i * i <= n; i++)
	{
		count = 0;
		while (n % i == 0)
		{
			n /= i;
			count++;
		}
		if (count > 0)
			res *= (pow(i, count) - pow(i, count - 1));
	}
	if (n > 1)
		res *= (n - 1);
	return res;
}

int main()
{
	long a, b, c, d;
	cin >> a >> b >> c >> d;

	// GCD(12, 12) = 12
	// GCD(X, 1) = 1
	// all primes not a prime factor of 12 is a potential pair
	// check all pairs of each other and compute GCD.
	// GCD(a,b) = GCD(a - b, b) if a >= b - anyhthing divides a and b also divides a +/- b
	// GCD(a, b) = GCD(b, a mod b)
	int solution = 0;
	// GCD(a, b) = GCD(b, a)
	for (int i = a; i <= b; i++)
	{
		for (int k = c; k <= d; k++)
		{
			if (visited[i][k] || visited[k][i])
			{
				continue;
			}

			// add the combination in
			visited[i][k] = true;
			visited[k][i] = true;

			if (GCD(i, k) == 1)
			{
				solution++;
			}
		}
	}
	printf("%d\n", solution);
}