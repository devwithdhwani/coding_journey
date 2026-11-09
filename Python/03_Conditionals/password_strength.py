password = input("Enter a password: ")

long_enough = len(password) >= 8
has_digit = not password.isalpha()
has_upper = password != password.lower()

if long_enough and has_digit and has_upper:
    print("Strong")
elif long_enough and (has_digit or has_upper):
    print("Medium")
else:
    print("Weak")
