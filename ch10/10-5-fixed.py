"""
This method returns the location of the given string
"""
# tail recursive method
def search_r(strings, key, first, last):
	# move mid to the middle
	mid = (last + first) / 2
	# if mid is empty, closest non empty string
	if strings[mid] == '':
		left = mid - 1
		right = mid + 1
		while (True):
			if left < first and right > last:
				return -1
			elif right <= last and not strings[right] == '':
				mid = right
				break
			elif left >= first and not strings[left] == '':
				mid = left
				break
			right += 1
			left += 1
	
	# check for string and recurse if necessary
	if key == strings[mid]: # found
		return mid
	elif strings[mid] < key:
		return search_r(strings, key, mid + 1, last)
	else:
		return search_r(strings, key, first, mid - 1)

# if key is the empty string or string not found, return -1
def search(strings, key):
	if strings == None or len(strings) == 0 or str == '':
		return -1
	return search_r(strings, key, 0, len(strings) - 1)