import sys
new_recursion_limit=3000
sys.setrecursionlimit(new_recursion_limit)
fibonacci_cache = {}


def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci_cache[n] = result
        return result



number = int(input("Enter the number for fiboonacci value: "))
result = fibonacci(number)
print(f"The value of fibbonaci {number} is {result}")
