class DatabaseVisualisationController:

    def __init__(self, gui):
        self.gui = gui

    def return_button_command(self):
        self.gui.database_visualisation.hide()
        self.gui.parameters_menu.display()
