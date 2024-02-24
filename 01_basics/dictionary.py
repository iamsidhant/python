
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
# print(chai_types)
# print(chai_types["Masala"])

# print(chai_types.get("Ginger"))

chai_types["Green"] = "Fresh"
# print(chai_types)

# for chai in chai_types:
#     print(chai)               # give only keys

# for chai in chai_types:
#     print(chai, chai_types[chai])

# for key, value in chai_types.items():
#     print(key, value)

# if "Masala" in chai_types:
#     print("I have masala chai")

# print(len(chai_types))  

chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

chai_types.pop("Masala")
# print(chai_types)

chai_types.popitem()
# print(chai_types)

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "tea": {"Green": "Freah", "Black": "Strong"}
}
# print(tea_shop)
# print(tea_shop["chai"])
# print(tea_shop["chai"]["Ginger"])

squared_nums = {x:x**2 for x in range(11)}
# print(squared_nums)
squared_nums.clear()
# print(squared_nums)

keys = ["Masala", "Ginger", "Lemon"]
# print(keys)

default_value = "delicious"
new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)

new_dict2 = dict.fromkeys(keys, keys)
# print(new_dict2)
