/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (Lowest common ancestor + distance ) - https://github.com/UAPSPC/Code-Archive/blob/master/graph/lca.cpp
  (binary lifting code from G4G) - https://www.geeksforgeeks.org/lca-in-a-tree-using-binary-lifting-technique/
  (documentation about LCA/binary lift) - https://cp-algorithms.com/graph/lca_binary_lifting.html
 
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
#include <cmath>
#include <cassert>
#include <set>
#include <cstring>
#include <queue>

using namespace std;

constexpr int log2(int n)
{
	int c = 0;
	while (n >>= 1)
		c++;
	return c;
}

// Pre-processing to calculate values of memo[][]
void dfs(int u, int p, int **memo, int *lev, int n, vector<int> *g)
{
	// Using recursion formula to calculate
	// the values of memo[][]
	memo[u][0] = p;

	for (int i = 1; i <= log2(n); i++)
		memo[u][i] = memo[memo[u][i - 1]][i - 1];

	for (int v : g[u])
	{
		if (v != p)
		{
			lev[v] = lev[u] + 1;
			dfs(v, u, memo, lev, n, g);
			//            cout << "Depth of " << v << " is " << lev[v] << endl;
		}
	}
}

// Function to return the LCA of nodes u and v
int lca(int u, int v, int n, int *lev, int **memo)
{
	// The node which is present farthest
	// from the root node is taken as u
	// If v is farther from root node
	// then swap the two
	if (lev[u] < lev[v])
		swap(u, v);

	// Finding the ancestor of u
	// which is at same level as v
	for (int i = log2(n); i >= 0; i--)
		if ((lev[u] - (1 << i)) >= lev[v])
			u = memo[u][i]; // move the parent up

	// If v is the ancestor of u
	// then v is the LCA of u and v
	//    cout << u << " " << lev[u] << " with " << v << " " << lev[v] << endl;
	assert(lev[u] == lev[v]);
	if (u == v)
		return u;

	// Finding the node closest to the root which is
	// not the common ancestor of u and v i.e. a node
	// x such that x is not the common ancestor of u
	// and v but memo[x][0] is
	for (int i = log2(n); i >= 0; i--)
	{
		if (memo[u][i] != memo[v][i])
		{
			u = memo[u][i];
			v = memo[v][i];
		}
	}

	// Returning the first ancestor
	// of above found node
	assert(memo[u][0] == memo[v][0]);
	return memo[u][0];
}

long depth(int u, int v, int n, int *lev, int **memo)
{
	int a = lca(u, v, n, lev, memo);
	return (lev[u] + lev[v]) - (2 * lev[a]) + 1;
}

int main()
{
	// Number of nodes
	int n;
	vector<bool> visited;
	cin >> n;
	// vector to store tree
	vector<int> g[n + 1];
	int **memo = new int *[n + 1];
	for (int i = 0; i < n + 1; i++)
		memo[i] = new int[log2(n) + 1];

	// Stores the level of each node
	int *lev = new int[n + 1];
	// Initialising memo values with -1
	for (int i = 0; i <= n; i++)
		memset(memo[i], -1, sizeof memo[i]);

	// Add edges - from input file
	for (int i = 0; i < n - 1; i++)
	{
		int u, v;
		cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u);
	}
	// preprocess under O(NlogN) time for binary lifting
	// dfs(1, 1, memo, lev, n, g);

	visited.resize(n + 1, false);
	queue<int> q;
	q.push(1);
	visited[1] = true;

	while (q.size() != 0)
	{
		int current = q.front();
		q.pop();

		for (int child : g[current])
		{
			if (!visited[child])
			{
				visited[child] = true;
				memo[child][0] = current;
				lev[child] = lev[current] + 1;
				q.push(child);
			}
		}
	}

	// construct bonds via binary lift
	for (int i = 1; i <= log2(n); i++)
	{
		// check the above height and see if it connects first
		for (int j = 1; j <= n; j++)
		{
			if (memo[j][i - 1] != -1)
			{
				// the parent of j is indexed above it
				memo[j][i] = memo[memo[j][i - 1]][i - 1];

				// update the depth of the value j
			} // check 1 height above itself
		}
	}

	// query
	long total = 0;
	for (int i = 1; i <= n; i++)
	{
		// for each value of n [1, n] - calculate factors
		for (int j = 2 * i; j <= n; j += i)
		{
			total += depth(i, j, n, lev, memo);
		}
	}
	cout << total << endl;
	return 0;
}