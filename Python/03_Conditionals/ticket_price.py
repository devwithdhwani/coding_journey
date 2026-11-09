age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age < 5:
    print("Ticket: Free")
else:
    if age < 18 or is_student:
        print("Ticket: Rs. 50")
    else:
        print("Ticket: Rs. 100")
