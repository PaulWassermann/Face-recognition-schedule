class LanguageController:

    def __init__(self, gui):
        self.gui = gui

    def change_language(self):
        """Change gui variable language"""
        if self.gui.language == 'en':
            self.gui.language = 'es'
        elif self.gui.language == 'es':
            self.gui.language = 'fr'
        elif self.gui.language == 'fr':
            self.gui.language = 'en'

        self.update_language()

        print(self.gui.language)


    def update_language(self):
        """Update text to correspond to actual language choice"""

        #update start_menu
        self.gui.start_menu.registration_button.update_text(self.gui.language_text[self.gui.language]['registration_button'])
        self.gui.start_menu.recognition_button.update_text(self.gui.language_text[self.gui.language]['recognition_button'])
        self.gui.start_menu.itemconfigure(self.gui.start_menu.title_id, text=self.gui.language_text[self.gui.language]['title'])

        #update recognition_menu
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.first_name_text_id,
                                                 text=self.gui.language_text[self.gui.language]['name'])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.last_name_text_id,
                                                 text=self.gui.language_text[self.gui.language]['last_name'])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.id_label_text_id,
                                                 text=self.gui.language_text[self.gui.language]['student_number'])
        self.gui.registration_menu.itemconfigure(self.gui.registration_menu.error_message_id,
                                                 text=self.gui.language_text[self.gui.language]['error_message'])


        #update registration_menu


