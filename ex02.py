number = int(input("Input an integer: "))

if number % 2 == 0:
    if number % 4 == 0:
        print(number, " is a multiple of 4.")
    else:
        print(number, " is even.")
elif number % 2 == 1:
    print(number, " is odd.")
else:
    print("You did not enter an integer.")



