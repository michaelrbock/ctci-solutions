def compress_string(s):
	compressed = ""
	count = 1
	for i, c in enumerate(s):
		if i == 0:
			continue
		if c == s[i-1]:
			count += 1
		else:
			compressed = compressed + s[i-1] + str(count)
			count = 1
	if len(compressed) < len(s):
		return compressed
	else:
		return s
