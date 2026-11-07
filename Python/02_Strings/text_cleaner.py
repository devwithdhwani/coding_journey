messy = "   Hello,   World!!   "

cleaned = messy.strip().replace("!", "").replace(",", "")

print("Original:", repr(messy))
print("Cleaned:", repr(cleaned))
print("Upper:", cleaned.upper())
print("Swapcase:", cleaned.swapcase())
