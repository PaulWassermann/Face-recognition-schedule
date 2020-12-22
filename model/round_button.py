from math import sqrt


class RoundButton:

    def __init__(self, canvas, gui, x, y, radius, text="", font=None, text_color=None, justify=None,
                 image=None, image_on_click=None, command=None):

        self.canvas = canvas
        self.gui = gui

        self.x = x
        self.y = y
        self.radius = radius
        self.text = text
        self.text_id = 0

        if font is None:
            font = ("helvetica", 16)

        if text_color is None:
            text_color = "green"

        if justify is None:
            justify = "left"

        self.font = font
        self.text_color = text_color
        self.justify = justify
        self.image = image
        self.image_on_click = image_on_click
        self.command = command

        self.circle_id = 0
        self.image_id = 0
        self.pressed = False

        self.shape()

        if image is not None:
            self.canvas.tag_bind(self.image_id, "<ButtonPress-1>", self.on_click)
            self.canvas.tag_bind(self.image_id, "<ButtonRelease-1>", self.on_release)

        else:
            self.canvas.tag_bind(self.circle_id, "<ButtonPress-1>", self.on_click)
            self.canvas.tag_bind(self.circle_id, "<ButtonRelease-1>", self.on_release)

    def shape(self):

        x0 = self.x
        y0 = self.y
        x1 = self.x + 2 * self.radius
        y1 = self.y + 2 * self.radius
        fill = ""

        if self.image is None:
            fill = "white"

        self.circle_id = self.canvas.create_oval(x0, y0, x1, y1, outline="", fill=fill)
        self.image_id = self.canvas.create_image(x0, y0, image=self.image, anchor="center")

        if self.text != "":
            self.text_id = self.canvas.create_text(x0, y0 + int(3 * self.radius / 5), text=self.text, font=self.font,
                                    fill=self.text_color, justify=self.justify, anchor="center")

    def on_click(self, event):

        if sqrt((event.x - self.x) ** 2 + (event.y - self.y) ** 2) <= self.radius:
            self.canvas.itemconfigure(self.image_id, image=self.image_on_click)
            self.pressed = True

    def on_release(self, event):

        if self.pressed:

            self.canvas.itemconfigure(self.image_id, image=self.image)
            self.gui.root.update()

            if sqrt((event.x - self.x) ** 2 + (event.y - self.y) ** 2) <= self.radius and self.command is not None:
                self.command()

            self.pressed = False

    def update_text(self, text):
        self.canvas.itemconfigure(self.text_id, text=text)