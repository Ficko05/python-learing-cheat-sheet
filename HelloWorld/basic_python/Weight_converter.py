weight = float(input("what is your wight ? "))
converting_type = input("(K) g or (L)bs? ")

if converting_type.lower() == 'l':
    temp_weight = weight / 2.2046
    print("weight in KG is " + str(temp_weight))
elif converting_type.lower() == 'k':
    temp_weight = weight * 2.246
    print("weight in lbs is " + str(temp_weight))
else:
    print("something went wrong")
