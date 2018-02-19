#The hurdle race

def hurdle(k, height):
	diff = magic = 0
	for elm in height:
		if k < elm:
			diff = elm - k
			k += diff
			magic += diff
	return magic

#print(hurdle(7,[2,5,4,5,2]))
