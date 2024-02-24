
species = input("What is the species of animal?: ")
age = int(input("Type the age: "))

if species == "dog" and age < 2:
    food = "Puppy food"
elif species == "cat" and age > 5:
    food = "Senior cat food"
else:
    food = "chappati"        

print("You can give", food, "to", species)