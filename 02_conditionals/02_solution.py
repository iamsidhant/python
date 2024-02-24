age = int(input("Type your age: "))
day = input("On which day?: ")

price = 12 if age >= 18 else 8

if day == "wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)
