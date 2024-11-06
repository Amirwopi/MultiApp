import random

def gamenumber_run():
    while True:
        a = random.randint(1, 100)
        good = 0
        bad = 0
        print("I have chosen a number between 1 and 100. Try to guess it!")
        while True:
            z = input("Enter a number between 1 and 100 or 'exit' to quit: ")
            if z == "exit":
                print("Exiting the game.")
                return  # Break out of the function and stop the game
            try:
                z = int(z)  # Convert input to an integer
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue  # Skip this loop iteration if input is invalid

            if z > a:
                print("Number too high")
                bad += 1
            elif z < a:
                print("Number too low")
                bad += 1
            else:  # z == a
                print("Good Number!")
                good += 1
                print(f"Total good guesses: {good}, Total bad guesses: {bad}")
                break  # Exit the inner loop once the correct number is guessed

