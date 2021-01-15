from controller.database_visualisation_controller import DatabaseVisualisationController
from view.round_button import RoundButton
from model.log import Log
from tkinter import *


class DatabaseVisualisation(Canvas):

    def __init__(self, gui):
        self.gui = gui
        super().__init__(self.gui.root, width=self.gui.width, height=self.gui.height, border=0, highlightthickness=0)

        self.width = int(0.68 * self.gui.width)
        self.height = int(0.7 * self.gui.height)

        # Initializing the controller
        self.controller = DatabaseVisualisationController(self.gui)

        self.background_id = self.create_image(0, 0, image=self.gui.global_background_image, anchor="nw")
        self.cm_logo_id = self.create_image(5, 5, image=self.gui.global_cm_logo_image, anchor="nw")
        self.modify_text_button_image = self.gui.modify_text_button_image.resize_to_tk(width=int(0.05 * self.width))
        self.validate_modification_button_image = self.gui.validate_modification_button_image.resize_to_tk(
            width=int(0.05 * self.width))
        self.cancel_modification_button_image = self.gui.cancel_modification_button_image.resize_to_tk(
            width=int(0.05 * self.width))

        self.frame = Frame(self, bg="white", width=self.width, height=self.height)

        self.canvas = Canvas(self.frame, bg="white", width=self.width, height=self.height, highlightthickness=0)

        self.scrollbar = Scrollbar(self.frame, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.inside_frame = Frame(self.canvas, bg="white", width=self.width, height=self.height)
        self.canvas.create_window((int(self.canvas.cget("width")) / 2, 0), window=self.inside_frame, anchor=N)
        self.frame.place(x=int(0.5 * self.gui.width), y=int(0.55 * self.gui.height), anchor="center")
        self.canvas.pack()

        self.last_name_text = self.create_text(0.27 * self.gui.width, 0.15 * self.gui.height,
                                               text="Nom de famille", font=("Helvetica", 24), fill="green",
                                               anchor="center")
        self.first_name_text = self.create_text(0.46 * self.gui.width, 0.15 * self.gui.height,
                                                text="Prénom", font=("Helvetica", 24), fill="green",
                                                anchor="center")
        self.id_text = self.create_text(0.70 * self.gui.width, 0.15 * self.gui.height,
                                        text="Identifiant", font=("Helvetica", 24), fill="green",
                                        anchor="center")

        self.canvas_dict = {}
        self.text_dict = {}
        self.button_dict = {}

        self.init_database_view()

        self.active_modification_line = None

        # Return Button
        self.return_button = RoundButton(canvas=self,
                                         gui=self.gui,
                                         x=0.95 * self.gui.width,
                                         y=0.08 * self.gui.height,
                                         radius=40,
                                         image=self.gui.return_button_image,
                                         image_on_click=self.gui.return_button_on_click_image,
                                         command=self.controller.return_button_command)

    def create_line(self, id_, first_name, last_name):

        self.canvas_dict[id_] = [Canvas(self.inside_frame, width=self.width, bg="white", border=0,
                                        highlightthickness=0, relief="sunken"),
                                 last_name]

        self.text_dict[id_] = [Text(self.canvas_dict[id_][0], font=('helvetica', 22), width=20, height=1, wrap="word",
                                    undo=True, highlightthickness=0, highlightcolor="white"),
                               Text(self.canvas_dict[id_][0], font=('helvetica', 22), width=20, height=1, wrap="word",
                                    undo=True, highlightthickness=0, highlightcolor="white"),
                               Text(self.canvas_dict[id_][0], font=('helvetica', 22), width=9, height=1, wrap="word",
                                    undo=True, highlightthickness=0, highlightcolor="white")]

        for index, elem in enumerate([last_name, first_name, id_]):
            self.text_dict[id_][index]["height"] = 1 + (len(elem) // (1 + int(self.text_dict[id_][index]["width"])))
            self.text_dict[id_][index].insert("insert", elem)
            self.text_dict[id_][index]["state"] = "disabled"

            self.text_dict[id_][index].pack(side="left", padx=10, pady=5)

        self.button_dict[id_] = [Button(self.canvas_dict[id_][0], image=self.modify_text_button_image,
                                        anchor="center", bg="white", activebackground="white", relief="flat",
                                        command=lambda param=id_: self.modify_data(param)),
                                 Button(self.canvas_dict[id_][0], image=self.validate_modification_button_image,
                                        anchor="center", bg="white", activebackground="white", relief="flat",
                                        command=self.validate_modification),
                                 Button(self.canvas_dict[id_][0], image=self.cancel_modification_button_image,
                                        anchor="center", bg="white", activebackground="white", relief="flat",
                                        command=self.cancel_modification)]

        self.button_dict[id_][0].pack(side="left", padx=10)

    def modify_data(self, id_):

        if id_ != self.active_modification_line:

            if self.active_modification_line is not None:
                for elem in self.text_dict[self.active_modification_line]:
                    elem["state"] = "disabled"

                self.button_dict[self.active_modification_line][1].pack_forget()
                self.button_dict[self.active_modification_line][2].pack_forget()

            self.active_modification_line = id_
            self.button_dict[id_][1].pack(side="left")
            self.button_dict[id_][2].pack(side="left")
            for elem in self.text_dict[id_]:
                elem["state"] = "normal"
                elem.edit_separator()
                elem.edit_modified(False)

        elif id_ == self.active_modification_line:

            for elem in self.text_dict[id_]:
                try:
                    if elem.edit_modified():
                        elem.edit_undo()
                except:
                    pass

                finally:
                    elem.edit_modified(False)
                    elem.edit_reset()

                elem["state"] = "disabled"

            self.button_dict[id_][1].pack_forget()
            self.button_dict[id_][2].pack_forget()
            self.active_modification_line = None

        self.canvas.focus_set()

    def validate_modification(self):

        id_text = self.text_dict[self.active_modification_line][2].get("1.0", "end").strip("\n")

        if id_text != self.active_modification_line:
            old_id = self.active_modification_line
            new_id = self.text_dict[old_id][2].get("1.0", "end")
            self.gui.database[new_id] = self.gui.database[old_id]
            self.gui.database.pop(old_id)
            self.canvas_dict[new_id] = self.canvas_dict[old_id]
            self.canvas_dict.pop(old_id)
            self.text_dict[new_id] = self.text_dict[old_id]
            self.text_dict.pop(old_id)
            self.button_dict[new_id] = self.button_dict[old_id]
            self.button_dict.pop(old_id)
            self.active_modification_line = new_id

        self.gui.database[self.active_modification_line][0] = \
            self.text_dict[self.active_modification_line][1].get("1.0", "end").strip("\n")

        self.gui.database[self.active_modification_line][1] = \
            self.text_dict[self.active_modification_line][0].get("1.0", "end").strip("\n")

        self.modify_data(self.active_modification_line)

    def cancel_modification(self):
        self.modify_data(self.active_modification_line)

    def init_database_view(self):

        for id_ in self.gui.database.keys():
            self.create_line(id_=id_, first_name=self.gui.database[id_][0], last_name=self.gui.database[id_][1])

    def display_data(self):

        self.canvas_dict = dict(sorted(self.canvas_dict.items(), key=lambda x: x[1][1]))

        for canvas in [x[0] for x in self.canvas_dict.values()]:
            canvas.pack(fill="x")
            canvas.bind("<Button-1>", lambda e: self.focus_set())

        self.adjust_scrollable_region()

    def hide_data(self):
        for canvas in [x[0] for x in self.canvas_dict.values()]:
            canvas.pack_forget()
            canvas.unbind("<Button-1>")

    def adjust_scrollable_region(self, for_keyboard=False):

        try:
            region = sum([int(elem[0].cget("height")) // 4.3 for elem in self.canvas_dict.values()])

            if for_keyboard:
                region += self.gui.touch_keyboard.height

            self.canvas.configure(scrollregion=(0, 0, 0, region))

        except:
            Log().write_log_exception()

    def display_touch_keyboard(self, event):

        if event.widget["state"] == "normal":
            self.gui.touch_keyboard.display(event)
            self.adjust_scrollable_region(for_keyboard=True)

    def hide_touch_keyboard(self):
        self.adjust_scrollable_region()
        self.gui.touch_keyboard.hide()

    def display(self):
        self.bind("<Button-1>", lambda e: self.focus_set())
        self.gui.root.bind_class("Text", "<FocusIn>", lambda e: self.display_touch_keyboard(e))
        self.gui.root.bind_class("Text", "<FocusOut>", lambda e: self.hide_touch_keyboard())
        self.display_data()
        self.pack(expand="yes")

    def hide(self):
        self.unbind("<Button-1>")
        self.hide_data()
        self.gui.root.unbind_class("Entry", "<FocusIn>")
        self.gui.root.unbind_class("Entry", "<FocusOut>")
        self.pack_forget()
