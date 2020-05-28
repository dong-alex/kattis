"""
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
"""


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        # at the end of the word - set it to be true as a word so the search can find it
        current.isWord = True


visited = set()
found = set()
scoring = [0, 0, 0, 1, 1, 2, 3, 5, 11]
directions = [(0, -1), (-1, -1), (-1, 1), (1, 0),
              (-1, 0), (1, 1), (0, 1), (1, -1)]
trie = Trie()
root = trie.root
# iterate through all the possible choices - cancel if mismatches


def isValid(board, row, col, node):
    return 4 > row >= 0 and 4 > col >= 0 and (row, col) not in visited and board[row][col] in node.children


def dfs(board, row, col, trieNode, word):
    if (row, col) in visited:
        return

    letter = board[row][col]
    visited.add((row, col))

    # if there is a letter found in the trieNode currently - we can traverse through it
    if letter in trieNode.children:
        newWord = word + letter
        if trieNode.children[letter].isWord:
            # found a word in the dictionary that we can use
            if newWord not in found:
                found.add(newWord)
                if len(newWord) > len(solution[1]) or len(newWord) == len(solution[1]) and newWord < solution[1]:
                    solution[1] = newWord
                solution[2] += 1
                solution[0] += scoring[len(newWord)]

        for i in range(8):
            if isValid(board, row + directions[i][0], col + directions[i][1], trieNode.children[letter]):
                dfs(board, row + directions[i][0], col + directions[i]
                    [1], trieNode.children[letter], newWord)

    visited.remove((row, col))


numWords = int(input())
words = set()
# hanlde any duplicates words if there are
for _ in range(numWords):
    word = input()
    if word not in words:
      words.add(input())
      trie.addWord(word)

# empty line
input()

# get the boards
numBoards = int(input())
board = [['' for _ in range(4)] for __ in range(4)]

letters = set()
while numBoards != 0:
    solution = [0, "", 0]
    for i in range(4):
        row = input()

        for j in range(4):
            board[i][j] = row[j]
            letters.add(board[i][j])

    found.clear()

    for i in range(4):
        for j in range(4):
            letter = board[i][j]
            if letter in root.children:
                dfs(board, i, j, root, '')

    print(*solution)
    numBoards -= 1

    if numBoards != 0:
        input()
