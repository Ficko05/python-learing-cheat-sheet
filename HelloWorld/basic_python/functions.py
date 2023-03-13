def sum_of(a, b, c):
    return a+b+c

def sum_of_equals(a,b,c = 10):
    return a+b+c

print(sum_of(1,2,3))
print(sum_of_equals(1,2))

mystery = sum_of

print(mystery(4,5,6))
print(sum_of(1,2,3))


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name} ')
    print("wlcome")
    
greet_user(first_name="mark", last_name="zuck") # keyword arguments
