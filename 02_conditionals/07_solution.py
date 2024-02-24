order_size = input("What size of coffee do you want?: ")
extra_shot = input("Do you want any extra shot?:")

if extra_shot == "yes":
    coffee = order_size + " coffee with extra shot"
else:
    coffee = order_size + " coffee"    

print("Order: ", coffee)
