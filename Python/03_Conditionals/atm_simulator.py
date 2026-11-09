correct_pin = "4321"
balance = 5000

pin = input("Enter your PIN: ")

if pin == correct_pin:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    elif amount % 100 != 0:
        print("Amount must be in multiples of 100")
    else:
        balance = balance - amount
        print(f"Collect your cash. Remaining balance: {balance}")
else:
    print("Incorrect PIN")
