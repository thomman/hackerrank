def pm(arr):
	minus = zero = plus = 0
	for i in arr:
		if 0 < i:
			plus += 1
		elif i < 0:
			minus += 1
		else:
			zero += 1
	N = len(arr)
	minus = minus/N
	zero = zero/N
	plus = plus/N
	return minus, plus, zero

print(pm([-4,3,-9,0,4,1]))


