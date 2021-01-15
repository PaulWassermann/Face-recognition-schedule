from model.log import Log
from view.gui import GUI

try:
    gui = GUI()

    gui.start_menu.display()

    gui.root.mainloop()

except:
    Log().write_log_exception(level="error",
                              message="Un problème est survenu lors de l'exécution de l'application.",
                              show=True,
                              log=False)

