from controller.administrator_log_in_controller import AdministratorLogInController
from view.round_button import RoundButton
from hashlib import sha256
from tkinter import *


class AdministratorLogIn(Canvas):

    def __init__(self, gui):
        self.gui = gui
        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        # Initializing the controller
        self.controller = AdministratorLogInController(self.gui)

        self.background_id = self.create_image(0, 0, image=self.gui.global_background_image, anchor="nw")
        self.cm_logo_id = self.create_image(5, 5, image=self.gui.global_cm_logo_image, anchor="nw")

        self.admin_registration = False

        self.username = StringVar(value="")
        self.password = StringVar(value="")
        self.password_confirmation = StringVar(value="")

        self.username_text_id = self.create_text(0.20 * self.gui.width, 0.3 * self.gui.height,
                                                 text="Nom d'utilisateur",
                                                 font=('helvetica', 28), anchor="nw")
        self.password_text_id = self.create_text(0.20 * self.gui.width, 0.4 * self.gui.height,
                                                 text="Mot de passe",
                                                 font=('helvetica', 28), anchor="nw")
        self.password_confirmation_text_id = self.create_text(0.20 * self.gui.width, 0.5 * self.gui.height,
                                                              text="Confirmer le\nmot de passe",
                                                              font=('helvetica', 28),
                                                              justify="left", anchor="nw", state="hidden")

        self.required_field_error_message_id = self.create_text(0.4 * self.gui.width, 0.35 * self.gui.height,
                                                                text="Champ requis",
                                                                font=("Helvetica", 14),
                                                                fill="red", anchor="nw", state="hidden")

        self.already_exists_error_message_id = self.create_text(0.4 * self.gui.width, 0.35 * self.gui.height,
                                                                text="Ce nom d'utilisateur n'est pas disponible",
                                                                font=("Helvetica", 14),
                                                                fill="red", anchor="nw", state="hidden")

        self.password_error_message_id = self.create_text(0.4 * self.gui.width, 0.45 * self.gui.height,
                                                          text="Le mot de passe doit contenir 8 caractères ou plus",
                                                          font=("Helvetica", 14),
                                                          fill="red", anchor="nw", state="hidden")

        self.password_confirmation_error_message_id = self.create_text(0.4 * self.gui.width, 0.55 * self.gui.height,
                                                                       text="Vous avez saisi deux mots de passe"
                                                                            " différents",
                                                                       font=("Helvetica", 14),
                                                                       fill="red", anchor="nw", state="hidden")

        self.validation_error_message_id = self.create_text(0.5 * self.gui.width, 0.8 * self.gui.height,
                                                            text="Le mot de passe ou le nom d'utilisateur est "
                                                                 "incorrect",
                                                            font=("Helvetica", 14),
                                                            fill="red", anchor="center", state="hidden")

        self.username_entry = Entry(self, textvariable=self.username, font=('helvetica', 24), width=30)
        self.password_entry = Entry(self, textvariable=self.password, font=('helvetica', 24), show="\u2022", width=30)
        self.password_confirmation_entry = Entry(self, textvariable=self.password_confirmation, font=('helvetica', 24),
                                                 show="\u2022", width=30)

        self.username_entry.bind("<FocusOut>",
                                 lambda e: [self.itemconfigure(self.required_field_error_message_id,
                                                               state="normal")
                                            if len(self.username_entry.get()) == 0
                                               and self.admin_registration else
                                            (self.itemconfigure(self.required_field_error_message_id, state="hidden") if
                                             self.itemcget(self.required_field_error_message_id,
                                                           "state") == "normal" else None),
                                            self.itemconfigure(self.already_exists_error_message_id,
                                                               state="normal")
                                            if sha256(self.username_entry.get().encode("utf-8")).hexdigest()
                                               in self.gui.admins.keys()
                                               and self.admin_registration else
                                            (self.itemconfigure(self.already_exists_error_message_id, state="hidden") if
                                             self.itemcget(self.already_exists_error_message_id,
                                                           "state") == "normal" else None)]
                                 )

        self.password_entry.bind("<FocusOut>",
                                 lambda e: self.itemconfigure(self.password_error_message_id,
                                                              state="normal")
                                 if 0 < len(self.password_entry.get()) < 8 and self.admin_registration else
                                 (self.itemconfigure(self.password_error_message_id, state="hidden") if
                                  self.itemcget(self.password_error_message_id, "state") == "normal" else None))

        self.password_confirmation_entry.bind("<FocusOut>",
                                              lambda e: self.itemconfigure(
                                                  self.password_confirmation_error_message_id,
                                                  state="normal")
                                              if self.password_confirmation_entry.get() != self.password_entry.get()
                                                 and len(self.password_entry.get()) > 0
                                              else
                                              (self.itemconfigure(self.password_confirmation_error_message_id,
                                                                  state="hidden") if
                                               self.itemcget(self.password_confirmation_error_message_id,
                                                             "state") == "normal" else None))

        self.username_entry.place(x=0.4 * self.gui.width, y=0.3 * self.gui.height)
        self.password_entry.place(x=0.4 * self.gui.width, y=0.4 * self.gui.height)

        # Validation Button
        self.validation_button = Button(self, text="Valider", font=('helvetica', 24),
                                        fg="green", bg="white",
                                        activeforeground="green", activebackground="white",
                                        relief="flat",
                                        takefocus=False,
                                        command=self.controller.validation_button_command)

        self.validation_button.place(x=0.5 * self.gui.width, y=0.75 * self.gui.height, anchor="center")

        # Return Button
        self.return_button = RoundButton(canvas=self,
                                         gui=self.gui,
                                         x=0.95 * self.gui.width,
                                         y=0.08 * self.gui.height,
                                         radius=40,
                                         image=self.gui.return_button_image,
                                         image_on_click=self.gui.return_button_on_click_image,
                                         command=self.controller.return_button_command)

    def toggle_admin_registration(self):

        if not self.admin_registration:
            self.admin_registration = True
            self.itemconfigure(self.password_confirmation_text_id, state="normal")
            self.password_confirmation_entry.place(x=int(0.4 * self.gui.width), y=int(0.5 * self.gui.height))
            self.validation_button["state"] = "disabled"

        elif self.admin_registration:
            self.admin_registration = False
            self.itemconfigure(self.password_confirmation_text_id, state="hidden")
            self.password_confirmation_entry.place_forget()

    def enable_validation_button(self):

        if self.admin_registration:
            if len(self.username_entry.get()) > 0 and self.username_entry.get() not in self.gui.admins.keys() \
                    and len(self.password_entry.get()) > 0 \
                    and self.password_confirmation_entry.get() == self.password_entry.get():
                self.validation_button["state"] = "active"

            else:
                self.validation_button["state"] = "disabled"

    def display(self):

        # Linking the touch keyboard
        self.bind("<Button-1>", lambda e: self.focus_set())
        self.gui.root.bind_class("Entry", "<FocusIn>", lambda e: self.gui.touch_keyboard.display(e))
        self.gui.root.bind_class("Entry", "<FocusOut>", lambda e: [self.gui.touch_keyboard.hide(),
                                                                   self.enable_validation_button()])

        self.pack(expand="yes")

    def hide(self):

        self.unbind("<Button-1>")
        self.gui.root.unbind_class("Entry", "<FocusIn>")
        self.gui.root.unbind_class("Entry", "<FocusOut>")

        # Erasing the entries
        for entry in [self.username_entry,
                      self.password_entry,
                      self.password_confirmation_entry]:
            entry.delete(0, "end")

        self.pack_forget()
