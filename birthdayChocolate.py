#The birthday bar problem

def solve(n,s,d,m):
	count = 0
	for i in range(n - m + 1): #0 < m and we must stop m units before end
		p = sum(s[i+j] for j in range(m)) #sum sequences of m consecutive numbers
		count += 1 if d == p else 0
	return count

print(solve(6,[1,1,1,1,1,1],3,2))
