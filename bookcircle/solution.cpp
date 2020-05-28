/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (bipartite matching - minimum vertex cover (covers all books with minimum presentations)) - https://github.com/UAPSPC/Code-Archive/blob/master/graph/minpath_vertexcover.cc

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

// left side can be for boys - right side can be for girls
// use bipartite matching to get the pair of presentations needed - will create all the matching needed - extra books results in more presentations which we dont want

#include <iostream>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

#define MAXN 2050

char e[MAXN][MAXN]; /* MODIFIED Adj. matrix (see note) */
long match[MAXN], back[MAXN], q[MAXN], tail;

void addEdge(long x, long y, long n)
{
	e[x][y + n] = e[y + n][x] = 1;
}

long find(long x, long n, long m)
{
	long i, j, r;

	if (match[x] != -1)
		return 0;
	memset(back, -1, sizeof(back));
	for (q[i = 0] = x, tail = 1; i < tail; i++)
		for (j = 0; j < n + m; j++)
		{
			if (!e[q[i]][j])
				continue;
			if (match[j] != -1)
			{
				if (back[j] == -1)
				{
					back[j] = q[i];
					back[q[tail++] = match[j]] = j;
				}
			}
			else
			{
				match[match[q[i]] = j] = q[i];
				for (r = back[q[i]]; r != -1; r = back[back[r]])
					match[match[r] = back[r]] = r;
				return 1;
			}
		}
	return 0;
}

void bipmatch(long n, long m)
{
	long i;
	memset(match, -1, sizeof(match));
	for (i = 0; i < n + m; i++)
		if (find(i, n, m))
			i = 0;
}

int main()
{
	long n, m, x, y, numBooks, count, i;
	char name[100], bookName[100];

	scanf("%ld %ld", &n, &m); /* n = number of vertices */ /* m = number of edges */
	// boys
	map<string, long> map;
	for (i = 0; i < n; i++)
	{
		cin >> name >> numBooks;
		for (long j = 0; j < numBooks; j++)
		{
			cin >> bookName;
			map.insert({bookName, i});
		}
	}
	// girls
	for (i = 0; i < m; i++)
	{
		cin >> name >> numBooks;
		for (long j = 0; j < numBooks; j++)
		{
			cin >> bookName;
			addEdge(map.at(bookName), i, n);
		}
	}

	bipmatch(n, m);
	for (count = i = 0; i < n; i++)
	{
		if (match[i] != -1)
		{
			count++;
		}
	}
	printf("%ld\n", count);
	return 0;
}