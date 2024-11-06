personnel = {"amir": 9000, "hamid": 1000, "mmd": 40000}
personnel.update({"wopi": 2000})
personnel.update(dict(wopi=2000))


def add_personnel(name):
    if name not in personnel:
        price = input("What is the price of the personnel nega " + name + "? ")
        personnel[name] = int(price)
    else:
        print("in barde hanodz dare mide  :)")


def remove_personnel(name):
    if name in personnel:
        personnel.pop(name)
        print(name + " barde azad shod")
    else:
        print("hamchin barde ii vojod nadarad")


def edit_personnel(name):
    if name not in personnel:
        print("in barde vojod nadarad :( ")
        return
    price_edit = input("What is the price of the personnel nega " + name + "? ")
    personnel.update({name: int(price_edit)})
    print(name + " -> " + price_edit + " updated")


def stats_personnel(name):
    if name not in personnel:
        print("in barde vojod nadarad :( ")
        return
    print(name + " has " + str(personnel.get(name)) + " Price ")


def list_personnel():
    print(list(personnel.keys()))


def handler(quest):
    if quest == "list":
        list_personnel()

        return True
    name = input("Enter Name Personnel: ")

    if quest == "add":
        add_personnel(name)
    elif quest == "remove":
        remove_personnel(name)
    elif quest == "edit":
        edit_personnel(name)
    elif quest == "stats":
        stats_personnel(name)

    else:
        return False

    return True


def bardefrosh_run():
    while True:
        quest = input("Would you like to add,remove,edit,stats,list a personnel or exit?")
        if quest == "exit":
            break
        elif not handler(quest):
            print("Oops! Something went wrong.")