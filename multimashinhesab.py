def sosis(d, condishen, numbers2):
    match condishen:
        case "-":
            return
        case "*":
            return numbers2 * d
        case "+":
            return numbers2 + d
        case "/":
            return numbers2 / d
        case _:
            return None


def multi_mashin_run():
    while True:
        condishen = input("Please enter the condition: *, +, /, or exit: ")
        if condishen == "exit":
            print("Exiting the program.")
            break
        else:
            while True:
                try:
                    cuntesh = int(input("Please enter the count (1 - 10): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        numbers = []
        for i in range(cuntesh):
            x = input("Enter a number or type 'end' to finish: ")
            if x == "end":
                break
            if not x.isnumeric():
                print("Invalid number. Please try again.")
                continue
            numbers.append(int(x))

        # Loop for 'numbers2' to ensure a valid integer
        while True:
            try:
                numbers2 = int(input("Please enter the number to apply operation with: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Applying `sosis` to each number in `numbers` using `map`
        results = list(map(lambda d: sosis(d, condishen, numbers2), numbers))

        print("Results:", results)
