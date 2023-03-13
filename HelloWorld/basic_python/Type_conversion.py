bith_year = int(input('birth year? '))  # input will always get treated as a string, thats why we put int in front of input
print(type(bith_year))
age = 2022 - int(bith_year)
print(type(age))
print(age)