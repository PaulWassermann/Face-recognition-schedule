from controller.registration_menu_controller import RegistrationMenuController
from face_recognition import face_locations
from model.round_button import RoundButton
from model.student import Student
from time import time
from tkinter import *
import cv2


class RegistrationMenu(Canvas):

    def __init__(self, gui):

        self.gui = gui

        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        # Initializing the controller
        self.controller = RegistrationMenuController(self.gui)

        self.background_id = self.create_image(0, 0,
                                               image=self.gui.background_image,
                                               anchor="nw")

        # Attributes for user input
        self.last_name = StringVar()
        self.first_name = StringVar()
        self.id = StringVar()

        self.background_id = self.create_image(0, 0, image=self.gui.background_image, anchor="nw")

        self.cm_logo_id = self.create_image(5, 5, image=self.gui.cm_logo_image, anchor="nw")

        # Text indications
        self.id_label_text_id = self.create_text(0.25 * self.gui.width, 0.3 * self.gui.height,
                                                 text=gui.language_text[gui.language]['student_number'], font=('helvetica', 24), anchor="nw")
        self.first_name_text_id = self.create_text(0.25 * self.gui.width, 0.4 * self.gui.height,
                                                   text=gui.language_text[gui.language]['name'], font=('helvetica', 24), anchor="nw")
        self.last_name_text_id = self.create_text(0.25 * self.gui.width, 0.5 * self.gui.height,
                                                  text=gui.language_text[gui.language]['last_name'], font=('helvetica', 24), anchor="nw")

        self.error_message_id = self.create_text(0.4 * self.gui.width, 0.35 * self.gui.height,
                                                 text="L'identifiant doit contenir 8 chiffres",
                                                 font=("Helvetica", 10),
                                                 fill="red", anchor="nw")
        self.itemconfigure(self.error_message_id, state="hidden")

        # Entries
        self.id_entry = Entry(self, textvariable=self.id, font=('helvetica', 20), width=10)
        self.first_name_entry = Entry(self, textvariable=self.first_name, font=('helvetica', 20), width=30)
        self.last_name_entry = Entry(self, textvariable=self.last_name, font=('helvetica', 20), width=30)

        self.id_entry.bind("<FocusOut>", lambda e: self.itemconfigure(self.error_message_id, state="normal")
        if len(self.id_entry.get()) != 8 else
        (self.itemconfigure(self.error_message_id, state="hidden") if
         self.itemcget(self.error_message_id, "state") == "normal" else None))

        # Placing the entries on the canvas
        self.id_entry.place(x=0.4 * self.gui.width, y=0.3 * self.gui.height)
        self.first_name_entry.place(x=0.4 * self.gui.width, y=0.4 * self.gui.height)
        self.last_name_entry.place(x=0.4 * self.gui.width, y=0.5 * self.gui.height)

        # Validation Button
        self.validation_button = Button(self, text="Valider", font=('helvetica', 20),
                                        fg="green", bg="white",
                                        activeforeground="green", activebackground="white",
                                        relief="flat",
                                        takefocus=False,
                                        command=self.registration)
        self.validation_button.place(x=0.5 * self.gui.width, y=0.75 * self.gui.height, anchor="center")

        # Return Button
        self.return_button = RoundButton(canvas=self,
                                         gui=self.gui,
                                         x=0.95 * self.gui.width,
                                         y=0.08 * self.gui.height,
                                         radius=40,
                                         image=self.gui.return_button_image,
                                         image_on_click=self.gui.return_button_on_click_image,
                                         command=self.controller.return_button_command)

        self.done = BooleanVar(value=False)

        #Entries
        self.id_entry = Entry(self, textvariable=self.id, justify=CENTER, font=('helvetica', 20))
        self.first_name_entry = Entry(self, textvariable=self.first_name, justify=CENTER, font=('helvetica', 20))
        self.last_name_entry = Entry(self, textvariable=self.last_name, justify=CENTER, font=('helvetica', 20))

    def registration(self):

        # Creating instance of student to then dump the user entries in the database
        student = Student(self.gui, self.id.get(), self.first_name.get(), self.last_name.get())

        # Linking to the computer camera
        vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.done = BooleanVar(value=False)

        last_calculation = 0
        start = time()

        while not self.done.get():

            # Getting the last frame captured by the camera
            _, frame = vc.read()

            # Mirroring the frame for a better video back
            frame = cv2.flip(frame, 1)

            # Processing where the faces are on the frame
            locations = face_locations(frame)

            are_faces_detected = False

            for (top, right, bottom, left) in locations:

                # Drawing green rectangles around the faces detected
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))

                # Faces have been detected
                if len(locations) > 0 and time() - start > 3:
                    are_faces_detected = True

            # Showing video back in a new cv2 window
            cv2.imshow("frame", frame)

            # Launching function to take a picture if a face have been detected
            # self.take_photo(are_faces_detected)

            # Terminating the video capture
            # if cv2.waitKey(1) and are_faces_detected:
            if self.done.get() and are_faces_detected:
                vc.release()
                cv2.destroyAllWindows()
                break

        # student.set_face_encoding(frame)
        # student.dump_infos('Database.txt')
        # self.hide()
        # self.gui.start_menu.display()

    def take_photo(self, boolean):
        if boolean:
            pass

    def display(self):

        self.bind("<Button-1>", lambda e: self.focus_set())
        self.gui.root.bind_class("Entry", "<FocusIn>", lambda e: [self.gui.tactile_keyboard.display(e),
                                                                  self.validation_button.place_forget()])
        self.gui.root.bind_class("Entry", "<FocusOut>", lambda e: [self.gui.tactile_keyboard.hide(),
                                                                   self.validation_button.place(x=0.5 * self.gui.width,
                                                                                                y=0.75 * self.gui.height,
                                                                                                anchor="center")])

        # Packing the canvas onto the root window

        self.pack(expand='yes')

    def hide(self):

        self.unbind("<Button-1>")
        self.gui.root.unbind_class("Entry", "<FocusIn>")
        self.gui.root.unbind_class("Entry", "<FocusOut>")
        self.pack_forget()
