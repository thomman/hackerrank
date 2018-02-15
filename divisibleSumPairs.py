#You are given an array of n integers, a0,a1...,an-1, and a positive integer, k.
#Find the number of (i,j) pairs s.t. i < j and ai + aj is divisible by k.

def divisibleSumPairs(n, k, arr):
	count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] + arr[j]) % k == 0:
				count += 1
	return count

#Expect 5
#print(divisibleSumPairs(6, 3, [1,3,2,6,1,2]))
