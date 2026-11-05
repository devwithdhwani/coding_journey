first = input("Enter first name: ")
last = input("Enter last name: ")

username1 = f"{first.lower()}_{last.lower()}"
username2 = f"{first[0:3].lower()}_{last.lower()}"

print(f"Username 1: {username1}")
print(f"Username 2: {username2}")
