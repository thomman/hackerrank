def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    larry = rob = 0
    
    for apple in apples:
		throw = apple + a
        if s <= throw <= t:
            larry += 1
    for orange in oranges:
    	throw = b + orange 
            if s <= throw <= t:
                rob += 1
    print(larry)
    print(rob)

countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])
