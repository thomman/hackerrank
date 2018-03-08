#Beautiful-days-at-the-movies
def bDay(i,j,k):
	bday = 0
	for day in range(i, j+1):
		rday = int(str(day)[::-1]) #Reversed
		if (day-rday) % k == 0:
			bday += 1
	return bday
	
print(bDay(20,23,6))
