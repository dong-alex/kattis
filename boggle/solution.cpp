
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

double numWords;
int numBoards;

// index with length
vector<int> wordScores = {0, 0, 0, 1, 1, 2, 3, 5, 11};
// index with 8 positions
vector<int> xDir = {0, -1, -1, 1, -1, 1, 0, 1};
vector<int> yDir = {-1, -1, 1, 0, 0, 1, 1, -1};
unordered_set<string> found;
// setup visited array
vector<vector<bool>> visited(4, vector<bool>(4, false));
vector<vector<char>> board;

bool isValid(int r, int c, string s, int index)
{
	return !(r < 0 || c < 0 || r == 4 || c == 4 || visited[r][c] || board[r][c] != s[index]);
}

bool dfs(int row, int column, string &s, int length)
{
	// if we found the string
	if (length == s.length())
	{
		return true;
	}

	visited[row][column] = true;
	bool wordFound = false;
	// valid position - traverse all potential directions
	for (int i = 0; i < 8; i++)
	{
		int newRow = row + xDir[i];
		int newCol = column + yDir[i];
		// recurse on choice

		if (isValid(newRow, newCol, s, length))
		{
			// if word was found prior - skip dfs
			wordFound = wordFound || dfs(newRow, newCol, s, length + 1);
		}
	}

	// rescind
	visited[row][column] = false;

	return wordFound;
}

int main()
{
	scanf("%lf\n", &numWords);
	char dummy;
	char word[9];
	vector<string> words;
	for (int i = 0; i < numWords; i++)
	{
		scanf("%s\n", &word);
		words.push_back(word);
	}

	cin >> numBoards;

	// per board test case
	for (int _ = 0; _ < numBoards; _++)
	{
		found.clear();
		board.resize(4, vector<char>(4));
		visited.resize(4, vector<bool>(4, false));
		// read the board
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> board[i][j];
			}
		}

		// check for every word in the current board
		// iterate through each letter in the board
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				for (string word : words)
				{
					if (found.find(word) != found.end())
					{
						continue;
					}

					if (board[i][j] == word[0] && dfs(i, j, word, 1))
					{
						found.insert(word);
					}
				}
			}
		}

		// track the best solution here
		long score = 0, total = 0;
		string solution = "";
		for (string word : found)
		{
			// do work here when we found
			if (solution.length() < word.length())
			{
				solution = word;
			}
			else if (solution.length() == word.length() && word < solution)
			{
				solution = word;
			}
			// if we didn't find anything - count the scores
			score += wordScores[word.length()];
			total += 1;
			// output solution here
		}
		printf("%ld %s %ld\n", score, solution.c_str(), total);
	}
}