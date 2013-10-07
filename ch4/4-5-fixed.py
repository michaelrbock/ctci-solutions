import sys

class Node:
	def __init__(self, data):
		self.l_child = None
		self.r_child = None
		self.data = data

def is_bst(root):
	return is_bst_recursive(root, -sys.maxint - 1, sys.maxint)

def is_bst_recursive(root, min, max):
	if root is None:
		return True
	if root.data <= min or root.data > max:
		return False

	if not is_bst_recursive(root.l_child, min, root.data) or \
	   not is_bst_recursive(root.r_child, root.data, max):
	   return False

	return True
