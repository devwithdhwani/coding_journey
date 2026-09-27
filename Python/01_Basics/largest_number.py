numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
print(largest)
