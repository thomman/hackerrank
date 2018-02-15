maxSum = 0

elm = [1,2,3,4,5]
minSum = sum(elm)

for i in range(len(elm)):
	for j in range(len(elm)):
		if j != i:
			s += elm[j]
	if maxSum < s:
		maxSum = s
	if s < minSum:
		minSum = s

