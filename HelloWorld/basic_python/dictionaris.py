customer = {  # unique dictionaries, no duplicates
    "name": "john",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
customer["name"] = "jack smith"
customer["job"] = "programmer"
print(customer.get("name"))
print(customer.get("birthdate", "Jan 1 1999")) # give value to something thats not in the "list"

print(customer)

phone = input("phone number?: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for item in phone: # goes threw al characters one at a tone
    print(item)
    output += digits_mapping.get(item, "!") # the ! is a default value that gets printed if nothing "fits"
print(output)
