sec1 = int(input("Enter seconds: "))

hours = sec1 // 3600
remaining = sec1 % 3600
minutes = remaining // 60
seconds = remaining % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
