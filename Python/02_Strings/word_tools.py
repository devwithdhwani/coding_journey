sentence = input("Enter a sentence: ").strip()

words = sentence.split()

print("Words:", words)
print("Word count:", len(words))
print("Joined with dashes:", "-".join(words))
print("Title case:", sentence.title())
