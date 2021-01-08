from controller.parameters_menu_controller import ParametersMenuController
from view.round_button import RoundButton
from tkinter import *


class ParametersMenu(Canvas):

    def __init__(self, gui):
        self.gui = gui
        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        # Initializing the controller
        self.controller = ParametersMenuController(self.gui)

        self.background_id = self.create_image(0, 0, image=self.gui.global_background_image, anchor="nw")
        self.cm_logo_id = self.create_image(5, 5, image=self.gui.global_cm_logo_image, anchor="nw")

        # Administrator registration button
        self.registration_button = Button(self, text="Enregistrer un\nnouvel administrateur", font=('helvetica', 28),
                                          justify="center",
                                          fg="green", bg="white",
                                          activeforeground="green", activebackground="white",
                                          relief="flat",
                                          takefocus=False,
                                          command=lambda: [self.hide(),
                                                           self.gui.administrator_log_in.toggle_admin_registration(),
                                                           self.gui.administrator_log_in.display()])

        self.registration_button.place(x=int(0.5 * self.gui.width), y=int(0.5 * self.gui.height), anchor="center")

        # Quit button
        self.quit_button = Button(self, text="Fermer l'application", font=('helvetica', 28),
                                  fg="green", bg="white",
                                  activeforeground="green", activebackground="white",
                                  relief="flat",
                                  takefocus=False,
                                  command=self.controller.quit_button_command)

        self.quit_button.place(x=int(0.5 * self.gui.width), y=int(0.9 * self.gui.height), anchor="center")

        # Return Button
        self.return_button = RoundButton(canvas=self,
                                         gui=self.gui,
                                         x=0.95 * self.gui.width,
                                         y=0.08 * self.gui.height,
                                         radius=40,
                                         image=self.gui.return_button_image,
                                         image_on_click=self.gui.return_button_on_click_image,
                                         command=self.controller.return_button_command)

    def display(self):
        self.pack(expand="yes")

    def hide(self):
        self.pack_forget()
