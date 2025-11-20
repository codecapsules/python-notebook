age = int(input("Enter your age: "))

if age <= 18:
    print("At {age} years old, you are too young to enter.".format(age=age))
else:
    print("At {0} years old, you can enter.".format(age))
