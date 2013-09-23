def is_balanced(root):
	if root == None or (root.l_child == None and root.r_child == None):
		return True
	if root.l_child == None:
		l_height = 0
	else:
		l_height = count_height(root.l_child, 0)
	if root.r_child == None:
		r_height = 0
	else:
		r_height = count_height(root.r_child, 0)
	return is_balanced(root.l_child) and is_within_one(l_height, r_height) and is_balanced(root.r_child)

def count_height(root, height):
	if root.l_child == None and root.r_child == None:
		return height
	elif root.l_child == None:
		return count_height(root.r_child, height + 1)
	elif root.r_child == None:
		return count_height(root.l_child, height + 1)
	l_height = count_height(root.l_child, height + 1)
	r_height = count_height(root.r_child, height + 1)
	return max(l_height, r_height)

def is_within_one(num1, num2):
	return (num1 - num2 == 0) or (num1 - num2 == 1) or (num1 - num2 == -1)
