#Takes two tuples as input and compare each entry, then returns a score.
def comp(a,b):
	sa = sb = 0
	for a,b in zip(A,B):
		if a < b:
			sb += 1
		elif b < a:
			sa += 1
	return sa, sb

A = eval(",".join(input("sequence 1: ").split()))
B = eval(",".join(input("sequence 2: ").split()))
a, b = comp(A,B)
print(a,b)
