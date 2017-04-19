# From http://stackoverflow.com/a/14119223/6816646
# with askdirectory() to request folder path
def setPath(filename='.dataFolderPath'):
	import tkinter as tk
	from tkinter import filedialog

	root=tk.Tk()
	root.withdraw()
	root.wm_attributes('-topmost', 1)
	data_folder_path=filedialog.askdirectory(parent=root)
	if len(data_folder_path)>0:
		with open(filename,'w') as f:
			f.write(data_folder_path)

	root.quit()
	
	return data_folder_path
