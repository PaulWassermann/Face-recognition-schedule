from controller.language_selection_controller import LanguageSelectionController
from controller.start_menu_controller import StartMenuController
from model.round_button import RoundButton
from tkinter import Canvas


class StartMenu(Canvas):

    def __init__(self, gui):
        self.gui = gui
        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        # Initializing the controller
        self.controller = StartMenuController(self.gui)
        self.language_controller = LanguageSelectionController(self.gui)

        # Styling elements
        self.background_id = self.create_image(0, 0, image=self.gui.global_background_image, anchor="nw")

        self.cm_logo_id = self.create_image(5, 5, image=self.gui.global_cm_logo_image, anchor="nw")

        self.title_id = self.create_text(0.5 * self.gui.width,
                                         0.1 * self.gui.height,
                                         text="Mon Emploi du Temps",
                                         font=('helvetica', 50),
                                         fill="green",
                                         anchor="n")

        # Buttons
        self.registration_button = RoundButton(canvas=self,
                                               gui=self.gui,
                                               x=0.3 * self.gui.width,
                                               y=0.6 * self.gui.height,
                                               radius=0.15 * self.gui.width,
                                               text=gui.text_resources[gui.language]['registration_button'],
                                               font=('helvetica', 16),
                                               text_color="green",
                                               image=self.gui.registration_button_image,
                                               image_on_click=self.gui.registration_button_on_click_image,
                                               command=self.controller.registration_button_command)

        self.recognition_button = RoundButton(canvas=self,
                                              gui=self.gui,
                                              x=0.7 * self.gui.width,
                                              y=0.6 * self.gui.height,
                                              radius=0.15 * self.gui.width,
                                              text=gui.text_resources[gui.language]['recognition_button'],
                                              font=('helvetica', 14),
                                              text_color="green",
                                              justify="center",
                                              image=self.gui.schedule_button_image,
                                              image_on_click=self.gui.schedule_button_on_click_image,
                                              command=self.controller.recognition_button_command)

        self.parameters_button = RoundButton(canvas=self,
                                             gui=self.gui,
                                             x=0.95 * self.gui.width,
                                             y=0.08 * self.gui.height,
                                             radius=0.03 * self.gui.width,
                                             image=self.gui.parameters_button,
                                             image_on_click=self.gui.parameters_button_on_click,
                                             command=self.controller.parameters_button_command)

        self.language_button = RoundButton(canvas=self,
                                           gui=self.gui,
                                           x=0.95 * self.gui.width,
                                           y=0.92 * self.gui.height,
                                           radius=0.04 * self.gui.width,
                                           image=self.gui.language_assets[self.gui.language][0],
                                           image_on_click=self.gui.language_assets[self.gui.language][1],
                                           command=self.controller.language_selection_button_command)

    def display(self):
        self.pack(expand='yes')

    def hide(self):
        self.pack_forget()
