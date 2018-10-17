#Title: Quick Batch Extension Replace
#Description: Gives files new extensions in a directory
#Author: dandruk (https://github.com/dandruk)

import os
import shutil
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import ntpath
import xml.etree.ElementTree as etree
from urllib.parse import unquote

#opens dialog window for user to select directory
def open_selection():
	root = Tk()
	root.withdraw() #hides tk root window
	folder =  filedialog.askdirectory(initialdir = "/",title = "Select directory")
	return (folder)

#replaces the extensions in the given directory
def replace_in(path, old, new):
	for filename in os.listdir(path):
		if filename.endswith(old):
			file = os.path.join(path, filename)
			split_old = file.split(old)
			new_filename = split_old[0] + new
			os.rename(file, new_filename)

#PROGRAM START

selectPath = open_selection() #select path to directory
selectDir = ntpath.basename(selectPath) #directory name

old_ext = input("Enter old extension:")
new_ext = input("Enter new extension:")

replace_in(selectPath, old_ext, new_ext)

messagebox.showinfo("Replacement in " + selectDir + ": ", old_ext + " replaced with " + new_ext)