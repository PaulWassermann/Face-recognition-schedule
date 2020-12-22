class StartMenuController:

    def __init__(self, gui):
        self.gui = gui

    def registration_button_command(self):
        self.gui.start_menu.hide()
        self.gui.registration_menu.display()

    def recognition_button_command(self):
        self.gui.start_menu.hide()
        self.gui.recognition_menu.display()

    def change_language(self):

        if self.gui.language == 'en':
            self.gui.language = 'es'
        elif self.gui.language == 'es':
            self.gui.language = 'fr'
        elif self.gui.language == 'fr':
            self.gui.language = 'en'

        gui.root.update()
        print(self.gui.language)


    def language_select(self, language):
        return(language)