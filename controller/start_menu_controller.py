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


