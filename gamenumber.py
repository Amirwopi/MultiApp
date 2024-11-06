import random


def gamenumber_run():
    while True:
        a = random.randint(1, 100)
        good = 0
        bad = 0
        while True:
            z = input("Enter a number between 1 and 100 or exit: ")
            if z == "end":
                break
            else:
                z = int(z)
                if a > z:
                    print("Number too high")
                    bad += 1
                elif a < z:
                    print("Number too low")
                    bad += 1
                elif a == z:
                    print("Good Number")
                    good += 1
                    print(f"Total good guesses: {good}, Total bad guesses: {bad}")

                else:
                    print("Error number plz enter nunber intejer")

    print(a)
