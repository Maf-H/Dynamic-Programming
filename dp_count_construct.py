def dp_count_construct_memo(target, word_bank, memo={}):

	"""
	count, in how many ways can target constructed from word_bank
	we can reuse elements of word_bank as much as we need
	@param:
		target:target string
		word_bank:list of strings
	returns:
		ways to construct target from word_bank
	n = length of nums
    m = target sum
	time complexity O(m^2*n)
	space complexity O(m)
	(Memoization)
	"""

	if target == '':
		return 1
	if target in memo:
		return memo[target]
	count = 0
	for word in word_bank:
		if target.startswith(word):
			count += dp_count_construct_memo(target[len(word):], word_bank)
	memo[target] = count
	return count
def dp_count_construct_tabulation(target, word_bank):
	"""
	@param:
		target:target string
		word_bank:list of strings
	returns:
		ways to construct target from word_bank
	n = length of nums
	m = target sum
	time complexity O(m^2*n)
	space complexity O(m)
	(Tabulation)
	"""

	length = len(target) + 1
	table = [0 if i != 0 else 1 for i in range(length)]

	for i in range(length):
		for word in word_bank:
			if target[i:].startswith(word):
				table[i + len(word)] += table[i] 

	return table[length - 1]




print(dp_count_construct_memo('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(dp_count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(dp_count_construct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(dp_count_construct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(dp_count_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
print("="* 30)
print(dp_count_construct_tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(dp_count_construct_tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(dp_count_construct_tabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(dp_count_construct_tabulation('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(dp_count_construct_tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
