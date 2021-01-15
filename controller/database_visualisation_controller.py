class DatabaseVisualisationController:

    def __init__(self, gui):
        self.gui = gui

    def return_button_command(self):

        if self.gui.database_visualisation.active_modification_line is not None:
            self.gui.database_visualisation.modify_data(self.gui.database_visualisation.active_modification_line)

        self.gui.database_visualisation.hide()
        self.gui.parameters_menu.display()
