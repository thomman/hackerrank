#Prints the number of integers between two sets

def getTotal(a,b):
	count = 0
	for x in range(max(a), min(b) + 1): # max(a) <= x <= min(b)
		flag = True
		for elm in a:
			if not x % elm == 0:
				flag = False
				break
		for elm in b:
			if not elm % x == 0:
				flag = False
				break
		if flag:
			count += 1
	return count

#Expect 3
#A = {2,4}
#B = {16,32,96}

#print(getTotal(A,B))


