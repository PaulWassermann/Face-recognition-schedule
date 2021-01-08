# The controller for the language selection pop-up menu


class LanguageSelectionController:

    def __init__(self, gui):
        self.gui = gui

    # As hinted by the its name, this method modify the attributes relative to the language
    def update_language(self, new_language):
        self.gui.language = new_language
        self.gui.start_menu.language_button.update_image(*self.gui.language_assets[self.gui.language])
        self.update_text()

    # This method updates specifically all the texts in the app
    def update_text(self):
        # Updating texts in start menu
        self.gui.start_menu.registration_button.update_text(self.gui.text_resources[self.gui.language]
                                                            ["registration_button"])
        self.gui.start_menu.recognition_button.update_text(self.gui.text_resources[self.gui.language]
                                                           ["recognition_button"])
        self.gui.start_menu.itemconfigure(self.gui.start_menu.title_id, text=self.gui.text_resources[self.gui.language]
                                          ["title"])

        # Updating texts in registration menu
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.first_name_text,
                                                 text=self.gui.text_resources[self.gui.language]["name"])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.last_name_text,
                                                 text=self.gui.text_resources[self.gui.language]["last_name"])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.id_label_text,
                                                 text=self.gui.text_resources[self.gui.language]["student_number"])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.student_number_error_message,
                                                 text=self.gui.text_resources[self.gui.language]
                                                 ["student_number_error_message"])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.required_field_error_message_1,
                                                 text=self.gui.text_resources[self.gui.language]
                                                 ["required_field_error_message"])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.required_field_error_message_2,
                                                 text=self.gui.text_resources[self.gui.language]
                                                 ["required_field_error_message"])

        # Updating texts in recognition menu
