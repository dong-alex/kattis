/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (tangents on circle) - https://github.com/UAPSPC/Code-Archive/blob/master/2d_geometry/circ_tangents.c
  (solving standard form) - https://bobobobo.wordpress.com/2008/01/07/solving-linear-equations-ax-by-c-0/
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

#include <iostream>
#include <cmath>

#define SQR(x) ((x) * (x))

using namespace std;

typedef struct
{
	double x, y;
} Point;

long double dist2(Point a)
{
	return SQR(a.x) + SQR(a.y);
}

Point a, b;

void tangents(Point p)
{
	long double tmp = dist2(p);
	long double para = 1 / tmp;
	long double perp = sqrt(tmp - 1 * 1) / tmp;
	a.x = p.x * para - p.y * perp;
	a.y = p.y * para + p.x * perp;
	b.x = p.x * para + p.y * perp;
	b.y = p.y * para - p.x * perp;
}

int main()
{
	int n;
	cin >> n;
	Point c, p;

	while (n--)
	{
		scanf("%lf %lf", &p.x, &p.y);
		tangents(p);

		long double a1, b1, c1, a2, b2, c2;
		a1 = a.y - p.y;
		b1 = p.x - a.x;
		c1 = -(a.x * p.y - p.x * a.y);

		a2 = b.y - p.y;
		b2 = p.x - b.x;
		c2 = -(b.x * p.y - p.x * b.y);

		printf("(%Lf,%Lf,%Lf,%Lf,%Lf,%Lf)\n", a1, b1, c1, a2, b2, c2);
	}
	return 0;
}