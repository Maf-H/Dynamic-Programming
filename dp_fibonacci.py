from time import perf_counter
"""
To solve Fibonacci series there are two dynamic programming approach
1. bottom-up (Tabulation)
2. Top-down(Memorization)
"""
fib_series = []
def fib_bottom_up(num):
	fib_series.insert(0, 0)
	fib_series.insert(1, 1)
	for i in range(2, num + 1):
		fib_series.insert(i, (fib_series[i - 1] + fib_series[i - 2]))
	return fib_series[num]

def fib_bottom_up_improved(num):
    """
    During tabulation we only need fib(n-1) and fib(n-2)
    therefore, we don't need to track every previous value
    instead we only need the two previous value
    """
    prev,curr = 0, 1
    for i in range(2, num + 1):
        prev, curr = curr, curr + prev
    return curr


memo = {0:0, 1:1}
def fib_top_down(num):
	if num in memo:
		return memo[num]
	memo[num] = fib_top_down(num - 1) + fib_top_down(num - 2)
	return memo[num]
	
t1 = perf_counter()
print(f"Bottom-Up : {fib_bottom_up(1000): >20}")
print(perf_counter() - t1)
t2 = perf_counter()
print(f"Bottom-Up Improved: {fib_bottom_up_improved(1000): >20}")
print(perf_counter() - t2)
t3 = perf_counter()
print(f"Top Down : {fib_top_down(500): >20}")
print(perf_counter() - t3)
