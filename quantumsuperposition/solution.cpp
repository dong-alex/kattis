// DAG - need to go from start -> end under a given step limit
#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <algorithm>
#include <queue>

#define MAXN 1005

using namespace std;

void topologicalSort(int n, int m, vector<vector<int>> &universe, vector<vector<int>> &memo)
{
	// get the number of degrees from the adjacency list
	vector<int> degrees(n, 0);

	// get the amount of degrees per point
	for (auto i : universe)
	{
		for (auto j : i)
		{
			// every list of i - there is an edge u -> v (track the number of v's indegree)
			degrees[j]++;
		}
	}

	// topological sort using BFS
	queue<int> q;

	// base case 1 1 represents
	memo[0][0] = 1;
	// start index always at 0 - go up to n
	q.push(0);
	while (!q.empty())
	{
		int current = q.front();
		q.pop();

		// check all edges of the current node - u is list of all nodes from current -> u
		for (auto u : universe[current])
		{
			printf("Searching Edge %d %d\n", current + 1, u + 1);

			for (int v = 0; v < m; v++)
			{
				// check all possible current -> _____ edges and see if it is available basic 0 0 is accessible
				// if the initial vertext (current) can approach to vertex (v)
				if (memo[current][v])
				{
					// would indicate the current -> u -> v + 1 is then approachable
					memo[u][v + 1] = 1;
				}
			}
			// accessed all nodes to the node we are searching in - add into queue
			if (!--degrees[u])
			{
				q.push(u);
			}
		}
	}

	// indicates that we can reach to the last row (n1 vertice) from the corresponding edges
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			printf("%d ", memo[i][j]);
		}
		printf("\n");
	}
}
int main()
{
	/*
	n1 - number of vertices in universe 1 - start index = 1 | end index = n1
	n2 - number of vertices in universe 2 - start index = 2 | end index = n2

	m1 - number of edges in universe 1
	m2 - number of edges in universe 2

	constriant - num of steps in universe 1 + num of steps in universe 2 = query
	*/
	long n1, n2, m1, m2, v1, v2, v3, v4, queries, steps;
	scanf("%ld %ld %ld %ld\n", &n1, &n2, &m1, &m2);

	// adjacency lists
	vector<vector<int>> u1(n1);
	vector<vector<int>> u2(n2);

	// track which values is accessible
	vector<vector<int>> memo1(n1, vector<int>(m1, false));
	vector<vector<int>> memo2(n2, vector<int>(m2, false));
	// add universe 1 edges - DAG
	for (int i = 0; i < m1; i++)
	{
		// scanf("%d %d\n", &v1, &v2);
		cin >> v1 >> v2;
		u1[v1 - 1].push_back(v2 - 1);
	}

	// add universe 2 edges - DAG
	for (int i = 0; i < m2; i++)
	{
		// scanf("%d %d\n", &v1, &v2);
		cin >> v1 >> v2;
		u2[v1 - 1].push_back(v2 - 1);
	}

	topologicalSort(n1, m1, u1, memo1);
	// for (int i = 0; i < n1; i++)
	// 	printf("%d ", top[i] + 1);
	// printf("\n");
	topologicalSort(n2, m2, u2, memo2);
	// get all the possible sums
	set<int> s;
	for (int i = 0; i < m1 + 1; i++)
	{
		for (int j = 0; j < m2 + 1; j++)
		{
			// check if edge i and edge j approachable to the final vertext n1 -1 and n2 -1 (indexed)
			if (memo1[n1 - 1][i] && memo2[n2 - 1][j])
			{
				s.insert(i + j);
			}
		}
	}
	// determine the number of steps possible from start to end for both universes
	// use topological sort to traverse a DAG from start to end
	scanf("%ld\n", &queries);
	for (int i = 0; i < queries; i++)
	{
		scanf("%ld\n", &steps);
		if (s.count(steps) > 0)
		{
			cout << "Yes" << endl;
		}
		else
		{
			cout << "No" << endl;
		}
		// find out if the steps are good enough - using some path where u1 + u2 = steps
	}
	return 0;
}
