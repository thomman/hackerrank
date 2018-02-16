def mag(s):
#	All possible magic squares
	magic = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[8,3,4,1,5,9,6,7,2],
		[6,7,2,1,5,9,8,3,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],
		[4,3,8,9,5,1,2,7,6],[2,7,6,9,5,1,4,3,8]]
	diff = [0]*8 #Store differences

	for i in range(len(magic)):
		for j in range(len(s)):
			diff[i] += abs(magic[i][j] - s[j])
	return min(diff)

#Expect 4
#s = [4,8,2,4,5,7,6,1,6]
#print(mag(s))

s = []

for i in range(3):
	s += [int(s_temp) for s_temp in input().strip().split(' ')]
