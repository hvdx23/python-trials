6786897678676
def sum_digit(n):
    if n < 10:
        return n
    last_digit = n % 10
    remain = n // 10
    result = last_digit+sum_digit(remain)
    return result

number = int(input("Enter a positive integer: "))

result = sum_digit(number)
print(f"The sum of digits of {number} is {result}")