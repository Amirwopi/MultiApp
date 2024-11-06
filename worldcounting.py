import time


def counting(y, a, b):
    y = 0
    for i in range(b):
        x = a[i]
        y += 1
        print(f"{x} {y}")

        time.sleep(0.5)


def counting_run():
    while True:
        a = input("give me world or exit : ")
        if a == "exit":
            break
        else:
            b = len(a)
            print(f"world is {a} and number world is {b}")
