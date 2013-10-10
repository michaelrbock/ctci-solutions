"""
This method only returns True/False, not the location of the key
"""
def modified_binary_search(lst, key):
	if len(lst) == 0 or lst is None:
		return False
	# test if only one element left
	if len(lst) == 1:
		return lst[0] == key
	mid = (len(lst) - 1) / 2
	curr = mid
	while lst[curr] == '':
		if curr == len(lst) - 1:
			curr = 0
		else:
			curr += 1
		if curr == mid: # only empty strings in the list
			return lst[curr] == key
	if key == lst[curr]:
		return True
	elif key < lst[curr]:
		return modified_binary_search(lst[:curr], key)
	elif key > lst[curr]:
		return modified_binary_search(lst[(curr+1):], key)
