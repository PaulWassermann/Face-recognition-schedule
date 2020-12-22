class RegistrationMenuController:

    def __init__(self, gui):
        self.gui = gui

    def return_button_command(self):
        self.gui.registration_menu.hide()

        for entry in [self.gui.registration_menu.id_entry,
                      self.gui.registration_menu.first_name_entry,
                      self.gui.registration_menu.last_name_entry]:

            entry.delete(0, "end")

        if self.gui.registration_menu.itemcget(self.gui.registration_menu.error_message_id, "state") == "normal":
            self.gui.registration_menu.itemconfigure(self.gui.registration_menu.error_message_id, state="hidden")

        self.gui.start_menu.display()
