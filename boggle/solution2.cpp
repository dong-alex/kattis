/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (trie insert) - https://www.geeksforgeeks.org/trie-insert-and-search/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/
#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;

long numWords;
long numBoards;

// index with length
vector<int> wordScores = {0, 0, 0, 1, 1, 2, 3, 5, 11};
// index with 8 positions
vector<int> xDir = {0, -1, -1, 1, -1, 1, 0, 1};
vector<int> yDir = {-1, -1, 1, 0, 0, 1, 1, -1};
unordered_set<string> found;
// setup visited array
vector<vector<bool>> visited(4, vector<bool>(4, false));
vector<vector<char>> board;
long score, total;
string solution = "";

struct TrieNode
{
	vector<TrieNode *> children;
	bool isWord;
	TrieNode()
	{
		isWord = false;
		children = vector<TrieNode *>(26, NULL);
	}

	TrieNode *getChild(char letter)
	{
		return children[letter] ? children[letter] : NULL;
	};
};

void insert(TrieNode *root, string word)
{
	TrieNode *current = root;

	for (int i = 0; i < word.length(); i++)
	{
		int index = word[i] - 'A';
		if (!current->children[index])
		{
			current->children[index] = new TrieNode();
		}
		current = current->children[index];
	}
	current->isWord = true;
	// cout << "Added the word " << word << endl;
}

bool contains(TrieNode *root, char letter)
{
	return root->children[letter - 'A'] == NULL;
}

TrieNode *getChild(TrieNode *root, char letter)
{

	return root->children[letter - 'A'];
}

bool isValid(int r, int c)
{
	return !(r < 0 || c < 0 || r == 4 || c == 4 || visited[r][c]);
}

void dfs(int row, int col, TrieNode *currentNode, string word)
{
	if (visited[row][col])
	{
		return;
	}

	visited[row][col] = true;
	char letter = board[row][col];
	TrieNode *nextNode = getChild(currentNode, letter);

	// if there is a next node then check for the a word
	if (nextNode)
	{
		string newWord = word + letter;
		if (nextNode->isWord)
		{
			if (found.find(newWord) == found.end())
			{
				found.insert(newWord);
				if (solution.length() < newWord.length() || (solution.length() == newWord.length() && newWord < solution))
				{
					solution = newWord;
				}
				// if we didn't find anything - count the scores
				score += wordScores[newWord.length()];
				total++;
			}
		}
		for (int i = 0; i < 8; i++)
		{
			int newRow = row + xDir[i];
			int newCol = col + yDir[i];
			if (isValid(newRow, newCol))
			{
				dfs(newRow, newCol, nextNode, newWord);
			}
		}
	}

	visited[row][col] = false;
}

TrieNode *root = new TrieNode();

int main()
{
	scanf("%ld\n", &numWords);
	char word[9];

	for (int i = 0; i < numWords; i++)
	{
		scanf("%s\n", &word);
		insert(root, word);
	}

	scanf("%ld\n", &numBoards);

	// per board test case
	for (long _ = 0; _ < numBoards; _++)
	{
		score = 0;
		total = 0;
		solution = "";
		found.clear();
		board.resize(4, vector<char>(4));
		visited.resize(4, vector<bool>(4, false));
		// read the board
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%c\n", &board[i][j]);
			}
		}

		// check for every word in the current board
		// iterate through each letter in the board

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				dfs(i, j, root, "");
			}
		}

		printf("%ld %s %ld\n", score, solution.c_str(), total);
	}
	return 0;
}