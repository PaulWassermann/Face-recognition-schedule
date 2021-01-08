from tkinter import messagebox
import os
import logging
import datetime

monthTranslationDict = {'January': 'Janvier', 'February': 'Février', 'March': 'Mars', 'April': 'Avril', 'May': 'Mai',
                        'June': 'Juin', 'July': 'Juillet', 'August': 'Août', 'September': 'Septembre',
                        'October': 'Octobre', 'November': 'Novembre', 'December': 'Décembre'}

# This class allows us to write to the specified file every errors occurring while the application is running
# Useful when debugging


class Log:

    def __init__(self):

        # Attributes related to time
        self.time = datetime.datetime.now()
        self.year = self.time.strftime("%Y")
        self.month = monthTranslationDict[self.time.strftime("%B")]
        self.dayOfTheMonth = self.time.strftime("%d")
        self.hour = self.time.strftime("%H")
        self.minute = self.time.strftime("%M")
        self.second = self.time.strftime("%S")

        # Allows us to know if we're writing to a new file
        self.new = False

        # Path to the log file
        self.dirs = f"Log\\{self.month} {self.year}"
        self.pathname = self.dirs + f"\\{self.dayOfTheMonth}.txt"

        # Verify is the log file of the day already exists
        self.check_on_log_path()

        logger = logging.getLogger()

        # If not already done, we format the output written in our file
        if not logger.hasHandlers():

            self.fileHandler = logging.FileHandler(filename=self.pathname, mode='a')
            self.customFormatter = OneLineExceptionFormatter(fmt="%(message)s")
            self.fileHandler.setFormatter(self.customFormatter)
            logger.addHandler(self.fileHandler)
            logger.setLevel(logging.INFO)

            if self.new:
                self.write_log_info("Log of the day was successfully created and initialized.")

    def check_on_log_path(self):

        try:
            if not os.path.exists(f"{os.getcwd()}\\{self.dirs}"):
                os.makedirs(f"{self.dirs}")

            if not os.path.exists(f"{self.pathname}"):
                self.new = True

        except OSError:
            messagebox.showerror("Log Error", "A problem occurred while creating a directory for the current log.")

        except:
            messagebox.showerror("Log Error",
                                 "A problem occurred while checking if a path to the log exists and could "
                                 "not be logged.")

    def write_log_info(self, message):

        logging.info(f"[{self.hour}:{self.minute}:{self.second}] Info   :  {message}")

    def write_log_exception(self, level="error", message="", show=True, log=False):

        if level == "warning":

            if show:
                messagebox.showwarning("Warning", message)

            if log:
                logging.exception(f"[{self.hour}:{self.minute}:{self.second}] Warning:  {message}")

            else:
                logging.exception(f"[{self.hour}:{self.minute}:{self.second}] Warning: ")

        elif level == "error":

            if show:
                messagebox.showerror("Error", message)

            if log:
                logging.exception(f"[{self.hour}:{self.minute}:{self.second}] Error  :  {message}")

            else:
                logging.exception(f"[{self.hour}:{self.minute}:{self.second}] Error  : ")


class OneLineExceptionFormatter(logging.Formatter):

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)

        if record.exc_text:
            s = s.replace('\n', ' ')
            s = s.replace('Traceback (most recent call last):  ', '')

        return s
