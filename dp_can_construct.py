def can_construct_memo(target, word_bank, memo={}):
	"""
	Checks if target can be generated using one or more elements from word bank
	@param:
		target: string
		word_bank: list of strings
	returns:
		true or false
	time complexity O(m^2n)
	space complexity O(m)
	"""
	if target == '':
		return True
	if target in memo:
		return memo[target]

	for word in word_bank:
		if target.startswith(word):
			if can_construct_memo(target[len(word):], word_bank):
				memo[target] = True
				return True

	memo[target] = False
	return False

def can_construct_tabulation(target, word_bank):
	"""
	Checks if target can be generated using one or more elements from word bank
	@param:
		target: string
		word_bank: list of strings
	returns:
		true/false
	time complexity O(m^2n)
	space complexity O(m)
	"""
	table = [False if i != 0 else True for i in range(len(target) + 1)]
	length = len(table)
	i = 0
	while i < length:
		if table[i] is True:
			for sub_string in word_bank:
				if target[i:].startswith(sub_string):
					table[len(sub_string) + i] = True
		i += 1
	return table[-1]

print(can_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
print("="*30)
print(can_construct_tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct_tabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct_tabulation('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct_tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))

