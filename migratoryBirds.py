def migratoryBirds(n, ar):
	freq = dict()
	for elm in ar:
		if not elm in freq:
			freq[elm] = 1
		else:
			freq[elm] += 1
	smallestID = idNumb = 0
	for val,key in sorted(zip(freq.values(), freq.keys())):
		if idNumb < val:
			idNumb = val
			smallestID = key
	return smallestID

#Expect 4
#print(migratoryBirds(6,[1,4,4,5,3]))

