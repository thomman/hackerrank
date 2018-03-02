#Sparse Arrays using dict and list

n = int(input())
words = dict()

for i in range(n):
	word = input()
	if word in words:
		words[word] += 1
	else:
		words[word] = 1

q = int(input())
stat = []

for i in range(q):
	word = input()
	if word in words:
		stat.append(words[word])
	else:
		stat.append(0)

for i in stat:
	print(i)

