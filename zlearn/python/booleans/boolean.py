age = 18

result = age >= 18

print(result)  # True
bool(age)  # True
bool("Hello")  # True
bool("")  # False

bool("")  # False
bool([])  # False
bool([1, 2, 3])  # True

bool(0)  # False
bool(1)  # True

print(0 or "Go")  # Go
print(0 and "Go")  # 0
