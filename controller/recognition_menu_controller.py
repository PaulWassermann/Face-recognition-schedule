class RecognitionMenuController:

    def __init__(self, gui):
        self.gui = gui

    def return_button_command(self):

        if not self.gui.recognition_menu.done.get():
            self.gui.recognition_menu.done.set(value=True)

        self.gui.recognition_menu.hide()
        self.gui.start_menu.display()
