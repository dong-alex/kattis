/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (suffix array implementation) - https://github.com/UAPSPC/Code-Archive/blob/master/string/suffix_array.cpp
  (maxing array element) - https://stackoverflow.com/questions/34315002/max-in-a-c-array
  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;

const int MaxN = 200010;
char T[MaxN];
int N;
// Index from sorted suffix i to position in string
int SA[MaxN], tempSA[MaxN];
// Rank of i in T. Used by SA[j] = i.
int RA[MaxN], tempRA[MaxN];

// Must be as large as MaxN, since possible for every character
// to have a unique rank.
int c[MaxN];
void radixSort(int k)
{ // O(n), numbers up to N, any chars
	int i, maxi = max(300, N);
	memset(c, 0, sizeof c);
	for (i = 0; i < N; ++i)
	{ // Integer rank freq
		// TODO: Mod instead if circular sorting.
		int index = i + k < N ? RA[i + k] : 0;
		c[index]++;
	}
	int sum = 0;
	for (i = 0; i < maxi; ++i)
	{
		int t = c[i];
		c[i] = sum;
		sum += t;
	}
	for (i = 0; i < N; ++i)
	{ // Shuffle sufix array.
		// TODO: Mod if circular sorting.
		int indexToRA = SA[i] + k;
		int indexToC = indexToRA < N ? RA[indexToRA] : 0;
		tempSA[c[indexToC]++] = SA[i];
	}
	for (i = 0; i < N; ++i)
		SA[i] = tempSA[i];
}

void constructSA()
{
	int i;
	for (i = 0; i < N; ++i)
		RA[i] = T[i];
	for (i = 0; i < N; ++i)
		SA[i] = i;
	for (int k = 1; k < N; k <<= 1)
	{
		radixSort(k); // Sort based on value k indicies after
		radixSort(0); // Sort based on current value of self (stable)
		int r = 0;	// Rank, starting from 0.
		tempRA[SA[0]] = r;
		for (i = 1; i < N; ++i)
		{
			tempRA[SA[i]] =
				// Note that second condition will only be tried with non-circular sorting if SAs + k < N.
				// Otherwise they would already be different, due to sorting to the end.
				(RA[SA[i]] == RA[SA[i - 1]] && RA[(SA[i] + k) % N] == RA[(SA[i - 1] + k) % N]) ? r : ++r;
		}
		for (i = 0; i < N; ++i)
			RA[i] = tempRA[i];
		if (RA[SA[N - 1]] == N - 1)
			break; // All have unique ranks.
	}
}
// LCP[i] = prefix size that SA[i] has in common with SA[i - 1];
int LCP[MaxN];
// Last character MUST be different than all other characters!
void ComputeLCP()
{
	int Phi[MaxN], PLCP[MaxN], i;
	Phi[SA[0]] = -1;
	for (i = 1; i < N; ++i)
		Phi[SA[i]] = SA[i - 1];
	int L = 0;
	for (i = 0; i < N; ++i)
	{
		if (Phi[i] == -1)
		{
			PLCP[i] = 0;
			continue;
		}
		while (T[i + L] == T[Phi[i] + L])
			++L;
		PLCP[i] = L;
		L = max(L - 1, 0);
	}
	for (int i = 0; i < N; ++i)
		LCP[i] = PLCP[SA[i]];
}

int main()
{
	cin >> N;
	scanf("%s\n", T);

	constructSA();
	ComputeLCP();
	cout << *max_element(LCP, LCP + MaxN) << endl;
	return 0;
}