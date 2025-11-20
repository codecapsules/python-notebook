def is_sayan():
    sayans = ["goku", "vegeta", "broly"]
    half_sayans = ["goku", "vegeta", "broly"]
    user_name = input("Enter your name: ").lower()

    if user_name in sayans:
        print("You are a Sayan!")
    elif user_name in half_sayans:
        print("You are a half Sayan!")
    else:
        print("You are not a Sayan.")


is_sayan()
