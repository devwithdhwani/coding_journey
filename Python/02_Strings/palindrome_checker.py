word = input("Enter a word: ").lower().strip()

print(f"Word: {word}")
print(f"Reversed: {word[::-1]}")
print(f"Palindrome: {word == word[::-1]}")
