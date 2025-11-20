def guess_number(lottery_number):
    actual_number = 0

    while actual_number != lottery_number:
        actual_number = int(input("Guess the number: "))

        if actual_number > 0 and actual_number < 20:
            # result = "Too low!" if actual_number < lottery_number else "Too high!"
            if actual_number < lottery_number:
                print("Too low!")
            elif actual_number > lottery_number:
                print("Too high!")
            else:
                print("Correct!")
        else:
            print("The number must be between 1 and 20.")

    print("You guessed it!")


guess_number(7)
