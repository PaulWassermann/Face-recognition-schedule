class ParametersMenuController:

    def __init__(self, gui):
        self.gui = gui

    def quit_button_command(self):
        self.gui.close_app()

    def return_button_command(self):
        self.gui.parameters_menu.hide()
        self.gui.start_menu.display()
