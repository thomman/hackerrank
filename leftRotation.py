#Left rotation; shifts an array of size n by 1 unit to the left.

def shift(x, d):
	if d == len(x):
		return x
	return [i for i in x[d:]] + x[:d]
