######################################
# Script removes prefixes from files #       
######################################
import os
import tkinter as tk
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.withdraw()

path = askdirectory()
new_filename= ""
prefix = ""

filenames = os.listdir(path) 
for dir,subdir,listfilename in os.walk(path):
    for filename in listfilename:
        new_filename =  filename.removeprefix(prefix)
        src = os.path.join(dir, filename) 
        dst = os.path.join(dir, new_filename) 
        os.rename(src, dst)        
