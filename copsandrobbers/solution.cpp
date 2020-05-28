
/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  () - https://github.com/UAPSPC/Code-Archive/blob/master/graph/minpath_vertexcover.cc

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

// minimize the cost of the barricades on the grid - minimum algorithm - block the flow of the robbers
// maximum s - t flow value equal the minimum s-t cut capacity

// calculate the maximum flow of the graph

#include <iostream>
#include <vector>

using namespace std;

#define MAXN 200
const int Inf = 1e9;

typedef struct
{
	int v, cap, flow;
} Edge;

vector<Edge> g[MAXN];
int pred[MAXN], maxcap[MAXN], S[MAXN];

void addEdge(int u, int v, int cap)
{
	size_t i;
	Edge e;

	for (i = 0; i < g[u].size(); i++) /* Add cap if edge exists */
		if (g[u][i].v == v)
		{
			g[u][i].cap += cap;
			return;
		}

	e.v = v;
	e.cap = cap;
	e.flow = 0;
	g[u].push_back(e); /* Add edge u->v */

	for (i = 0; i < g[v].size(); i++) /* Add dummy reverse edge */
		if (g[v][i].v == u)
			return;

	e.v = u;
	e.cap = 0;
	g[v].push_back(e);
}

/* Should only be used when know that the edge between the two nodes is only added once */
void addUniqueEdge(int u, int v, int cap)
{
	Edge e;

	/* Add edge u->v */
	e.v = v;
	e.cap = cap;
	e.flow = 0;
	g[u].push_back(e);

	/* Add reverse edge v->u */
	e.v = u;
	e.cap = 0;
	g[v].push_back(e);
}

Edge *getEdge(int u, int v)
{
	for (size_t i = 0; i < g[u].size(); i++)
		if (g[u][i].v == v)
			return &g[u][i];
	return 0;
}

int maxflow(int n, int source, int sink)
{
	vector<int> q;
	int i, v, flow, inc;
	size_t j;
	Edge *e1, *e2;

	for (i = 0; i < n; i++)
		for (j = 0; j < g[i].size(); j++)
			g[i][j].flow = 0; /* Clear all flows */

	flow = 0;

	while (1)
	{ /* BFS to find augmenting path */
		memset(S, 0, sizeof(S));
		S[source] = 1;
		q.clear();
		q.push_back(source);
		for (i = 0; i < (int)q.size(); i++)
		{
			v = q[i];
			if (v == sink)
				break;
			for (j = 0; j < g[v].size(); j++)
			{
				Edge e = g[v][j];
				if (S[e.v])
					continue;
				if (e.cap && e.flow < e.cap)
				{
					q.push_back(e.v);
					S[e.v] = 1;
					pred[e.v] = v;
					maxcap[e.v] = e.cap - e.flow;
				}
				else
				{
					e1 = getEdge(e.v, v);
					if (e1 && e1->cap && e1->flow > 0)
					{
						q.push_back(e.v);
						S[e.v] = 1;
						pred[e.v] = v;
						maxcap[e.v] = e1->flow;
					}
				}
			}
		}
		if (v != sink)
			break; /* No more augmenting paths */

		/* Calculate flow */
		for (inc = Inf, v = sink; v != source; v = pred[v])
			inc = min(inc, maxcap[v]);
		flow += inc;

		/* Update flow */
		for (v = sink; v != source; v = pred[v])
		{
			e1 = getEdge(pred[v], v);
			e2 = getEdge(v, pred[v]);

			if (e1 && e1->cap)
				e1->flow += inc;
			else if (e2 && e2->cap)
				e2->flow -= inc;

			if (e1 && e2 && e1->flow && e2->flow)
			{
				if (e1->flow > e2->flow)
				{
					e1->flow -= e2->flow;
					e2->flow = 0;
				}
				else
				{
					e2->flow -= e1->flow;
					e1->flow = 0;
				}
			}
		}
	}
	return flow;
}

int main()
{
	int n, m, c;
	cin >> n >> m >> c;

	vector<string> board(m);
	// lines to go through
	for (auto &i : board)
	{
		cin >> i;
		printf("%d\n", i);
	}
	// terratin pricing
	vector<int> cost(c);
	// lines to go through
	for (auto &i : cost)
	{
		cin >> i;
	}
	return 0;
}
// int n;		/* Number of vertices */
// int m;		/* Number of edges */
// int source; /* Source of the flow */
// int sink;   /* Sink of the flow */
// int flow;   /* The value of the max flow */
// int i, u, v, cap;

// /* n = # of vertices,  m = # of edges */
// while (scanf("%d %d %d %d", &n, &m, &source, &sink) == 4)
// {

// 	/* Clear graph */
// 	for (i = 0; i < n; i++)
// 		g[i].clear();

// 	/* Read in m edges */
// 	for (i = 0; i < m; i++)
// 	{
// 		scanf("%d %d %d", &u, &v, &cap);
// 		addEdge(u, v, cap);
// 	}

// 	flow = maxflow(n, source, sink);

// 	printf("The maximum flow: %d\n", flow);
// 	printf("Min-cut edges:\n");
// 	for (i = 0; i < n; i++)
// 		if (S[i] == 1)
// 		{
// 			for (size_t j = 0; j < g[i].size(); j++)
// 				if (S[g[i][j].v] == 0)
// 					printf("(%d->%d)\n", i, g[i][j].v);
// 		}
// 	printf("Flow values:\n");
// 	for (i = 0; i < n; i++)
// 		for (size_t j = 0; j < g[i].size(); j++)
// 			printf("(%d->%d): %d/%d\n", i, g[i][j].v, g[i][j].flow, g[i][j].cap);
// }
