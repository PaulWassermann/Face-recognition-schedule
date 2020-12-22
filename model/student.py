from face_recognition import face_encodings
from requests import get
import json


class Student:

    def __init__(self, gui, id_="20200001", first_name=None, last_name=None):
        self.gui = gui
        self.__id = id_
        self.__first_name = ""

        if first_name is not None:
            self.set_first_name(first_name)

        self.__last_name = ""

        if last_name is not None:
            self.set_last_name(last_name)

        self.__face_encoding = []

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):

        if "-" in first_name:
            surnames = first_name.split("-")

            for surname in surnames:
                surname = surname.capitalize()

            self.__first_name = "-".join(surnames)

        else:
            self.__first_name = first_name.capitalize()

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):

        if "-" in last_name:
            elements = last_name.split("-")

            for element in elements:

                element = element.capitalize()

            last_name = "-".join(elements)

        if " " in last_name:
            elements = last_name.split(" ")

            for element in elements:

                if element not in ["de", "De", "DE"]:
                    element = element.capitalize()

                else:
                    element = element.lower()

            last_name = " ".join(elements)

        self.__last_name = last_name

    def get_face_encoding(self):
        return self.__face_encoding

    def set_face_encoding(self, image):
        self.__face_encoding = list(face_encodings(image)[0])

    def get_schedule(self):

        try:
            request = get(f"https://serenade.centrale-marseille.fr/utilisateurs/livecal/"
                          f"{self.__last_name}/{self.__first_name}")
            print(request.text)
            return True

        except:
            return False

    def dump_infos(self, file):
        self.gui.database = {}
        with open(file, 'r') as database:
            self.gui.database = json.load(database)
            self.gui.database[self.__id] = [self.__first_name, self.__last_name, self.__face_encoding]

        with open(file, 'w') as database:
            dump = self.gui.database
            json.dump(dump, database, sort_keys=True, indent=4)

    def __eq__(self, student):
        return self.__id == student.get_id()

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} ({self.__id})"