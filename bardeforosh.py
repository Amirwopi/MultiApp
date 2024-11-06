personnel = {"amir": 9000, "hamid": 1000, "mmd": 40000}
personnel.update({"wopi": 2000})
personnel.update(dict(wopi=2000))


def add_personnel(name):
    if name not in personnel:
        try:
            price = int(input("What is the price of the personnel " + name + "? "))
            personnel[name] = price
        except ValueError:
            print("Please enter a valid number for the price.")
    else:
        print("This personnel already exists :)")


def remove_personnel(name):
    if name in personnel:
        personnel.pop(name)
        print(name + " has been removed.")
    else:
        print("This personnel does not exist.")


def edit_personnel(name):
    if name not in personnel:
        print("This personnel does not exist :( ")
        return
    try:
        price_edit = int(input("What is the new price for the personnel " + name + "? "))
        personnel.update({name: price_edit})
        print(name + " has been updated with the new price: " + str(price_edit))
    except ValueError:
        print("Please enter a valid number for the price.")


def stats_personnel(name):
    if name not in personnel:
        print("This personnel does not exist :( ")
        return
    print(name + " has " + str(personnel.get(name)) + " price.")


def list_personnel():
    print("List of all personnel:")
    for name in personnel:
        print(name)


def handler(quest):
    if quest == "list":
        list_personnel()
        return True
    name = input("Enter the name of the personnel: ")

    if quest == "add":
        add_personnel(name)
    elif quest == "remove":
        remove_personnel(name)
    elif quest == "edit":
        edit_personnel(name)
    elif quest == "stats":
        stats_personnel(name)
    else:
        print("Invalid option!")
        return False

    return True


def bardefrosh_run():
    while True:
        quest = input("Would you like to add, remove, edit, stats, list a personnel or exit? ").lower()
        if quest == "exit":
            print("Exiting the program. plz move item")
            break
        elif not handler(quest):
            print("Oops! Something went wrong.")

