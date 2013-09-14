def is_permutation(s1, s2):
	# go through string 1, count use of each char in dict
	# go through string 2 and see if it matches
	chars1 = {} # {char : int}
	for c in s1:
		if c in chars1:
			chars1[c] += 1
		else:
			chars1[c] = 1

	chars2 = {} # {char : int}
	for c in s2:
		if c in chars2:
			chars2[c] += 1
		else:
			chars2[c] = 1

	return chars1 == chars2