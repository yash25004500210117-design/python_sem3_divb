age = int(input("Enter your age: "))

if age < 5:
    print("Ticket Price: Free")
elif age <= 12:
    print("Ticket Price: ₹100")
elif age <= 59:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹150")
