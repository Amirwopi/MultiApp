import os
import keyboard
from pystyle import Center


class _Colors:

    @staticmethod
    def _color_code(code):
        return f'\033[{code}m'

    ENDC: str = _color_code(0)
    BOLD: str = _color_code(1)
    UNDERLINE: str = _color_code(4)
    BLACK: str = _color_code(30)
    RED: str = _color_code(31)
    GREEN: str = _color_code(32)
    YELLOW: str = _color_code(33)
    BLUE: str = _color_code(34)
    MAGENTA: str = _color_code(35)
    CYAN: str = _color_code(36)
    WHITE: str = _color_code(37)
    REDBG: str = _color_code(41)
    GREENBG: str = _color_code(42)
    YELLOWBG: str = _color_code(43)
    BLUEBG: str = _color_code(44)
    MAGENTABG: str = _color_code(45)
    CYANBG: str = _color_code(46)
    WHITEBG: str = _color_code(47)
    GREY: str = _color_code(90)
    REDGREY: str = _color_code(91)
    GREENGREY: str = _color_code(92)
    YELLOWGREY: str = _color_code(93)
    BLUEGREY: str = _color_code(94)
    MAGENTAGREY: str = _color_code(95)
    CYANGREY: str = _color_code(96)
    WHITEGREY: str = _color_code(97)
    GREYBG: str = _color_code(100)
    REDGREYBG: str = _color_code(101)
    GREENGREYBG: str = _color_code(102)
    YELLOWGREYBG: str = _color_code(103)
    BLUEGREYBG: str = _color_code(104)
    MAGENTAGREYBG: str = _color_code(105)
    CYANGREYBG: str = _color_code(106)
    WHITEGREYBG: str = _color_code(107)


class _Styles:
    DEFAULT: int = 1
    SELECTED: int = 2
    ARROW: int = 3
    CENTERED: int = 11
    CENTEREDSELECTED: int = 22
    ARROWCENTERED: int = 33


Colors = _Colors()
Styles = _Styles()


class Menu:

    def __init__(self, options: list = None, color: str = Colors.CYAN, style: int = Styles.DEFAULT,
                 pretext: str = None):
        self.pretext = str(pretext)
        self.style = style
        self.options = options
        self.color = color
        self.index = 0
        if options is not None:
            self.index_max = len(options)
        self.selected = None
        self.json = {}
        self.selected_index = None
        self.last_known_index = 1

    def launch(self, response: str = "String"):
        return self._create_menu(response)

    def _create_menu(self, response: str = "String"):

        for index, option in enumerate(self.options):
            self.json[index] = option

        # Set up hotkeys for navigation
        keyboard.add_hotkey('up', self._up, suppress=True)
        keyboard.add_hotkey('down', self._down, suppress=True)
        keyboard.add_hotkey('enter', self._enter, suppress=True)
        keyboard.add_hotkey('right', self._enter, suppress=True)

        # Display the menu and wait for user input
        self._display()

        # Unhook all hotkeys after menu display
        keyboard.unhook_all()
        if response == "String":
            return self.selected
        return self.selected_index

    def _up(self):

        self.index = (self.index - 1) % self.index_max

    def _down(self):

        self.index = (self.index + 1) % self.index_max

    def _enter(self):

        self.selected = self.index

    def _style_parse_non_center(self):

        if self.style == 1:
            for i in range(self.index_max):
                if i == self.index:
                    print(self.color + self.json[i] + Colors.ENDC)
                else:
                    print(self.json[i])
        elif self.style == 2:
            for i in range(self.index_max):
                if i == self.index:
                    print(self.color + "> " + self.json[i] + " <" + Colors.ENDC)
                else:
                    print(self.json[i])
        elif self.style == 3:
            for i in range(self.index_max):
                if i == self.index:
                    print(self.color + "╰┈> " + self.json[i] + Colors.ENDC)
                else:
                    print(self.json[i])

    def _style_parse_center(self):
        equaling_space = "         "
        if self.style == 11:
            for i in range(self.index_max):
                if i == self.index:
                    sep = equaling_space
                    print(Center.XCenter(self.color + sep + self.json[i] + Colors.ENDC))
                else:
                    print(Center.XCenter(self.json[i]))
        if self.style == 22:
            for i in range(self.index_max):
                if i == self.index:
                    sep = equaling_space + ">"
                    print(Center.XCenter(self.color + sep + self.json[i] + "<" + Colors.ENDC))
                else:
                    print(Center.XCenter(self.json[i]))
        if self.style == 33:
            for i in range(self.index_max):
                if i == self.index:
                    sep = equaling_space + "↳ "
                    print(Center.XCenter(self.color + sep + self.json[i] + Colors.ENDC))
                else:
                    print(Center.XCenter(self.json[i]))

    def _display(self):
        self.index = 0
        self.selected = None

        while self.selected is None:
            if self.last_known_index != self.index:
                self.last_known_index = self.index
                self.cls()
                if self.pretext is not None:
                    if self.style in [11, 22, 33]:
                        print(Center.XCenter(self.pretext))
                        self._style_parse_center()
                    else:
                        print(self.pretext)
                        self._style_parse_non_center()
        self.selected = self.json[self.selected]
        self.selected_index = self.index

    def show_example(self):
        for example_style in [1, 2, 3, 11, 22, 33]:
            options = ["Option 1", "Option 2", "Option 3"]
            Menu(options=options, style=example_style).launch()

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'printf "\033c"')
