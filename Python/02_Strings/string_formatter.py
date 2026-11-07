name = input("Enter your name: ").strip().title()
course = input("Enter your course: ").strip().title()

print("=" * 30)
print(name.center(30))
print("=" * 30)
print("Course:".ljust(10) + course)
print("Name length:".ljust(10) + str(len(name)).rjust(5))
print("=" * 30) 
