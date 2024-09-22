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


memo = {0:0, 1:1}
def fib_top_down(num):
	if num in memo:
		return memo[num]
	memo[num] = fib_top_down(num - 1) + fib_top_down(num - 2)
	return memo[num]

print(f"Bottom-Up : {fib_bottom_up(6)}")
print(f"Top Down : {fib_top_down(6)}")