def power(base_number, exponent_value):
    if exponent_value == 0:
        return 1
    else:
        result = base_number * power(base_number, exponent_value - 1)
        return result


base_number = int(input("Enter the base value: "))
exponent = int(input("Enter the exponent value: "))
result = power(base_number, exponent)
print(f"{base_number} to the power of {exponent} is {result}")
