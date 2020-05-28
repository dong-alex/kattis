"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

from collections import defaultdict, deque


class TrieNode:

    def __init__(self):
        self.children = {}
        self.depth = 0
        self.freq = 0


def insert(root, sentence, i):
    current = root
    while i < len(sentence):
        letter = sentence[i]
        if letter == ' ':
            i += 1
            continue

        # not found yet - create the new node - increase frequency of the parent node
        # number of occurences resembles number of times the node had been visited including itself
        if letter not in current.children:
            current.children[letter] = TrieNode()
            current.children[letter].depth = current.depth + 1
        current.freq += 1

        # we found another node - go downwards and see how far we can go
        current = current.children[letter]
        i += 1
    # include the last node - we won't traverse it but it has a node i.e. itself
    current.freq += 1


# children - letter - counter - depth
try:
    while True:
        root = TrieNode()
        line = input()
        depths = [0 for _ in range(len(line))]
        # create the trie tree based on counter
        # every letter we have - insert it into the beginning and begin as its own
        # for every index i - generate words where a[i:] is being appended
        for i in range(len(line)):
            if line[i] == ' ':
                continue
            insert(root, line, i)
        # for each depth - find until no more - BFS
        queue = deque([root])
        while queue:
            found = False
            maxFreq = 1
            current = queue.pop()
            currentDepth = current.depth
            for child in current.children:
                depths[currentDepth] = max(depths[currentDepth], current.children[child].freq)
                queue.appendleft(current.children[child])

        for i in range(len(depths)):
            if depths[i] > 1:
                print(depths[i])
            else:
                print()
                break
except:
    pass
