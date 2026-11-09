num = int(input("Enter a number: "))

result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

sign = "Non-negative" if num >= 0 else "Negative"
print(sign)
