import PIL


class ResizableImage:

    def __init__(self, path_to_image=None, pil_image=None):

        if path_to_image is not None:
            self.image = PIL.Image.open(path_to_image)

        elif pil_image is not None:
            self.image = pil_image

    def resize_to_tk(self, width=None, height=None, x_ratio=None, y_ratio=None):

        if x_ratio is not None and y_ratio is None:
            width = height = x_ratio * self.image.width

        elif x_ratio is None and y_ratio is not None:
            width = height = y_ratio * self.image.height

        elif x_ratio is not None and y_ratio is not None:
            width = x_ratio * self.image.width
            height = y_ratio * self.image.height

        else:

            if height is None:
                height = width

            elif width is None:
                width = height

        # print(width, height)
        return PIL.ImageTk.PhotoImage(image=self.image.resize((int(width), int(height)), PIL.Image.ANTIALIAS))
