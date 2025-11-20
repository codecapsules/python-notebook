# help(sorted)
# help(list.append)

lost_numbers = [23, 15, 8, 4, 16, 42]
ln_asc = sorted(lost_numbers, reverse=False)

print(lost_numbers)  # [23, 15, 8, 4, 16, 42]
print(ln_asc)  # [4, 8, 15, 16, 23, 42]

ln_desc = sorted(lost_numbers, reverse=True)
print(ln_desc)  # [42, 23, 16, 15, 8, 4]
