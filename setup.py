import sys
from cx_Freeze import setup, Executable

version = "1.0.0"

base = None

if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {"include_files": ["assets/"], "excludes": ["matplotlib.tests", "numpy.random._examples"],
                     "include_msvcr": True}

setup(
    name="Mon Emploi du Temps",
    version=version,
    description=f"Mon Emploi du Temps version {version}",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(script="main.py", base=base, targetName="Mon Emploi du Temps.exe",
                   shortcutName="Mon Emploi du Temps",
                   shortcutDir="DesktopFolder", icon="assets/logo.ico")]
)
