age = 40
name = "Alice"

PI = 3.14

print(f"{name} is {age} years old.")

print(PI)

print((5 + 5) / (1 + 1))  # 5.0
print((5 + 5) // (1 + 1))  # 5

print(10 % 2)  # 0
print(10 % 3)  # 1

print('Hello, start with "Hello World".')  # 1
multiline = """Hello, 
My name is: 
- Hassen
"""

print(multiline)
print(f"You have {str(age)} years old.")  # Error
print("You have {} years old.".format(age))  # Error
