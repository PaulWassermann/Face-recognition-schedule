from model.resizable_image import ResizableImage
from tkinter import Frame, Button, BooleanVar


# This class creates a working touch keyboard


class TouchKeyboard(Frame):

    def __init__(self, gui):

        self.gui = gui
        self.width = 0.55 * self.gui.width
        self.height = 0.4 * self.gui.height

        super().__init__(self.gui.root, width=self.width, height=self.height, bg="white")
        self.place(x=self.gui.width // 2, y=self.gui.height - 1.05 * self.height, anchor="n")
        self.lower()

        self.keyboard_frame_1_upper = Frame(self, width=self.width, height=self.height, bg="white")

        self.keyboard_frame_1_lower = Frame(self, width=self.width, height=self.height, bg="white")

        self.keyboard_frame_2_upper = Frame(self, width=self.width, height=self.height, bg="white")

        self.keyboard_frame_2_lower = Frame(self, width=self.width, height=self.height, bg="white")

        self.keyboard_frames = {"1": {"upper": self.keyboard_frame_1_upper, "lower": self.keyboard_frame_1_lower},
                                "2": {"upper": self.keyboard_frame_2_upper, "lower": self.keyboard_frame_2_lower}}

        self.key_width = self.width // 11.1
        self.key_height = self.height // 5.9
        self.key_gap = self.key_width // 10
        self.row_gap = 3 * self.key_height // 20

        self.keys = {"1": {"upper": [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
                                     [["A", [["Å", "Æ", "Ā", "Ă", "Ą"], ["À", "Á", "Â", "Ã", "Ä"]]],
                                      ["Z", [["Ź", "Ż", "Ž"]]],
                                      ["E", [["Ė", "Ę", "Ě", "Ĕ", "Ə"], ["É", "È", "Ê", "Ë", "Ē"]]],
                                      ["R", [["Ŕ", "Ř"]]],
                                      ["T", [["Þ", "Ť", "Ț", "Ţ"]]],
                                      ["Y", ["Ý"]],
                                      ["U", [["Ų", "Ű", "Ů", "Ū"], ["Ü", "Ú", "Ù", "Û"]]],
                                      ["I", [["Į", "Ī", "Î"], ["Í", "Ì", "Ï"]]],
                                      ["O", [["Ő", "Ø", "Ö", "Õ"], ["Ó", "Ò", "Œ", "Ô"]]], "P"],
                                     ["Q",
                                      ["S", [["ß", "§", "Ś", "Š", "Ş"]]],
                                      ["D", [["Ď", "Đ"]]],
                                      "F",
                                      ["G", [["Ģ", "Ğ"]]],
                                      "H", "J",
                                      ["K", ["Ķ"]],
                                      ["L", [["Ł", "Ľ", "Ļ", "Ĺ"]]],
                                      "M"],
                                     ["shift", "", "W", "X",
                                      ["C", [["Ç", "Ć", "Č"]]], "V", "B",
                                      ["N", [["Ň", "Ņ", "Ń", "Ñ"]]],
                                      "backspace"],
                                     ["1_out_of_2", "", "spacebar", "", "", "", "", "", "return"]],
                           "lower": [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
                                     [["a", [["å", "æ", "ā", "ă", "ą"], ["à", "á", "â", "ã", "ä"]]],
                                      ["z", [["ź", "ż", "ž"]]],
                                      ["e", [["ė", "ę", "ě", "ĕ", "ǝ"], ["é", "è", "ê", "ë", "ē"]]],
                                      ["r", [["ŕ", "ř"]]],
                                      ["t", [["þ", "ť", "ț", "ţ"]]],
                                      ["y", ["ý"]],
                                      ["u", [["ų", "ű", "ů", "ū"], ["ü", "ú", "ù", "û"]]],
                                      ["i", [["į", "ī", "î"], ["í", "ì", "ï"]]],
                                      ["o", [["ő", "ø", "ö", "õ"], ["ó", "ò", "œ", "ô"]]], "p"],
                                     ["q",
                                      ["s", [["ß", "§", "ś", "š", "ş"]]],
                                      ["d", [["ď", "đ"]]],
                                      "f",
                                      ["g", [["ģ", "ğ"]]],
                                      "h", "j",
                                      ["k", ["ķ"]],
                                      ["l", [["ł", "ľ", "ļ", "ĺ"]]],
                                      "m"],
                                     ["shift", "", "w", "x",
                                      ["c", [["ç", "ć", "č"]]],
                                      "v", "b",
                                      ["n", [["ň", "ņ", "ń", "ñ"]]],
                                      "backspace"],
                                     ["1_out_of_2", "", "spacebar", "", "", "", "", "", "return"]]},
                     "2": {"upper": [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
                                     ["+", "×", "÷", "=",
                                      ["slash", [["vertical_bar", "backslash"]]],
                                      "_",
                                      ["€", [["£", "¥", "₩"]]],
                                      "$", "lesser_than", "greater_than"],
                                     [["!", ["¡"]],
                                      "@", "#", "%", "^", "&", "asterisk", "°",
                                      ["(", [["[", "{"]]],
                                      [")", [["]", "}"]]]],
                                     ["shift", "",
                                      ["-", ["~"]],
                                      ["'", ["`"]],
                                      "double_quote", ",",
                                      ["colon", [";"]],
                                      ["question_mark", ["¿"]],
                                      "backspace"],
                                     ["2_out_of_2", "", "spacebar", "", "", "", "", "", "return"]],
                           "lower": [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
                                     ["+", "×", "÷", "=",
                                      ["slash", [["vertical_bar", "backslash"]]],
                                      "_",
                                      ["€", [["£", "¥", "₩"]]],
                                      "$", "lesser_than", "greater_than"],
                                     [["!", ["¡"]],
                                      "@", "#", "%", "^", "&", "asterisk", "°",
                                      ["(", [["[", "{"]]],
                                      [")", [["]", "}"]]]],
                                     ["shift", "",
                                      ["-", ["~"]],
                                      ["'", ["`"]],
                                      "double_quote", ",",
                                      ["colon", [";"]],
                                      ["question_mark", ["¿"]],
                                      "backspace"],
                                     ["2_out_of_2", "", "spacebar", "", "", "", "", "", "return"]]}
                     }

        self.key_images = {"1": {"upper": [],
                                 "lower": []},
                           "2": {"upper": [],
                                 "lower": []}}
        self.key_buttons = {"1": {"upper": [],
                                  "lower": []},
                            "2": {"upper": [],
                                  "lower": []}}

        self.create_buttons()

        for keyboard in self.keyboard_frames:
            for capitalization in self.keyboard_frames[keyboard]:
                self.keyboard_frames[keyboard][capitalization].place(x=0, y=0)

        self.entry = None
        self.active_keyboard = "1"
        self.capitalization = "upper"
        self.caps_lock = False
        self.id_after_complex_key = 0
        self.active_complex_key = BooleanVar(value=False)
        self.active_complex_key_frame = None

    def create_buttons(self):

        for super_key in self.keys:

            for capitalization in self.keys[super_key]:

                for super_index, row in enumerate(self.keys[super_key][capitalization]):

                    self.key_buttons[super_key][capitalization].append([])
                    self.key_images[super_key][capitalization].append([])

                    for index, key in enumerate(row):

                        if type(key) is str:

                            if key == "shift":
                                self.key_images[super_key][capitalization][super_index].append(
                                    ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{key}.png").
                                        resize_to_tk(width=2 * self.key_width + self.key_gap,
                                                     height=self.key_height))

                                self.key_buttons[super_key][capitalization][super_index].append(Button(
                                    self.keyboard_frames[super_key][capitalization],
                                    image=self.key_images[super_key][capitalization][super_index][index],
                                    anchor="nw", bg="white", relief="flat",
                                    command=self.toggle_shift))

                            elif key == "backspace":
                                self.key_images[super_key][capitalization][super_index].append(
                                    ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{key}.png").
                                        resize_to_tk(width=2 * self.key_width + self.key_gap,
                                                     height=self.key_height))

                                self.key_buttons[super_key][capitalization][super_index].append(Button(
                                    self.keyboard_frames[super_key][capitalization],
                                    image=self.key_images[super_key][capitalization][super_index][index],
                                    anchor="nw", bg="white", relief="flat",
                                    command=lambda: [self.toggle_complex_key(only_if_active=True),
                                                     self.entry.delete(self.entry.index("insert") - 1),
                                                     self.toggle_shift(only_if_inactive=True)
                                                     if self.entry.index("insert") == 0 else None],
                                    repeatdelay=500,
                                    repeatinterval=100))

                            elif key == "1_out_of_2" or key == "2_out_of_2":
                                self.key_images[super_key][capitalization][super_index].append(
                                    ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{key}.png").
                                        resize_to_tk(width=2 * self.key_width + self.key_gap,
                                                     height=self.key_height))

                                self.key_buttons[super_key][capitalization][super_index].append(Button(
                                    self.keyboard_frames[super_key][capitalization],
                                    image=self.key_images[super_key][capitalization][super_index][index],
                                    anchor="nw", bg="white", relief="flat",
                                    command=lambda: self.toggle_keyboards()))

                            elif key == "spacebar":
                                self.key_images[super_key][capitalization][super_index].append(
                                    ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{key}.png").
                                        resize_to_tk(width=6 * self.key_width + 5 * self.key_gap,
                                                     height=self.key_height))

                                self.key_buttons[super_key][capitalization][super_index].append(Button(
                                    self.keyboard_frames[super_key][capitalization],
                                    image=self.key_images[super_key][capitalization][super_index][index],
                                    anchor="nw", bg="white", relief="flat",
                                    command=lambda: [self.toggle_complex_key(only_if_active=True),
                                                     self.entry.insert(self.entry.index("insert"), " ") if
                                                     (len(self.entry.get()) > 0 and self.entry.get()[
                                                         self.entry.index("insert") - 1] != " ")
                                                     else None]))

                            elif key == "return":
                                self.key_images[super_key][capitalization][super_index].append(
                                    ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{key}.png").
                                        resize_to_tk(width=2 * self.key_width + self.key_gap,
                                                     height=self.key_height))

                                self.key_buttons[super_key][capitalization][super_index].append(Button(
                                    self.keyboard_frames[super_key][capitalization],
                                    image=self.key_images[super_key][capitalization][super_index][index],
                                    anchor="nw", bg="white", relief="flat",
                                    command=lambda: [self.toggle_complex_key(only_if_active=True),
                                                     self.entry.tk_focusNext().focus(), self.toggle_shift()]))

                            elif key == "":
                                self.key_buttons[super_key][capitalization][super_index].append("")
                                self.key_images[super_key][capitalization][super_index].append("")

                            else:
                                self.key_images[super_key][capitalization][super_index].append(
                                    ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{key}.png").
                                        resize_to_tk(width=self.key_width, height=self.key_height))

                                self.key_buttons[super_key][capitalization][super_index].append(Button(
                                    self.keyboard_frames[super_key][capitalization],
                                    image=self.key_images[super_key][capitalization][super_index][index],
                                    anchor="nw", bg="white", relief="flat",
                                    command=lambda i=super_key, j=capitalization, k=super_index,
                                                   l=index: self.entry.insert(
                                        self.entry.index("insert"),
                                        self.formatted_letter(self.keys[i][j][k][l]))))

                            if key != "":
                                self.key_buttons[super_key][capitalization][super_index][index].place(
                                    x=(1 + index) * self.key_gap + index * self.key_width,
                                    y=(1 + super_index) * self.row_gap + super_index * self.key_height)

                        elif type(key) is list:

                            main_key = key[0]

                            self.key_buttons[super_key][capitalization][super_index].append([])
                            self.key_images[super_key][capitalization][super_index].append([])

                            self.key_images[super_key][capitalization][super_index][index].append(
                                ResizableImage(path_to_image=f"assets/keyboard/{capitalization}/{main_key}.png").
                                    resize_to_tk(width=self.key_width, height=self.key_height))

                            self.key_buttons[super_key][capitalization][super_index][index].append(Button(
                                self.keyboard_frames[super_key][capitalization],
                                image=self.key_images[super_key][capitalization][super_index][index][0],
                                anchor="nw", bg="white", relief="flat",
                                command=None))

                            self.key_buttons[super_key][capitalization][super_index][index][0].bind(
                                "<ButtonPress-1>", lambda e,
                                                          i=super_key,
                                                          j=capitalization,
                                                          k=super_index,
                                                          l=index: self.complex_key_handler(i, j, k, l))

                            self.key_buttons[super_key][capitalization][super_index][index][0].bind(
                                "<ButtonRelease-1>", lambda e,
                                                            i=super_key,
                                                            j=capitalization,
                                                            k=super_index,
                                                            l=index: [self.entry.insert(self.entry.index("insert"),
                                                                                        self.formatted_letter(
                                                                                            self.keys[i][j][k][l][0])),
                                                                      self.gui.root.after_cancel(
                                                                          self.id_after_complex_key)]
                                if not self.active_complex_key.get() else None)

                            self.key_buttons[super_key][capitalization][super_index][index][0].place(
                                x=(1 + index) * self.key_gap + index * self.key_width,
                                y=(1 + super_index) * self.row_gap + super_index * self.key_height)

                            rows = len(self.keys[super_key][capitalization][super_index][index][1])
                            columns = len(self.keys[super_key][capitalization][super_index][index][1][0])
                            width = columns * self.key_width + (columns + 3) * self.key_gap
                            height = rows * self.key_height + (rows + 3) * self.row_gap

                            self.key_buttons[super_key][capitalization][super_index][index].append(
                                Frame(self.gui.root, width=width, height=height, bg="white",
                                      borderwidth=4, relief="ridge"))

                            self.key_images[super_key][capitalization][super_index][index].append([])

                            for minor_index, minor_row in enumerate(
                                    self.keys[super_key][capitalization][super_index][index][1]):

                                self.key_images[super_key][capitalization][super_index][index][1].append(
                                    [])

                                for super_minor_index, minor_key in enumerate(minor_row):
                                    self.key_images[super_key][capitalization][super_index][index][1][minor_index]. \
                                        append(ResizableImage(
                                        path_to_image=f"assets/keyboard/{capitalization}/{minor_key}.png").
                                               resize_to_tk(width=self.key_width, height=self.key_height))

                                    button = Button(self.key_buttons[super_key][capitalization][super_index][index][1],
                                                    image=
                                                    self.key_images[super_key][capitalization][super_index][index][1]
                                                    [minor_index][super_minor_index],
                                                    anchor="nw", bg="white", relief="flat",
                                                    command=lambda i=super_key,
                                                                   j=capitalization,
                                                                   k=super_index,
                                                                   l=index,
                                                                   m=minor_index,
                                                                   n=super_minor_index:
                                                    [self.active_complex_key.set(value=False),
                                                     self.entry.insert(
                                                         self.entry.index("insert"),
                                                         self.formatted_letter(self.keys[i][j][k][l][1][m][n]))])

                                    button.place(
                                        x=(1 + super_minor_index) * self.key_gap + super_minor_index * self.key_width,
                                        y=(1 + minor_index) * self.row_gap + minor_index * self.key_height)

    def toggle_shift(self, only_if_inactive=False):

        if not self.caps_lock:

            if self.capitalization == "upper":

                if not only_if_inactive:
                    self.capitalization = "lower"

            else:
                self.capitalization = "upper"

            self.keyboard_frames[self.active_keyboard][self.capitalization].tkraise()

            if self.active_complex_key.get():
                self.toggle_complex_key()
                self.active_complex_key_frame[1][1] = self.capitalization
                self.toggle_complex_key(*self.active_complex_key_frame[1])

    def toggle_caps_lock(self):

        if self.caps_lock:
            self.caps_lock = False

        elif not self.caps_lock:
            self.caps_lock = False

    def toggle_keyboards(self):

        self.toggle_complex_key(only_if_active=True)

        if self.active_keyboard == "1":
            self.active_keyboard = "2"

        elif self.active_keyboard == "2":
            self.active_keyboard = "1"

        self.keyboard_frames[self.active_keyboard][self.capitalization].tkraise()

    def formatted_letter(self, letter):

        if letter == "asterisk":
            letter = "*"

        elif letter == "backslash":
            letter = "\\"

        elif letter == "colon":
            letter = ":"

        elif letter == "double_quote":
            letter = '"'

        elif letter == "greater_than":
            letter = ">"

        elif letter == "lesser_than":
            letter = "<"

        elif letter == "question_mark":
            letter = "?"

        elif letter == "slash":
            letter = "/"

        elif letter == "vertical_bar":
            letter = "|"
        if self.capitalization == "lower":
            return letter

        else:
            self.toggle_complex_key(only_if_active=True)
            self.toggle_shift()
            return letter

    def complex_key_handler(self, i, j, k, l):

        if not self.active_complex_key.get():
            self.id_after_complex_key = self.gui.root.after(800, func=lambda: self.toggle_complex_key(i, j, k, l))

        elif [i, j, k, l] != self.active_complex_key_frame[1]:
            self.toggle_complex_key(only_if_active=True)
            self.id_after_complex_key = self.gui.root.after(800,
                                                            func=lambda: self.toggle_complex_key(i, j, k, l))

        else:
            self.toggle_complex_key()
            self.formatted_letter(self.keys[i][j][k][l][0])

    def toggle_complex_key(self, i=None, j=None, k=None, l=None, only_if_active=False):

        if not self.active_complex_key.get():

            if not only_if_active:
                self.active_complex_key.set(value=True)
                self.active_complex_key_frame = [self.key_buttons[i][j][k][l][1], [i, j, k, l]]
                self.active_complex_key_frame[0].place(
                    x=self.winfo_x() + (1 + l) * self.key_gap + int((1 / 2 + l) * self.key_width),
                    y=self.winfo_y() + (1 + k) * self.row_gap + int((k - 1 / 4) * self.key_height), anchor="s")
                self.active_complex_key_frame[0].tkraise()

                self.gui.root.wait_variable(self.active_complex_key)
                self.active_complex_key_frame[0].place_forget()

            else:
                pass

        else:

            if self.active_complex_key.get():
                self.active_complex_key.set(value=False)
                self.active_complex_key_frame[0].place_forget()

    def display(self, event):

        self.entry = event.widget

        if self.entry.index("insert") == 0 and len(self.entry.get()) == 0:
            self.capitalization = "upper"

        else:
            self.capitalization = "lower"

        self.keyboard_frames[self.active_keyboard][self.capitalization].tkraise()

        self.tkraise()

    def hide(self):

        self.toggle_complex_key(only_if_active=True)

        self.active_keyboard = "1"

        self.lower()
