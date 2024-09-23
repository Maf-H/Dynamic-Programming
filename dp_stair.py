def stair_tabulation(steps):
	"""
	Climbing stairs problem
	you can move 1 or 2 step at a time 
	in how many ways can you climb nth stair?
	The following solution is using: 
		dynamic programming (tabulation)
	@param:
		steps:int
	returns:
		number of ways to climb the stair.
	time complexity O(n)
	space complexity O(1)
	"""
	prev = 1
	current = 2

	for i in range(2, steps):
		prev, current = current, (prev + current)

	return current

print(stair_tabulation(10))