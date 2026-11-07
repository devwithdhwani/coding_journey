first = input("Enter first name: ").strip()
last = input("Enter last name: ").strip()

initials = first[0].upper() + last[0].upper()

print(f"Initials: {initials}")
print(f"Full name: {first.title()} {last.title()}")
