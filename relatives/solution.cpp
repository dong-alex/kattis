/*
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

*/
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;
int phi(int n)
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
	long n;
	while (cin >> n)
	{
		int p = phi(n);
		if (p > 1)
		{
			cout << p << endl;
		}
	}

	return 0;
}