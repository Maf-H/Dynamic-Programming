from pprint import pprint
def dp_all_construct_memo(target, word_bank, memo={}):
	"""
	all possible word combinations from word_bank to construct target
	@param:
		target: target string
		word_bank:diffent list of sub-string
		memo: to store intermediate values
	returns:
		Two dimenssional list of sub-strings that can construct a target
	time complexity O(n^m)
	space complexity O(m)
	(Memoization)
	"""
	if target == '':
		return [[]]
	if target in memo:
		return memo[target]

	final_result = []
	for word in word_bank:
		if target.startswith(word):
			sub_string = dp_all_construct_memo(target[len(word):], word_bank)

			list_of_substring = list(map(lambda inner_list: [word] + inner_list, sub_string))
			final_result.extend(list_of_substring)
			# print(f"{target:<8} {final_result}")

	memo[target] = final_result
	return final_result

def dp_all_construct_tabulation(target, word_bank):
	"""
	time complexity O(n^m)
	space complexity O(n^m)
	(Tabulation)
	"""
	length = len(target) + 1
	table = [[] if i != 0 else [[]] for i in range(length)]

	for i in range(length):
		for word in word_bank:
			if target[i:].startswith(word):
				sub_collection = [i + [word] for i in table[i]]
				table[i + len(word)].extend(sub_collection)
	return table[length - 1]

# pprint(dp_all_construct_memo('abc', ['a','b', 'c']))
pprint(dp_all_construct_memo('purple', ['purp', 'p', 'ur', 'le', 'purpl']))# [[ 'purp', 'le' ], ['p', 'ur', 'p', 'le' ]
pprint(dp_all_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))# [[ 'ab', 'cd', 'ef'],['ab','c', 'def'],['abc', 'def' ],[ 'abcd', 'ef' ]]
pprint(dp_all_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
pprint(dp_all_construct_memo("aaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
print("="*30)
print(dp_all_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(dp_all_construct_tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))# [[ 'purp', 'le' ], ['p', 'ur', 'p', 'le' ]
print(dp_all_construct_tabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(dp_all_construct_tabulation("aaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

