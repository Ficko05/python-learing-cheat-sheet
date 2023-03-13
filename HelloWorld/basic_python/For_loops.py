numbers = [1, 2, 3, 4, 5]
print(numbers)

for item in numbers:  # this is a foreach
    if item == 3:
        print("cheeky 3 in the list")
        continue
    print(item)

for x in range(7):  # for else loop ??
    if x == 8:
        break
else:
    print("enter else")
# this wil only print if break is not getting hit.
# if x was == 7 it would skipp else statement and continue in the code.


for temp in range(2, 10, 3):
    print(temp, end=" ")


print("--------")

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1


for item in ["mosh","ficko","sara","kidd"]:
    print(item)


price = [10,20,30]
new_price = 0
for item in price:
    new_price += item
print(new_price)