#Convert from 12-hour clock to military (not my solution)
import re

def timeConversion(s):
	hour = int(s[:2])
	meridian = s[8:]

	if hour == 12:
		hour = 0
	if meridian == 'PM':
		hour += 12
	return '%02d' % hour + s[2:8]
