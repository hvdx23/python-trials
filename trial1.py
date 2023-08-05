def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Get a value from the user
number = int(input("What number's factorial do you want to find out? "))

# Call the factorial function and print the result
result = factorial(number)
print(f"The factorial of {number} is {result}")
