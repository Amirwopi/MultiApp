def calculator(z, x, y):
    match z:
        case "+":
            return x + y
        case "-":
            return x - y
        case "/":
            return x / y
        case "*":
            return x * y
        case "%":
            return x % y
        case _:
            return "Invalid input"


def run_calculator():
    while True:
        z = input("Enter operation (+, -, *, /, % or exit): ")
        if z == "exit":
            print("Returning to main menu...")
            break
        else:
            try:
                x = int(input("Enter first number: "))
                y = int(input("Enter second number: "))
                result = calculator(z, x, y)
                print("Result:", result)
            except ValueError:
                print("Please enter valid numbers.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")
