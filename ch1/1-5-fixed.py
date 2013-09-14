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
	# for last character or only if 1 char string
	if len(s) >= 1:
		compressed = compressed + s[len(s)-1] + str(count)

	if len(compressed) < len(s):
		return compressed
	else:
		return s
