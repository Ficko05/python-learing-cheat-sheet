numbers = [1,2,3,4,5,6]
numbers.append(7)
print(numbers)
numbers.insert(0, 9) # 1 param is index, second is value
print(numbers)
#numbers.pop() # removes the last item in a list
numbers.remove(9)
print(numbers)

print(numbers.index(6))  # gives the index of the first occurrence of the item

print(1 in numbers)  # gives a bool if there is an occurrence of the item
print(8 in numbers)
print(len(numbers)) #numbers of items in the list

print(numbers.count(3))  # count how meny 3 there are in the list
numbers.sort()  # sorts the list
numbers.reverse()  # reverses the list
new_numbers = numbers.copy()  # makes a copy of the list

print("Index :", numbers[1:3])#prints from index 1 to 3


del(numbers[1])
print(numbers)

#numbers.clear() # clears out the whole list

del(numbers[1:3])
print(numbers)

print("_______")
number2 = []
number2.extend(numbers)
print(number2)
number2.append("number2")

number3 = numbers + number2
print(number3)

number4 = []
number4.append(numbers)
number4.append(number2)
print(number4)#Has 2 arrays in a the varianble/array
print(number4[1][4])#spesifiees the second list amd what index


# removes duplicates
ll = [4,5,6,6,5,4]
tt = []
for item in ll:
    if item not in tt:
        tt.append(item)
print(tt)
