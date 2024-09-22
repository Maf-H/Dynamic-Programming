from pprint import pprint
def grid_traveler_memo(m, n, memo={}):
	"""
	A traveler in a grid strart from (top-left -> bottom-right). 
	It can move either right or down
	@param:
		m: number of row
		n: number of column
		memo: dictionary to store intermediate value
	returns:
		number of ways the grid traveler can travel
	time complexity O(m * n)
	space complexity O(m + n)
	Dynamic Programming (Memoization)
	"""

	key = m,n
	if key in memo:
		return memo[key]
	if m == 1 and n == 1:
		return 1
	if m == 0 or n == 0:
		return 0
	memo[key] = grid_traveler_memo(m - 1, n) + grid_traveler_memo(m, n - 1)
	return memo[key]

print(grid_traveler_memo(4, 3))

def grid_traveler_tabulation(m, n):
	"""
	A traveler in a grid strart from (top-left -> bottom-right). 
	It can move either right or down
	@param:
		m: number of row
		n: number of column
		table: 2-D list to store intermediate value
	returns:
		number of ways the grid traveler can travel
	time complexity O(m * n)
	space complexity O(m * n)
	Dynamic Programming (Tabulation)
	"""
	table=[[0] * (n + 1) for i in range(m + 1)]
	table[1][1] = 1
	# pprint(table)

	for i in range(1, m+1):
		for j in range(1, n+1):
			table[i][j] += (table[i][j-1] + table[i-1][j])
			# print(table)

	return table[m][n]

print(grid_traveler_tabulation(1, 1))
print(grid_traveler_tabulation(2, 3))
print(grid_traveler_tabulation(3, 2))
print(grid_traveler_tabulation(3, 3))
print(grid_traveler_tabulation(18, 18))