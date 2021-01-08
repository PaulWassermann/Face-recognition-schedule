# The controller for the start menu


class StartMenuController:

    def __init__(self, gui):
        self.gui = gui

    # Displays the registration menu
    def registration_button_command(self):
        self.gui.start_menu.hide()
        self.gui.registration_menu.display()

    # Displays the recognition menu
    def recognition_button_command(self):
        self.gui.start_menu.hide()
        self.gui.recognition_menu.display()

    # Displays the adminsitrator log in page
    def parameters_button_command(self):
        self.gui.start_menu.hide()
        self.gui.administrator_log_in.display()

    # Displays the language selection pop-up menu
    def language_selection_button_command(self):
        self.gui.language_selection.display()
