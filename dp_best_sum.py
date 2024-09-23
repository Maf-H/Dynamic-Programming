from time import perf_counter
def best_sum_memo(target_sum, nums, memo={}):
    """
    Finds the shortest list of numbers that adds up to target_sum
    @param:
        target_sum
        nums: list of positive integers
        memo: dict to store intermediate values and valid summable nums
    returns:
        list of numbers that add up to target_sum or None if no solution exists
    n = length of nums
    m = target sum
    time complexity O(m * n^2)
    space complexity O(m * n)
    (Memoization)
    """
    
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    shortest_combination = None
    for i in nums:
        result = best_sum_memo(target_sum - i, nums, memo)
        if result is not None :
            current_combination = result + [i]
            if shortest_combination == None or len(current_combination) < len(shortest_combination):
                shortest_combination = current_combination

    memo[target_sum] = shortest_combination
    return shortest_combination

def dp_best_sum_tabulation(target, nums):
    """
    Finds the shortest list of numbers that adds up to target_sum
    @param:
        target
        nums: list of positive integers
    returns:
        shortest list of numbers that add up to target_sum or None if no solution exists
    n = length of nums
    m = target sum
    time complexity O(m * n^2)
    space complexity O(m * n)
    (Tabulation)
    """
    table = [None if i != 0 else [] for i in range(target + 1)]
    length = target + 1

    for i in range(length):
        if table[i] is not None:
            for j in nums:
                if (i + j) < length and table[i + j] is None:# breaks i≥7,6,4, j=2,3,5
                    table[i + j] = table[i] + [j]
                elif (i + j) < length and (len(table[i] + [j]) < len(table[i + j])):
                    table[i + j] = table[i] + [j]
    return table[target]

print(best_sum_memo(7, [5,3,4,7], {})) # [7]
print(best_sum_memo(8, [2,3,5], {})) # [3,5]
print(best_sum_memo(8, [1,4,5], {})) # [4,4]
t1 = perf_counter()
print(best_sum_memo(100, [1,2,5,25], {})) # [25,25,25,25]
print(perf_counter() - t1)
print("="*20)
print(dp_best_sum_tabulation(7, [5, 3, 4, 7]))
print(dp_best_sum_tabulation(8, [2, 3, 5]))
print(dp_best_sum_tabulation(8, [1, 4, 5]))
t2 = perf_counter()
print(dp_best_sum_tabulation(100, [1, 2, 5, 25]))
print(perf_counter() - t2)
