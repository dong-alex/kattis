/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  N/A

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

*/

#include <iostream>

using namespace std;

char completeBoard[5][5] = {{'1', '1', '1', '1', '1'}, {'0', '1', '1', '1', '1'}, {'0', '0', ' ', '1', '1'}, {'0', '0', '0', '0', '1'}, {'0', '0', '0', '0', '0'}};
int directionX[8] = {2, 2, -2, -2, 1, 1, -1, -1};
int directionY[8] = {1, -1, 1, -1, 2, -2, 2, -2};
char board[5][5];

bool isSolved()
{
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (completeBoard[i][j] != board[i][j])
			{
				return false;
			}
		}
	}
	return true;
}

bool isValid(int i, int j, int x, int y)
{
	// chekcs if new position is the same as previous and valid - don't want to go backwards - infinite loop
	return ((0 <= i && i < 5 && 0 <= j && j < 5) && !(i == x && j == y));
}

int dfs(int i, int j, int oldX, int oldY, int depth)
{
	// custom limit
	if (depth > 10)
	{
		return 100;
	}
	// base case - solved board requires 0 depth to go into
	if (isSolved())
	{
		return 0;
	}

	// check every valid direction
	int t = 100;
	for (int a = 0; a < 8; a++)
	{
		int newX = i + directionX[a];
		int newY = j + directionY[a];

		if (isValid(newX, newY, oldX, oldY))
		{
			// swap values first - recurse - swap back - backtracking
			swap(board[i][j], board[newX][newY]);
			// add 1 to the depth given - recursive returning
			t = min(t, 1 + dfs(newX, newY, i, j, depth + 1));
			swap(board[i][j], board[newX][newY]);
		}
	}
	return t;
}
int main()
{
	int tests;
	string s;
	cin >> tests;
	// some empty line ???
	getline(cin, s);

	int startX, startY, depth;

	while (tests--)
	{
		// gets the first line
		for (int i = 0; i < 5; i++)
		{
			getline(cin, s);
			for (int j = 0; j < 5; j++)
			{
				board[i][j] = s[j];
				if (s[j] == ' ')
				{
					startX = i;
					startY = j;
				}
			}
		}

		depth = dfs(startX, startY, startX, startY, 0);

		if (depth > 10)
		{
			printf("Unsolvable in less than 11 move(s).\n");
		}
		else
		{
			printf("Solvable in %d move(s).\n", depth);
		}
	}
}
