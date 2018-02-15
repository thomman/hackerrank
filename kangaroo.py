def kang(x1,v1,x2,v2):
	if v1 < v2:
		if x1 < x2:
			return 'NO'
		while x2 < x1:
			x1 += v1
			x2 += v2
	elif v1 == v2:
		if x1 != x2:
			return 'NO'
	else:
		if x2 < x1:
			return 'NO'
		while x1 < x2:
			x1 += v1
			x2 += v2

	return 'YES' if x1 == x2 else 'NO'

print(kang(0,3,4,2))
