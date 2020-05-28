/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (bridge/articulation points) - https://github.com/UAPSPC/Code-Archive/blob/master/graph/bridges.cc
  (pair comparison - similar to tuple in python) - https://www.quora.com/How-do-I-use-C++-STL-to-check-if-a-pair-exists-in-the-vector-of-pairs

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

// find all the bridges of a graph - remove those edges - then find the number of juncitons visited - that is the total

// articulation point vs bridge = vertex | edge removal results in disconnected graph
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

#define MAX_N 10001
#define min(a, b) (((a) < (b)) ? (a) : (b))

using namespace std;

typedef struct
{
	int deg;
	int adj[MAX_N];
} Node;

Node alist[MAX_N];
bool art[MAX_N];
vector<bool> visited(MAX_N, false);

int df_num[MAX_N], low[MAX_N], father[MAX_N], c;
vector<pair<int, int>> bridgeGraph;
void add_edge(int v1, int v2)
{
	alist[v1].adj[alist[v1].deg++] = v2;
	alist[v2].adj[alist[v2].deg++] = v1;
}

void add_bridge(int v1, int v2)
{
	bridgeGraph.push_back(make_pair(v1, v2));
}

void search(int v, bool root)
{
	int w, child = 0;

	low[v] = df_num[v] = c++;

	for (int i = 0; i < alist[v].deg; ++i)
	{
		w = alist[v].adj[i];

		if (df_num[w] == -1)
		{
			father[w] = v;
			++child;
			search(w, false);
			if (low[w] > df_num[v])
				add_bridge(v, w);
			if (low[w] >= df_num[v] && !root)
				art[v] = true;
			low[v] = min(low[v], low[w]);
		}
		else if (w != father[v])
		{
			low[v] = min(low[v], df_num[w]);
		}
	}

	if (root && child > 1)
		art[v] = true;
}

void articulate(int n)
{
	int child = 0;

	for (int i = 0; i < n; ++i)
	{
		art[i] = false;
		df_num[i] = -1;
		father[i] = -1;
	}

	c = 0;

	search(0, true);
}

int traverse(int v)
{
	if (visited[v])
	{
		return 0;
	}
	visited[v] = true;
	int temp = 1;

	for (int i = 0; i < alist[v].deg; i++)
	{
		if (!visited[alist[v].adj[i]])
		{
			pair<int, int> edge = make_pair(v, alist[v].adj[i]);
			// if the current edge is not a bridge
			if (find(bridgeGraph.begin(), bridgeGraph.end(), edge) == bridgeGraph.end())
			{
				temp += traverse(alist[v].adj[i]);
			}
		}
	}
	return temp;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m, v1, v2, c = 0;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; ++i)
	{
		scanf("%d %d", &v1, &v2);
		add_edge(v1, v2);
	}
	articulate(n);
	// traverse the original graph - starts with 1 because 0 is a junction
	printf("%d\n", traverse(0));
	return 0;
}
