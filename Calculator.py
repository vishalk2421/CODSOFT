<<<<<<< HEAD
def calculator():
    while True:
        # operation choices
        print("\nSimple Calculator")
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # Get input
        choice = input("Enter the number of the operation (1-5): ")

        if choice == '5':
            print("Exiting. SEE YOU AGAIN!")
            break

        # Input of two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform operation
        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Not Possible.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

calculator()
=======

>>>>>>> 437b0f1c9dc08e6f6b86b746f456b3c469cbd6b5
