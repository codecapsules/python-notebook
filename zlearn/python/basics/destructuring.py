from datetime import datetime

euro, dollar = 1.00, 1.17
currencies = [("Euro", 1.00), ("Dollar", 1.17), ("Yen", 129.53)]

print(f"Euro: {euro}, Dollar: {dollar}")

for currency, rate in currencies:
    print(f"1 Euro is {rate} {currency}")

# for curr in currencies:
#     currency, rate = curr
#     print(f"1 Euro is {rate} {currency}")

date = datetime.now()

print(date)
