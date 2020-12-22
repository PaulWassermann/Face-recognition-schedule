from view.registration_menu import RegistrationMenu
from model.touch_keyboard import TouchKeyboard
from view.recognition_menu import RecognitionMenu
from model.resizable_image import ResizableImage
from view.start_menu import StartMenu
from controller.language_controller import LanguageController
from tkinter import *
import json


class GUI:
    '''The gui model holds the attributes related to the application in general'''

    def __init__(self):

        self.root = Tk()

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.width = 4 * self.screen_width // 5
        self.height = 4 * self.screen_height // 5

        self.root.title("Face recognition")
        self.root.geometry(f'{self.width}x{self.height}+{int((self.root.winfo_screenwidth() - self.width) / 2)}+'
                           + f'{- 50 + int((self.root.winfo_screenheight() - self.height) / 2)}')
        self.root.resizable(width=False, height=False)
        self.root.overrideredirect(boolean=False) # False while debugging
        self.root.config(bg='white')

        # Loading database
        self.database = {}
        self.load_database()

        #Loading text
        self.language_text = {}
        self.load_language()
        self.language = 'fr'

        # Loading assets
        self.background_resizable_image = None
        self.background_image = None
        self.cm_logo_image = None
        self.registration_button_image = None
        self.registration_button_on_click_image = None
        self.schedule_button_image = None
        self.schedule_button_on_click_image = None
        self.french_button_image = None
        self.french_button_on_click_image = None
        self.return_button_image = None
        self.return_button_on_click_image = None

        self.load_assets()

        # Menus
        self.start_menu = StartMenu(self)
        self.registration_menu = RegistrationMenu(self)
        self.recognition_menu = RecognitionMenu(self)

        # Tactile Keyboard
        self.tactile_keyboard = TouchKeyboard(self)

        # Application Bindings
        self.root.bind_all("<Escape>", lambda e: self.root.quit())

    #Face registered's data
    def load_database(self):
        """"Load face database"""
        try:
            with open("Database.txt", 'r') as file:
                self.database = json.load(file)
        except:
            print("An error occurred while loading the database.")

    #Text for each language

    def load_language(self):
        """"Load different text"""
        try:
            with open("language.txt", 'r') as file:

                self.language_text = json.load(file)
        except:
            print("An error occurred while loading the language_text.")


    #Icons's loading
    def load_assets(self):
        """Load assets"""
        self.background_resizable_image = ResizableImage(path_to_image="assets/background.png")
        self.background_image = self.background_resizable_image.resize_to_tk(width=(1228 ** 2) // self.width,
                                                                             height=(691 ** 2) // self.height)

        self.cm_logo_image = PhotoImage(file="assets/cm_logo.png")
        self.registration_button_image = PhotoImage(file="assets/registration_button.png")
        self.registration_button_on_click_image = PhotoImage(file="assets/registration_button_on_click.png")
        self.schedule_button_image = PhotoImage(file="assets/schedule_button.png")
        self.schedule_button_on_click_image = PhotoImage(file="assets/schedule_button_on_click.png")
        self.french_button_image = PhotoImage(file="assets/french_button.png")
        self.french_button_on_click_image = PhotoImage(file="assets/french_button_on_click.png")
        self.return_button_image = PhotoImage(file="assets/return_button.png")
        self.return_button_on_click_image = PhotoImage(file="assets/return_button_on_click.png")

