# The controller for the registration menu


class RegistrationMenuController:

    def __init__(self, gui):
        self.gui = gui

    # Triggered when the return button of the registration menu is clicked, returns to start menu
    def return_button_command(self):

        self.gui.registration_menu.hide()

        # Erasing the entries
        for entry in [self.gui.registration_menu.id_entry,
                      self.gui.registration_menu.first_name_entry,
                      self.gui.registration_menu.last_name_entry]:
            entry.delete(0, "end")

        # Disabling the validation button
        if self.gui.registration_menu.validation_button["state"] == "active":
            self.gui.registration_menu.validation_button["state"] = "disabled"

        # Hiding error messages
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.student_number_error_message,
                                                 state="hidden")
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.required_field_error_message_1,
                                                 state="hidden")
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.required_field_error_message_2,
                                                 state="hidden")

        # Closing the cam
        if not self.gui.registration_menu.done.get():
            self.gui.registration_menu.done.set(value=True)

        # Resetting the timers if needed
        if self.gui.registration_menu.set_timer:
            self.gui.registration_menu.cancel_timer()

        self.gui.start_menu.display()
