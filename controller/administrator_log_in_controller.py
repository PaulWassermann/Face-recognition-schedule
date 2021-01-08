from hashlib import sha256
from model.log import Log


class AdministratorLogInController:

    def __init__(self, gui):
        self.gui = gui

    def validation_button_command(self):

        encoded_username = sha256(self.gui.administrator_log_in.username_entry.get().encode("utf-8")).hexdigest()
        encoded_password = sha256(self.gui.administrator_log_in.password_entry.get().encode("utf-8")).hexdigest()

        if not self.gui.administrator_log_in.admin_registration:
            if encoded_username in self.gui.admins.keys() and encoded_password == self.gui.admins[encoded_username]:

                if self.gui.administrator_log_in.itemcget(self.gui.administrator_log_in.validation_error_message_id,
                                                          "state") \
                        == "normal":
                    self.gui.administrator_log_in.itemconfigure(
                        self.gui.administrator_log_in.validation_error_message_id,
                        state="hidden")

                self.gui.administrator_log_in.hide()
                self.gui.parameters_menu.display()

            else:
                self.gui.administrator_log_in.itemconfigure(self.gui.administrator_log_in.validation_error_message_id,
                                                            state="normal")

        elif self.gui.administrator_log_in.admin_registration:
            self.gui.admins[f"{encoded_username}"] = encoded_password
            Log().write_log_info(message="Un compte administrateur pour l'utilisateur "
                                         f"{self.gui.administrator_log_in.username_entry.get()} a été créé.")
            self.gui.administrator_log_in.toggle_admin_registration()
            self.gui.administrator_log_in.hide()
            self.gui.parameters_menu.display()

    def return_button_command(self):

        # Hiding error messages
        self.gui.administrator_log_in.itemconfigure(self.gui.administrator_log_in.required_field_error_message_id,
                                                    state="hidden")
        self.gui.administrator_log_in.itemconfigure(self.gui.administrator_log_in.password_error_message_id,
                                                    state="hidden")
        self.gui.administrator_log_in.itemconfigure(self.gui.administrator_log_in.validation_error_message_id,
                                                    state="hidden")

        if not self.gui.administrator_log_in.admin_registration:
            self.gui.administrator_log_in.hide()
            self.gui.start_menu.display()

        elif self.gui.administrator_log_in.admin_registration:
            self.gui.administrator_log_in.toggle_admin_registration()
            self.gui.administrator_log_in.hide()
            self.gui.parameters_menu.display()
