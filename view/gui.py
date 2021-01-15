from view.database_visualisation import DatabaseVisualisation
from view.administrator_log_in import AdministratorLogIn
from view.language_selection import LanguageSelection
from view.registration_menu import RegistrationMenu
from view.recognition_menu import RecognitionMenu
from view.resizable_image import ResizableImage
from view.parameters_menu import ParametersMenu
from view.touch_keyboard import TouchKeyboard
from view.start_menu import StartMenu
from model.log import Log
from tkinter import *
import json


# The gui model holds the attributes related to the application in general
class GUI:

    def __init__(self):

        # This line creates the window used to display the application
        self.root = Tk()

        # We define the size of the app window relatively to the size of the screen that will display it
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.width = self.screen_width
        self.height = self.screen_height

        # Setting the title and the size of the window
        self.root.title("Face recognition")
        self.root.geometry(f"{self.width}x{self.height}+{int((self.screen_width - self.width) / 2)}+"
                           + f"{int((self.screen_height - self.height) / 2)}")

        # Disabling the resizable option as well as the top border
        self.root.resizable(width=False, height=False)
        self.root.overrideredirect(boolean=True)  # set to False while debugging

        # Loading students database as a dictionary
        self.database = {}
        self.load_database()

        # Loading admins database as a dictionary
        self.admins = {}
        self.load_admins()

        # Loading text as a dictionary
        self.language = "french"
        self.text_resources = {
            "french": {
                "last_name": "Nom",
                "name": "Pr\u00e9nom",
                "recognition_button": "Consulter mon EDT\n(Je suis d\u00e9j\u00e0 enregistr\u00e9)",
                "registration_button": "M'enregistrer",
                "required_field_error_message": "Champ requis",
                "student_number": "N\u00b0Etudiant",
                "student_number_error_message": "L'identifiant doit contenir 8 chiffres",
                "title": "Mon Emploi du Temps"
            },
            "english": {
                "last_name": "Last Name",
                "name": "Name",
                "recognition_button": "Consult my schedule\n(I'm already registered)",
                "registration_button": "Register",
                "required_field_error_message": "Required field",
                "student_number": "Student N\u00b0",
                "student_number_error_message": "ID must have 8 numbers",
                "title": "My Schedule"
            },
            "spanish": {
                "last_name": "Apellido",
                "name": "Nombre",
                "recognition_button": "Consultar mi calendario\n(Ya estoy registrado)",
                "registration_button": "Registrarme",
                "required_field_error_message": "Campo obligatorio",
                "student_number": "N\u00b0Estudiante",
                "student_number_error_message": "El identificador debe contener 8 cifras",
                "title": "Mi calendario"
            }
        }

        # Loading assets
        self.background_image = None
        self.global_background_image = None
        self.cm_logo_image = None
        self.global_cm_logo_image = None
        self.registration_button_image = None
        self.registration_button_on_click_image = None
        self.schedule_button_image = None
        self.schedule_button_on_click_image = None
        self.parameters_button = None
        self.parameters_button_on_click = None
        self.return_button_image = None
        self.return_button_on_click_image = None
        self.modify_text_button_image = None
        self.validate_modification_button_image = None
        self.cancel_modification_button_image = None
        self.language_assets = {}

        self.load_assets()

        # Menus
        self.start_menu = StartMenu(self)
        self.registration_menu = RegistrationMenu(self)
        self.recognition_menu = RecognitionMenu(self)
        self.parameters_menu = ParametersMenu(self)
        self.language_selection = LanguageSelection(self)
        self.database_visualisation = DatabaseVisualisation(self)
        self.administrator_log_in = AdministratorLogIn(self)

        # Tactile Keyboard
        self.touch_keyboard = TouchKeyboard(self)

        # Application Bindings
        self.root.bind_all("<Escape>", lambda e: self.close_app)

        # Protocols
        self.root.protocol('WM_DELETE_WINDOW', self.close_app)

    # Loading the file containing the users' info
    def load_database(self):

        try:

            with open("files/students.txt", 'r') as file:
                self.database = json.load(file)

        except:
            Log().write_log_exception(level="error", message="An error occurred while loading the students database.",
                                      show=True, log=True)

    def load_admins(self):

        try:

            with open("files/administrators.txt", 'r') as file:
                self.admins = json.load(file)

        except:
            Log().write_log_exception(level="error",
                                      message="An error occurred while loading the administrators database.",
                                      show=True, log=True)

    # Loading the assets as resizable images using our custom class to adjust their size to the screen
    def load_assets(self):

        try:
            self.background_image = ResizableImage(path_to_image="assets/background.png")
            self.global_background_image = self.background_image.resize_to_tk(width=self.width,
                                                                              height=self.height)
            self.cm_logo_image = ResizableImage(path_to_image="assets/cm_logo.png")
            self.global_cm_logo_image = self.cm_logo_image.resize_to_tk(width=0.2 * self.width)
            self.registration_button_image = ResizableImage(path_to_image="assets/registration_button.png")
            self.registration_button_on_click_image = ResizableImage(
                path_to_image="assets/registration_button_on_click.png")
            self.schedule_button_image = ResizableImage(path_to_image="assets/schedule_button.png")
            self.schedule_button_on_click_image = ResizableImage(path_to_image="assets/schedule_button_on_click.png")
            self.parameters_button = ResizableImage(path_to_image="assets/parameters_button.png")
            self.parameters_button_on_click = ResizableImage(path_to_image="assets/parameters_button_on_click.png")
            self.return_button_image = ResizableImage(path_to_image="assets/return_button.png")
            self.return_button_on_click_image = ResizableImage(path_to_image="assets/return_button_on_click.png")
            self.modify_text_button_image = ResizableImage(path_to_image="assets/modify_text.png")
            self.validate_modification_button_image = ResizableImage(
                path_to_image="assets/validate_modification_button.png")
            self.cancel_modification_button_image = ResizableImage(
                path_to_image="assets/cancel_modification_button.png")

            for language in self.text_resources.keys():
                self.language_assets[language] = [
                    ResizableImage(path_to_image=f"assets/{language}_button.png"),
                    ResizableImage(path_to_image=f"assets/{language}_button_on_click.png")]

        except:
            Log().write_log_exception(level="error", message="Une erreur est survenue lors du chargement des éléments "
                                                             "visuels.",
                                      show=True, log=True)

    def close_app(self):

        try:

            with open("files/students.txt", 'w') as file:
                json.dump(self.database, file, sort_keys=True, indent=4)

            with open("files/administrators.txt", 'w') as file:
                json.dump(self.admins, file, sort_keys=True, indent=4)

        except:
            Log().write_log_exception(level="error", message="The application didn't close properly.",
                                      show=False, log=True)

        finally:
            self.root.quit()
