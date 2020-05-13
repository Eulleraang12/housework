import sys
import cx_Freeze
import smtplib
import os
import datetime
import schedule

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python36\\tcl\\tcl8.6"
os.environ['Tk_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python36\\tcl\\tk8.6"


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        cx_Freeze.Executable("TarefasCasa.py", base=None)
]

cx_Freeze.setup(
    name = "TarefasCasa",
    version = "3.0",
    description = "Script para organizar as tarefas de casa 2020",
    executables = executables
 )
