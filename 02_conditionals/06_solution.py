
distance = int(input("How much distance you have to cover?: "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:    
    transport = "Bike"
else:    
    transport = "Car"

print("AI recommends you the transport of: ", transport)
