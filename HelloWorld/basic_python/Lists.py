names = ["john", "Bob", "mosh", "sam", "peter"]
print(names)
print(names[0])
print(names[-1])
names[0] = "jon"
print(names)
print(names[0:3])
print(names[2:5])

names.append("hello")#append is adding to the list
print(names)

nu = [5,6,4,2,-9,-3,7]
highest_number = 0
for item in nu:
    if item > highest_number:
        highest_number = item
print(highest_number)
