arr = [9,4,5,2,1,9]

arr.sort()
count = 1
tallest = arr[-1]
for i in range(len(arr)):
	if arr[-1-i] == tallest:
		count += 1
