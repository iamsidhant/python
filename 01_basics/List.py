tea_varieties = ["Black", "Green", "Oolong", "Milk"]
# print(tea_varieties)
# print(tea_varieties[0])
# print(tea_varieties[-1])
# print(tea_varieties[:2])
# print(tea_varieties[1:3])

# tea_varieties[3] = "Herbal"
# print(tea_varieties[0:4])

# tea_varieties[1:2] = "Lemon"    // get separated alphabet of element Lemon
# tea_varieties[1:2] = ["Lemon"]
# print(tea_varieties)
# print(tea_varieties[1:3])

# tea_varieties[1:3] = ["Green", "Masala"]
# print(tea_varieties[1:3])

# print(tea_varieties)
# print(tea_varieties[1:1])     # returns nothing

# tea_varieties[1:1] = ["test", "test"]
# print(tea_varieties)
# print(tea_varieties[1:3])

# tea_varieties[1:3] = []
# print(tea_varieties)

# for tea in tea_varieties:
#     print(tea)

# for tea in tea_varieties:
#     print(tea, end="-")

# if "Oolong" in tea_varieties:
#     print("We have Oolong tea")

# print(tea_varieties)
# tea_varieties.append("Lemon")
# print(tea_varieties)

# tea_varieties.pop()
# print(tea_varieties)

# tea_varieties.remove("Green")
# print(tea_varieties)

# tea_varieties.insert(1, "green")
# print(tea_varieties)

tea_varieties_copy = tea_varieties.copy()
# print(tea_varieties_copy)

# tea_varieties_copy.append("Lemon")
# print(tea_varieties_copy)
# print(tea_varieties)

# print(range(10))
squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [y**3 for y in range(7)]
print(cube_nums)
