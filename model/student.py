from face_recognition import face_encodings
from requests import get
import json


class Student:

    def __init__(self, gui, id_="20200001", first_name=None, last_name=None):
        self.gui = gui
        self.__id = id_
        self.__first_name = ""
        self.__last_name = ""
        self.__face_encoding = []

        if first_name is not None:
            self.set_first_name(first_name)

        if last_name is not None:
            self.set_last_name(last_name)

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):

        if "-" in first_name:
            surnames = first_name.split("-")

            for surname in surnames:
                surname.capitalize()

            self.__first_name = "-".join(surnames)

        else:
            self.__first_name = first_name.capitalize()

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        if "-" in last_name:
            elements = last_name.split("-")

            for element in elements:

                element.capitalize()

            last_name = "-".join(elements)

        if " " in last_name:
            elements = last_name.split(" ")

            for element in elements:

                if element not in ["de", "De", "DE"]:
                    element.capitalize()

                else:
                    element.lower()

            last_name = " ".join(elements)

        self.__last_name = last_name

    def get_face_encoding(self):
        return self.__face_encoding

    def set_face_encoding(self, image=None, encoding=None):

        if image is not None:
            self.__face_encoding = list(face_encodings(image)[0])

        if encoding is not None:
            self.__face_encoding = list(encoding)

    def get_schedule(self):
        try:
            request = get(f"https://serenade.centrale-marseille.fr/utilisateurs/livecal/"
                          f"{self.__last_name}/{self.__first_name}")
            print(request.text)
            return True

        except:
            return False

    def dump_info(self):
        self.gui.database[self.__id] = [self.__first_name, self.__last_name, self.__face_encoding]

    def __eq__(self, student):
        return self.__id == student.get_id()

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} ({self.__id})"
