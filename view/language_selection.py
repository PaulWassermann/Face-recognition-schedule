from controller.language_selection_controller import LanguageSelectionController
from view.round_button import RoundButton
from tkinter import Canvas, Frame


class LanguageSelection(Frame):

    def __init__(self, gui):
        self.gui = gui

        self.button_radius = int(self.gui.width // 16)
        self.button_gap = 0.1 * self.button_radius

        self.width = 2 * len(self.gui.text_resources.keys()) * self.button_radius + 4 * self.button_gap
        self.height = 2 * self.button_radius + 2 * self.button_gap

        super().__init__(self.gui.root, width=self.width, height=self.height, borderwidth=4, relief="ridge")
        self.place(x=self.gui.width // 2, y=self.gui.height // 2, anchor="center")
        self.lower()

        self.controller = LanguageSelectionController(self.gui)

        self.canvas = Canvas(self, width=self.width, height=self.height, bg="white", border=0, highlightthickness=0)

        self.background_image = self.gui.background_image.resize_to_tk(width=self.width, height=self.height)
        self.background_id = self.canvas.create_image(0, 0,
                                                      image=self.background_image,
                                                      anchor="nw")

        self.canvas.pack(expand='yes')

        self.buttons = {}

        for index, language in enumerate(self.gui.text_resources.keys()):
            self.buttons[language] = RoundButton(canvas=self.canvas,
                                                 gui=self.gui,
                                                 x=int((index + 1) * self.button_gap +
                                                       2 * (index + 1 / 2) * self.button_radius),
                                                 y=self.button_gap + self.button_radius,
                                                 radius=self.button_radius,
                                                 image=self.gui.language_assets[language][0],
                                                 image_on_click=self.gui.language_assets[language][1],
                                                 command=lambda param=language: [self.controller.update_language(param),
                                                                                 self.hide()])

    def display(self):
        self.tkraise()
        self.gui.start_menu.bind("<Button-1>", lambda e: self.hide())

    def hide(self):
        self.lower()
        self.gui.start_menu.unbind("<Button-1>")
