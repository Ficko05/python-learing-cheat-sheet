temperature = 25

if temperature > 30 and temperature > 30:
    print("its a hot day")
    print("drink water")
elif temperature > 20 or temperature > 20: #
    print("its a nice day")
else: 
    print("its cold")

print("done")

good_credit = True
price = 1000000

if good_credit:
    print("wow thats awsome")
    down_payment = 0.1 * price
else:
    print("sry fam u gotta pay more, like 20 %")
    down_payment = 0.2 * price
print(f"down paymeny; ${down_payment}")


name = "hello"

if len(name) < 3:
    print("name must be longer")
elif len(name) >= 50:
    print("name must be longer")
else:
    print("name looks good")