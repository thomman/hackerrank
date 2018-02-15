n, k = (int(i) for i in input().split())
food = [int(i) for i in input().split()]
price = int(input())

def op(n , k, food, price):
	anna = sum(food[i] for i in range(n) if i != k)//2
	return 'Bon Appetit' if anna == price else (price - anna)
