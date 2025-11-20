phones = ["ok", "ok", "ok", "broken", "ok", "ok", "ok"]


# for idx, phone in enumerate(phones):
for i in range(len(phones)):
    if phones[i] == "broken":
        print(f"Found a broken phone at index: {i}, stopping the search.")
        break
    print("Phone is ok, continuing the search ...")
else:
    print("All phones are ok!")
