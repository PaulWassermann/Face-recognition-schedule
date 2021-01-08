# The controller for the recognition menu


class RecognitionMenuController:

    def __init__(self, gui):
        self.gui = gui

    # Triggered when the return button on the recognition menu is clicked, returns to start menu
    def return_button_command(self):

        # Closing the cam
        if not self.gui.recognition_menu.done.get():
            self.gui.recognition_menu.done.set(value=True)

        self.gui.recognition_menu.hide()
        self.gui.start_menu.display()
