text = input("Enter a sentence: ").lower()

vowels = (
    text.count("a")
    + text.count("e")
    + text.count("i")
    + text.count("o")
    + text.count("u")
)

print(f"Vowels: {vowels}")
