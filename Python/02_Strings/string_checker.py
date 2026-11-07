text = input("Enter something: ").strip()

print("All digits:", text.isdigit())
print("All letters:", text.isalpha())
print("All uppercase:", text.isupper())
print("Contains a space:", " " in text) 
