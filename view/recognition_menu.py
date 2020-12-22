from controller.recognition_menu_controller import RecognitionMenuController
from face_recognition import face_locations, face_encodings, compare_faces
from model.round_button import RoundButton
from model.student import Student
from PIL import ImageTk
from time import time
from tkinter import *
import cv2
import PIL


class RecognitionMenu(Canvas):

    def __init__(self, gui):

        self.gui = gui
        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        # Initializing the controller
        self.controller = RecognitionMenuController(self.gui)

        self.background = self.gui.background_resizable_image.resize_to_tk(width=int(0.3 * self.gui.width),
                                                                           height=self.gui.height)

        self.background_id = self.create_image(0, 0,
                                               image=self.background,
                                               anchor="nw")

        # self.title_label = Label(self, text="Mon emploi du temps du jour:", font=('Helvetica', 16), bg="white")
        # self.title_label.place(x=0, y=0)

        self.video_back_id = self.create_image(0.3 * self.gui.width,
                                               0,
                                               image=None,
                                               anchor="nw")

        self.fps = 0
        self.fps_id = self.create_text(0.31 * self.gui.width, 0.01 * self.gui.height,
                                       text="FPS: 0", font=('Helvetica', 16), fill="green", anchor="nw")

        self.return_button = RoundButton(canvas=self,
                                         gui=self.gui,
                                         x=0.95 * self.gui.width,
                                         y=0.08 * self.gui.height,
                                         radius=40,
                                         image=self.gui.return_button_image,
                                         image_on_click=self.gui.return_button_on_click_image,
                                         command=self.controller.return_button_command)

        self.student = None
        self.got_schedule = False

        self.done = BooleanVar(value=False)

    def recognition(self):

        locations = []
        encodings = []

        last_calculation = 0

        # Linking to the computer camera
        vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.done.set(value=False)

        while not self.done.get():

            start = time()

            # Getting the last frame captured by the camera
            _, frame = vc.read()

            # Mirroring the frame for a better video back
            frame = cv2.flip(frame, 1)

            # Recalculating faces locations & encodings every 2 seconds
            if time() - last_calculation >= 2:
                encodings = face_encodings(frame)
                locations = face_locations(frame)
                last_calculation = time()

            for (top, right, bottom, left), face_encoding in zip(locations, encodings):

                matches = compare_faces([self.gui.database[key][2] for key in self.gui.database], face_encoding)

                if True in matches:
                    keys = list(self.gui.database.keys())
                    first_match_index = matches.index(True)

                    student = Student(self.gui, id_=keys[first_match_index],
                                      first_name=self.gui.database[keys[first_match_index]][0],
                                      last_name=self.gui.database[keys[first_match_index]][1])

                    if self.student is None or student != self.student:
                        self.student = student

                        # if not self.got_schedule:
                        #     self.got_schedule = self.student.get_schedule()

                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))
                    cv2.putText(img=frame, text=self.student.get_last_name(), org=(left, top - 10),
                                fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1,
                                color=(0, 255, 0))

                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))
                    cv2.putText(img=frame, text="Unknown", org=(left, top - 10), fontFace=cv2.FONT_HERSHEY_COMPLEX,
                                fontScale=1, color=(0, 255, 0))

            frame = cv2.resize(frame, (int(0.7 * self.gui.width), self.gui.height), interpolation=cv2.INTER_AREA)

            # Somehow the pixels are stored as BGR so we have to arrange them as RGB
            frame = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame[..., ::-1]))
            self.itemconfigure(self.video_back_id, image=frame)
            self.update_idletasks()

            if (time() - last_calculation) < 1:
                self.fps = round(1 / (time() - start))
                self.itemconfigure(self.fps_id, text=f"FPS: {self.fps}")

            self.gui.root.update()

        self.hide()

    def display(self):
        self.pack(expand="yes")
        self.recognition()

    def hide(self):
        self.pack_forget()
        self.gui.start_menu.display()
