# node implementation

"""
1. newly created nodes are 'full' - it holds an item. only then they can turn 'hollow' - no item. Always lives until destroyed
2. exogenous (holds items) rather than endogenous (be items)

if 'u' is a node, u.item = something if full, null otherwise, therefore initialization needs to pass an item
if 'item' is the node's item then item.node = the node holding itself.
"""

class Item():
	def __init__(self, parent, itemKey):
		self.node = parent # the node holding this item - this could be set to something else
		self.key = itemKey

# initial node created is full - it contains an item and the key of the item
# a node u of rank r has exactly r children
class HeapNode():

	def __init__(self, item, itemKey):
		self.item = Item(self, itemKey)

	# when it turns hollow the itemKey is whatever it once held - just hold it the same - while the item is moved away

# (v,w) - v is the parent of w  and w is a child of v
# path of 0 or more arcs - v is an ancestor of w and w is a descendant of v
# no children = leaf
# no parent = root

"""
Set of trees representing a heap is either empty or contains a 'full root' with the minimum key (full or hollow) - this is the minimum node of the heap
"""
# heap ordered - similar to min-heap - root has a minimum key
# for every arc (v,w) ; v.key <= w.key (whether or not v and w are hollow - its previous keys were retained even if the item left)
class TreeArcNode():
	def __init__(self, heapNode):
		self.node = heapNode
		self.parents = {} # multiple parents
		self.childs = {} # multiple children
		self.rank = 0

# ----- Links during DELETE-MIN or DELETE operations only --------
# input: two full ROOTS - u, v
# output: created a link between u and v (arbitrarily decide on which is parent if equal key) - loser link gets a parent
# compares their keys and makes the root of larger key a 'child' of the other - breaking ties arbitrarily 
# eliminates one full root and preserves heap order
def link(u, v):
	# check if they are full both full otherwise its not valid
	assert u.item and v.item, "Error: nodes are not full. One or both are hollow"

	# u becomes the parent to v and v is the child to u
	# u is the winner link - v is the loser link
	if u.key <= v.key:
		u.child[v] = v
		v.parents[u] = u
	# v becomes the parent to u and u is the child to v
	# v is the winner link - u is the loser link
	else:
		v.child[u] = v
		u.parents[u] = u
	return

# creates a collection of disjoint tree - collection of graphs that are not connected
def makeHeap():
	return None

# returns the ITEM in the minimum node - not the node
def findMin(h):
	if 
	pass