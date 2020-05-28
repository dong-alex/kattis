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
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)


def dfs(person, totalPeople):
    if person in visited:
        return 0  # dont return any cost - the visited person will have cost accounted for
    visited.add(person)
    cost = money[person]
    for i in relationships[person]:
        if i not in visited:
            childCost = dfs(i, totalPeople)
            # if the cost is negative compared to the returned value then its invalid
            cost += childCost
    return cost


line = input().split(' ')
people, relations = int(line[0]), int(line[1])

money = []
relationships = defaultdict(list)
for _ in range(people):
    money.append(int(input()))

for _ in range(relations):
    person1, person2 = input().split(' ')
    person1 = int(person1)
    person2 = int(person2)

    # undirected so that money will flow around - we want all debts paid for. 100 being owed means -75 -25 = person 1 owes 2 and 3 money 1 -> 2 -> 3
    relationships[person1].append(person2)
    relationships[person2].append(person1)

visited = set()
unpaid = False
# use dfs - subtract the money from the parent based on the child
for i in range(people):
    if i not in visited:
        if dfs(i, people) != 0:
            unpaid = True

if unpaid:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
