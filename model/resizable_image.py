import PIL

# The sole purpose of this class is to store images while being able to resize them so the application assets can be
# adjusted to the size of the screen


class ResizableImage:

    def __init__(self, path_to_image=None, pil_image=None):

        if path_to_image is not None:
            self.PIL_image = PIL.Image.open(path_to_image)

        elif pil_image is not None:
            self.PIL_image = pil_image

        self.image = PIL.ImageTk.PhotoImage(image=self.PIL_image)

        self.ratio = self.PIL_image.width / self.PIL_image.height

    # The resize method returns a PhotoImage instance
    def resize_to_tk(self, width=None, height=None, x_ratio=None, y_ratio=None):

        if x_ratio is not None and y_ratio is None:
            width = x_ratio * self.PIL_image.width
            height = self.ratio * self.PIL_image.height

        elif x_ratio is None and y_ratio is not None:
            width = self.PIL_image.width / self.ratio
            height = y_ratio * self.PIL_image.height

        elif x_ratio is not None and y_ratio is not None:
            width = x_ratio * self.PIL_image.width
            height = y_ratio * self.PIL_image.height

        else:

            if height is None:
                height = width / self.ratio

            elif width is None:
                width = self.ratio * height

        return PIL.ImageTk.PhotoImage(image=self.PIL_image.resize((int(width), int(height)), PIL.Image.ANTIALIAS))
