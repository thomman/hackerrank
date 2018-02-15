#Counts number of sock pairs you can sell:)
def sock(n, ar):
	socks = dict()
	for i in range(n):
		s = ar[i]
		if s in socks:
			socks[s] += 1
		else:
			socks[s] = 1
	pairs = 0
	for i in socks.values():
		while 1 < i:
			i -= 2
			pairs += 1
	return pairs
