#Given a square matrix of size n x n, calculate the absolute difference between the sums of its diagonals.
#Input array is given as strings

def diagDiff(A):
	diag1 = diag2 = 0
	for i in range(len(A)):
		diag1 += A[i][i]
		diag2 += A[i][-1-i]
	return abs(diag1 - diag2) #Abs diff

N = int(input()) #n

def toList(s):
	s = s.split()
	for i in range(len(s)):
		s[i] = int(s[i])
	return s

A = []

for i in range(N):
	s = input()
	A.append(toList(s))


print(diagDiff(A))
