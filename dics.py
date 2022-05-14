"""
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
print(customer["name"])
"""

phone = input("Phone: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three"
}
output = " "
for ch in phone:
   output +=  digits.get(ch, "!!")
print(output)
