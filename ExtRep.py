#Title: Quick Batch Extension Replace
#Description: alter extensions of all matching files within a directory
#Author: dandruk (https://github.com/dandruk)

import PySimpleGUI as sg	#GUI
import os		#for altering filenames
import ntpath	#for getting directory path basename

#opens dialog window for input values
def run_GUI():
	layout = [
		[sg.Text('Directory: ', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('/'), sg.FolderBrowse()],
		[sg.Text('Enter old extension: ', auto_size_text=True, justification='right'), sg.InputText('')],
		[sg.Text('Enter new extension: ', auto_size_text=True, justification='right'), sg.InputText('')],
		[sg.Submit()]
		]
	event, values = sg.Window('Select Directory', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
	
	return values #return first input, which is the selected directory

#replaces the extensions in the given directory
def replace_in(path, old, new):
	for filename in os.listdir(path):
		if filename.endswith(old):
			file = os.path.join(path, filename)
			split_old = file.split(old)
			new_filename = split_old[0] + new
			os.rename(file, new_filename)
			
			sg.Popup("In directory " + ntpath.basename(selectPath) + ": ", old + " replaced with " + new)	
		else:
			sg.Popup("Extension replacement could not be completed.")

#PROGRAM START

values = run_GUI()

selectPath = values[0]
old_ext = values[1]
new_ext = values[2]

replace_in(selectPath, old_ext, new_ext)