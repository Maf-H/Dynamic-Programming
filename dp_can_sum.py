from time import perf_counter
"""
Checks if target can be generated from nums:
We used two Functions dynamic programming 
    1. (memoization)
    2. (Tabulation)
"""
def can_sum_memo(target_sum, nums, memo={}):
	"""
	Checks if target_sum can be genereted by adding one or different elements of nums
	assumptions:
		nums are positive integers
		initially target is not equal zero
	@param:
		target_sum
		nums:list of positive numbers 
		memo:dict to store intermediate values
	returns:
		true or false
	n = length of nums
    m = target sum
	time complexity O(m * n)
	space complexity O(m)

	"""
	
	if target_sum == 0:
		return True
	if target_sum < 0:
		return False
	if target_sum in memo:
		return memo[target_sum]

	for i in nums:
		# target_sum -= i
		if can_sum_memo(target_sum - i, nums, memo) == True:
			memo[target_sum] = True
			return True
	# stores a dictionary value of each target value - each element of nums
	memo[target_sum] = False
	return False

def can_sum_tabulation(target, nums):
	"""
	@param:
		target_sum
		nums:list of positive numbers 
	returns:
		the last index of table as true/false
	n = length of nums
	m = target sum
	time complexity O(m * n)
	space complexity O(m)
	"""

	table = [False if i != 0 else True for i in range(target + 1)]
	length = (target + 1)

	for i in range(length):
		if table[i]:
		    for j in nums:
		        if (i + j) < length:
		            table[i + j] = True

	return table[-1]

t1 = perf_counter()
print(can_sum_memo(7, [2,3], {}))
print(can_sum_memo(7, [5,3,4,7], {}))
print(can_sum_memo(7, [2,4], {}))
print(can_sum_memo(8, [2,3,5], {}))
print(can_sum_memo(300, [7,14], {}))
print("="*20)
print(f"{"Memoization":.<15} {perf_counter() - t1}")
t2 = perf_counter()
print(can_sum_tabulation(7, [2,3]))
print(can_sum_tabulation(7, [5,3,4,7]))
print(can_sum_tabulation(7, [2,4]))
print(can_sum_tabulation(8, [2,3,5]))
print(can_sum_tabulation(300, [7,14]))
print(f"{"Tabulation":.<15} {perf_counter() - t1}")
