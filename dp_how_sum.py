from time import perf_counter
def how_sum_memo(target_sum, nums, memo={}):
	"""
	Checks how target_sum can be genereted by adding one or different elements of nums
	@param:
		target_sum
		nums:list of positive numbers 
		memo:dict to store intermediate values and valid summable nums
	returns:
		true or false
	n = length of nums
    m = target sum
	time complexity O(m^2 * n) 
	space complexity O(m^2)
	"""
	if target_sum in memo:
		return memo[target_sum]
	if target_sum == 0:
		return []
	if target_sum < 0:
		return None

	for i in nums:
		remainder = target_sum - i
		result = how_sum_memo(remainder,nums, memo)
		if  result != None:
			memo[target_sum] = result + [i]
			return memo[target_sum]
	# stores a dictionary value of each target value - each element of nums
	memo[target_sum] = None
	return None

def how_sum_tabulation(target, nums):
	"""
	@param:
		target_sum
		nums:list of positive numbers 
	returns:
		the last index of table as true/false
	n = length of nums
	m = target sum
	time complexity O(m^2 * n)
	space complexity O(m^2)
	"""
	table = [None if i != 0 else [] for i in range(target + 1)]
	length = len(table)

	for i in range(length):
		if table[i] is not None:
			for j in nums:
				if (i  + j) < length:
					table[i + j] = table[i] + [j]

	return table[-1]



# t1 = perf_counter()
print(how_sum_memo(7, [2,3], {})) # [3,2,2]
print(how_sum_memo(7, [5,3,4,7], {})) # [4,3]
print(how_sum_memo(7, [2,4], {})) #None
print(how_sum_memo(8, [2,3,5], {})) # [2,2,2,2]
print(how_sum_memo(300, [7,14], {})) # None
# print(perf_counter() - t1)
print("="*20)
print(how_sum_tabulation(7, [2,3])) # [3,2,2]
print(how_sum_tabulation(7, [5,3,4,7])) # [4,3]
print(how_sum_tabulation(7, [2,4])) #None
print(how_sum_tabulation(8, [2,3,5])) # [2,2,2,2]
print(how_sum_tabulation(300, [7,14])) # None(300, [7,14], {})) # None













