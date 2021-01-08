from controller.registration_menu_controller import RegistrationMenuController
from face_recognition import face_locations, face_encodings, compare_faces
from view.round_button import RoundButton
from model.student import Student
from PIL import ImageTk
from time import time
from tkinter import *
import cv2
import PIL


class RegistrationMenu(Canvas):

    def __init__(self, gui):

        self.gui = gui

        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        # Initializing the controller
        self.controller = RegistrationMenuController(self.gui)

        # Attributes for user input
        self.last_name = StringVar()
        self.first_name = StringVar()
        self.id = StringVar()

        self.background_id = self.create_image(0, 0, image=self.gui.global_background_image, anchor="nw")
        self.cm_logo_id = self.create_image(5, 5, image=self.gui.global_cm_logo_image, anchor="nw")

        # Text indications
        self.id_label_text = self.create_text(0.25 * self.gui.width, 0.3 * self.gui.height,
                                              text=self.gui.text_resources[self.gui.language]['student_number'],
                                              font=('helvetica', 28), anchor="nw")
        self.first_name_text = self.create_text(0.25 * self.gui.width, 0.4 * self.gui.height,
                                                text=self.gui.text_resources[self.gui.language]['name'],
                                                font=('helvetica', 28), anchor="nw")
        self.last_name_text = self.create_text(0.25 * self.gui.width, 0.5 * self.gui.height,
                                               text=self.gui.text_resources[self.gui.language]['last_name'],
                                               font=('helvetica', 28), anchor="nw")

        self.student_number_error_message = self.create_text(0.4 * self.gui.width, 0.35 * self.gui.height,
                                                             text=self.gui.text_resources[self.gui.language][
                                                                    "student_number_error_message"],
                                                             font=("Helvetica", 14),
                                                             fill="red", anchor="nw", state="hidden")

        self.required_field_error_message_1 = self.create_text(0.4 * self.gui.width, 0.45 * self.gui.height,
                                                               text=self.gui.text_resources[self.gui.language][
                                                                   "required_field_error_message"],
                                                               font=("Helvetica", 14),
                                                               fill="red", anchor="nw", state="hidden")

        self.required_field_error_message_2 = self.create_text(0.4 * self.gui.width, 0.55 * self.gui.height,
                                                               text=self.gui.text_resources[self.gui.language][
                                                                   "required_field_error_message"],
                                                               font=("Helvetica", 14),
                                                               fill="red", anchor="nw", state="hidden")

        # Entries
        self.id_entry = Entry(self, textvariable=self.id, font=('helvetica', 24), width=10)
        self.first_name_entry = Entry(self, textvariable=self.first_name, font=('helvetica', 24), width=30)
        self.last_name_entry = Entry(self, textvariable=self.last_name, font=('helvetica', 24), width=30)

        self.id_entry.bind("<FocusOut>",
                           lambda e: self.itemconfigure(self.student_number_error_message, state="normal")
                           if len(self.id_entry.get()) != 8 and len(self.id_entry.get()) > 0 else
                           (self.itemconfigure(self.student_number_error_message, state="hidden") if
                            self.itemcget(self.student_number_error_message, "state") == "normal" else None))

        self.first_name_entry.bind("<FocusOut>",
                                   lambda e: self.itemconfigure(self.required_field_error_message_1, state="normal")
                                   if len(self.id_entry.get()) == 0 else
                                   (self.itemconfigure(self.required_field_error_message_1, state="hidden") if
                                    self.itemcget(self.required_field_error_message_1, "state") == "normal" else None))

        self.last_name_entry.bind("<FocusOut>",
                                  lambda e: self.itemconfigure(self.required_field_error_message_2, state="normal")
                                  if len(self.id_entry.get()) == 0 else
                                  (self.itemconfigure(self.required_field_error_message_2, state="hidden") if
                                   self.itemcget(self.required_field_error_message_2, "state") == "normal" else None))

        # Placing the entries on the canvas
        self.id_entry.place(x=0.4 * self.gui.width, y=0.3 * self.gui.height)
        self.first_name_entry.place(x=0.4 * self.gui.width, y=0.4 * self.gui.height)
        self.last_name_entry.place(x=0.4 * self.gui.width, y=0.5 * self.gui.height)

        # Validation Button
        self.validation_button = Button(self, text="Valider", font=('helvetica', 24),
                                        fg="green", bg="white",
                                        activeforeground="green", activebackground="white",
                                        relief="flat",
                                        state="disabled",
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

        self.video_back_frame = Frame(self, bg='white')
        self.video_back_canvas = Canvas(self.video_back_frame, width=int(0.7 * self.gui.width), height=self.gui.height,
                                        border=0, highlightthickness=0)
        self.video_back_canvas.pack(expand='yes')
        self.video_back_id = self.video_back_canvas.create_image(0,
                                                                 0,
                                                                 image=None,
                                                                 anchor="nw")

        self.set_timer = False
        self.id_after_timer_2 = 0
        self.id_after_timer_1 = 0
        self.id_after_timer_0 = 0
        self.timer_text = self.video_back_canvas.create_text(int(0.35 * self.gui.width),
                                                             int(0.9 * self.gui.height),
                                                             text=" ")
        self.done = BooleanVar(value=False)

    def enable_validation_button(self):

        if len(self.id_entry.get()) == 8 \
                and len(self.first_name_entry.get()) > 0 \
                and len(self.last_name_entry.get()) > 0:
            self.validation_button["state"] = "active"

        else:
            self.validation_button["state"] = "disabled"

    def registration(self):

        locations = []
        encodings = []

        # Creating an instance of Student class to dump the user entries in the database when the face encoding is set
        student_to_register = Student(self.gui, self.id.get(), self.first_name.get(), self.last_name.get())

        temporary_encoding = None
        student_face_is_detected = False

        # Linking to the computer camera
        vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.done.set(value=False)

        self.video_back_frame.place(x=0.15 * self.gui.width, y=0)

        last_calculation = 0
        start = time()

        self.set_timer = False

        while not self.done.get():

            # Getting the last frame captured by the camera
            _, frame = vc.read()

            # Mirroring the frame for a better video back
            frame = cv2.flip(frame, 1)

            # Processing where the faces are on the frame
            if time() - last_calculation >= 0.5:
                encodings = face_encodings(frame)
                locations = face_locations(frame)
                last_calculation = time()
                student_face_is_detected = False

            if len(encodings) > 0:

                if temporary_encoding is None:
                    temporary_encoding = list(encodings[0])

                elif temporary_encoding is not None:

                    for (top, right, bottom, left), face_encoding in zip(locations, encodings):
                        matches = compare_faces([temporary_encoding], face_encoding)

                        if matches[0]:

                            student_face_is_detected = True

                            # Drawing a green rectangle around the face of the student
                            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))

                            if time() - start > 3:

                                if not self.set_timer:
                                    self.video_back_canvas.itemconfigure(self.timer_text,
                                                                         text="3",
                                                                         font=('helvetica', 70),
                                                                         fill="#00ff00",
                                                                         anchor="center")

                                    self.id_after_timer_2 = self.gui.root.after(1000,
                                                                                lambda:
                                                                                [self.video_back_canvas.itemconfigure(
                                                                                    self.timer_text,
                                                                                    text="2",
                                                                                    font=('helvetica', 70),
                                                                                    fill="#00ff00",
                                                                                    anchor="center"),
                                                                                    self.reset_timer_2()])

                                    self.id_after_timer_1 = self.gui.root.after(2500,
                                                                                lambda:
                                                                                [self.video_back_canvas.itemconfigure(
                                                                                    self.timer_text,
                                                                                    text="1",
                                                                                    font=('helvetica', 70),
                                                                                    fill="#00ff00",
                                                                                    anchor="center"),
                                                                                    self.reset_timer_1()])

                                    self.id_after_timer_0 = self.gui.root.after(
                                        4000,
                                        lambda: [self.video_back_canvas.itemconfigure(self.timer_text,
                                                                                      text=" "),
                                                 self.reset_timer_0(),
                                                 student_to_register.set_face_encoding(encoding=temporary_encoding),
                                                 self.gui.root.after(1000, self.done.set(value=True))])

                                    self.set_timer = True

                    if not student_face_is_detected:
                        self.cancel_timer()

            elif len(encodings) == 0:

                if self.set_timer:
                    self.cancel_timer()

            # Resizing the video back to fit our canvas
            frame = cv2.resize(frame, (int(0.7 * self.gui.width), self.gui.height), interpolation=cv2.INTER_AREA)

            # Somehow the pixels are stored as BGR so we have to arrange them as RGB
            frame = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame[..., ::-1]))
            self.video_back_canvas.itemconfigure(self.video_back_id, image=frame)

            self.gui.root.update()

        student_to_register.dump_info()
        self.video_back_frame.place_forget()
        self.hide()
        self.gui.start_menu.display()

    def reset_timer_2(self):
        self.id_after_timer_2 = 0

    def reset_timer_1(self):
        self.id_after_timer_1 = 0

    def reset_timer_0(self):
        self.id_after_timer_0 = 0

    def cancel_timer(self):

        self.set_timer = False
        self.video_back_canvas.itemconfigure(self.timer_text, text=" ")

        if self.id_after_timer_2 != 0:
            self.gui.root.after_cancel(self.id_after_timer_2)
            self.reset_timer_2()

        if self.id_after_timer_1 != 0:
            self.gui.root.after_cancel(self.id_after_timer_1)
            self.reset_timer_1()

        if self.id_after_timer_0 != 0:
            self.gui.root.after_cancel(self.id_after_timer_0)
            self.reset_timer_0()

    def display(self):

        self.bind("<Button-1>", lambda e: self.focus_set())
        self.gui.root.bind_class("Entry", "<FocusIn>", lambda e: self.gui.touch_keyboard.display(e))
        self.gui.root.bind_class("Entry", "<FocusOut>", lambda e: [self.gui.touch_keyboard.hide(),
                                                                   self.enable_validation_button()])

        # Packing the canvas onto the root window
        self.pack(expand='yes')

    def hide(self):

        self.unbind("<Button-1>")
        self.gui.root.unbind_class("Entry", "<FocusIn>")
        self.gui.root.unbind_class("Entry", "<FocusOut>")
        self.pack_forget()
