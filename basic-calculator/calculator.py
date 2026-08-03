print("START")
print("==== Simple Calculator ====")


while True:
    choice = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Division",
        5: "Exit",
    }

    for key, value in choice.items():
        print(f"{key}.{value}")

    user = int(input(f"Choose an option: "))
    if user == 5:
        print("Goodbye")
        break

    if user not in choice:
        print("Invalid Choices")
        continue

    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    if user == 1:
        answer = first_number + second_number
        print(f"The total is {answer}")
        print("=====================================")

    elif user == 2:
        answer = first_number - second_number
        print(f"The total is {answer}")
        print("=====================================")

    elif user == 3:
        answer = first_number * second_number
        print(f"The total is {answer}")
        print("=====================================")

    elif user == 4:

        if second_number == 0:
            print("Cannot divide by zero")

        else:
            answer = first_number / second_number
            print(f"The total is {answer}")
            print("=====================================")
    else:
        print("Invalid Choice")
