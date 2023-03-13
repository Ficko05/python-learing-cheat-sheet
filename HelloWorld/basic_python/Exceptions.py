try:
    age = int(input("age: "))  # try cath block basically.
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print("invalid value")
except Exception:
    print("invalid value 1")
