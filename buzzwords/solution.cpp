/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (trie insert) - https://www.geeksforgeeks.org/trie-insert-and-search/
  (NOTE referencing from my solution in boggle as well - for the Trie structure)
  (iterating through until empty line check false) - https://www.geeksforgeeks.org/how-to-use-getline-in-c-when-there-are-black-lines-in-input/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

struct TrieNode
{
	// track depth for the lines - freq for what to show as a counter
	vector<TrieNode *> children;
	int depth = 0;
	int freq = 0;

	TrieNode(int nextDepth = 0)
	{
		depth = nextDepth;
		freq = 0;
		children = vector<TrieNode *>(26, NULL);
	}
};


void insert(TrieNode *root, string &s, int i) {
	TrieNode *current = root;
	while (i < s.length()) {
		char letter = s[i];
		if (s[i++] != ' ') {
			int index = letter - 'A';
			// create a new child if not existing
			if (!current->children[index]) {
				current->children[index] = new TrieNode(current->depth + 1);
				// current->children[index]->depth = current->depth + 1;
			}
			current->freq++;
			current = current->children[index];
		}
	}
	// ending of word - counts a word itself if spaced
	current->freq++;
}

int main()
{

	string s;
	// continue until empty line
	while (getline(cin, s))
	{
		TrieNode *root = new TrieNode();
		// for every letter - skip spaces - insert the letters into the Trie
		for (int i = 0; i < s.length(); i++) {
			if (s[i] != ' ') {
				insert(root, s, i);
			}
		}

		queue<TrieNode*> q;
		q.push(root);
		TrieNode *current;
		int maxFreq = 0, depth = 0;

		while (q.size() != 0) {

			current = q.front();
			// new depth - print solution of the latest frequency and reset it
			if (depth != current->depth) {
				if (maxFreq > 1) {
					cout << maxFreq << endl;
					maxFreq = 1;
					depth++;
				} else {
					// hit a length with no more than 1 instance - no more continues
					cout << endl;
					break;
				}
			}
			q.pop();
			// every alphabet check
			for (int i = 0; i < 26; i++) {
				if (current->children[i]) {
					maxFreq = max(maxFreq, current->children[i]->freq);
					q.push(current->children[i]);
				}
			}
		}
	}
	return 0;
}