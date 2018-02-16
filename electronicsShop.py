def getMoneySpent:(keyboards, drives, s):
	affordable = []
	keyboards.sort()
	drives.sort()
	for key in keyboards:
		for drive in drives:
			if key + drive <= s:
				affordable.append(key + drive)
			else:
				break
	affordable.sort()
	return -1 if len(affordable) == 0 else affordable[-1]

