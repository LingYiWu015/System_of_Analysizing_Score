


import Show_Web_GUI
from Ulties import *

@Decotators.timer
def __Init__():
    print("Initializing>>>>>>>Please Wait")
    Tools.Make_dir_Safe("Outputs","Outputs",True)
    Tools.Make_dir_Safe("Inputs","Inputs",True)
    Tools.Make_dir_Safe("Sources","Sources",True)
    Tools.Make_dir_Safe(r"Sources\Files","Files",True)
    

if __name__ == "__main__":
    __Init__()
    Show_Web_GUI.Main_Window.launch()##Show The GUI