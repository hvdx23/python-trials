import random

random_numbers = []
for _ in range(0, 1000):
    random_numbers.append(random.randint(0, 1000))
print(random_numbers)

occurances = {num: 0 for num in range(0, 1001)}

for num in random_numbers:
    occurances[num] += 1

print(occurances)

max_occurrence = max(occurances.values())
largest_numbers = [num for num, occurrence in occurances.items() if occurrence == max_occurrence]

largest_random_number = max(random_numbers)

print(f"The largest number of occurrence is {largest_numbers[0]} and it occurs {max_occurrence} times")
print(f"The largest number from the random list is {largest_random_number}")
