def solve(n,p):
	if n % 2 == 0 and n-p == 1 and 2 < n: #Last page and even 
		return 1
	elif n % 2 == 0 and n-p == 1: #First page and even
		return 0
	else:
		return (n-p)//2 if n-p < p else p//2
