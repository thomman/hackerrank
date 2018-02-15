def rec(score):
	low = high = score[0]
	countLow = countHigh = 0
	for i in range(len(score)):
		if high < score[i]:
			high = score[i]
			countHigh += 1
		if score[i] < low:
			low = score[i]
			countLow += 1
	return countHigh, countLow
