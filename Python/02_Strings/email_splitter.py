email = input("Enter your email: ").strip().lower()

at = email.find("@")

print(f"Username: {email[:at]}")
print(f"Domain: {email[at + 1:]}")
print(f"Total length: {len(email)}")
