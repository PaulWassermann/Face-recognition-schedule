class StartMenuController:

    def __init__(self, gui):
        self.gui = gui

    def registration_button_command(self):
        """ Go to registration_menu"""
        self.gui.start_menu.hide()
        self.gui.registration_menu.display()

    def recognition_button_command(self):
        """Go to recognition menu"""
        self.gui.start_menu.hide()
        self.gui.recognition_menu.display()

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
        self.gui.start_menu.registration_button.update_text(self.gui.language_text[self.gui.language]['registration_button'])
        self.gui.start_menu.recognition_button.update_text(self.gui.language_text[self.gui.language]['recognition_button'])
        self.gui.start_menu.itemconfigure(self.gui.start_menu.title_id, text=self.gui.language_text[self.gui.language]['title'])

        # self.gui.start_menu.itemconfigure(self.gui.start_menu.language_button, self.gui.french_button_image)
