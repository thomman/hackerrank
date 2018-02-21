def des(h, word):
	import string
	s = string.ascii_lowercase
	d = {letter:val for letter,val in zip(s,h)}
	
	height = 0
	for l in word:
		if height < d[l]:
			height = d[l]
	return height*len(word)
