from time import sleep

from gamenumber import gamenumber_run
from mashinhesab import run_calculator
from multimashinhesab import multi_mashin_run
from worldcounting import counting_run
from bardeforosh import bardefrosh_run

import menu

app = ["BardeFroshi", "GameNumber", "CountWorld", "Mashin-hesab", "Multi-Mashin-Hesab"]
print("Welcome to My App")
sleep(0.5)
menu_ex = menu.Menu(
    app,
    color=menu.Colors.REDGREY,
    style=menu.Styles.ARROW,
    pretext="Select an App"
)


def main():
    while True:
        User_choice = menu_ex.launch(response="String")
        debug = f"Selected {menu_ex.selected}, index = {menu_ex.selected_index}, {User_choice}"
        print(debug)
        match User_choice:
            case "Mashin-hesab":
                print(menu.Colors.REDGREY, "OK")
                run_calculator()
            case "Multi-Mashin-Hesab":
                print(menu.Colors.RED, "OK")
                multi_mashin_run()
            case "CountWorld":
                print(menu.Colors.CYAN, "OK")
                counting_run()
            case "GameNumber":
                print(menu.Colors.RED, "OK")
                gamenumber_run()
            case "BardeFroshi":
                print(menu.Colors.RED, "OK")
                bardefrosh_run()
            case _:
                print("lotfan entekhab konid")


if __name__ == '__main__':
    main()
