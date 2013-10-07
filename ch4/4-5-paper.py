class Node:
	def __init__(self, data):
		self.l_child = None
		self.r_child = None
		self.data = data

def is_bst(root):
	if (root is None) or \
	   (root.l_child is None and root.r_child is None):
	   return True
	if root.r_child is None:
		return root.l_child.data < root.data and is_bst(root.l_child)
	elif root.l_child is None:
		return root.r_child.data > root.data and is_bst(root.r_child)
	else:
		return root.l_child.data < root.data and \
			   root.r_child.data > root.data and \
			   is_bst(root.l_child) and \
			   is_bst(root.r_child)
