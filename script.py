import os
import tkinter as tk
from tkinter import filedialog

def selectFolder():
    root = tk.Tk()
    root.withdraw()

    folderPath = filedialog.askdirectory(title="Select the submissions folder")

    if folderPath:
        print(f"Selected folder: {folderPath}")
    else:
        print("No folder selected.")
    return folderPath

# Maybe a file to remove comments, but IDK I want to see thier comments. But we might want to strip them for the AI

# call open AI api with each file content and prompt it. Return the results
def 

#todo, rename to something more accurate or other refactor so getFolderContent name isn't so stupid
def getFolderContent(folderPath):
    for fileName in os.listdir(folderPath):
        with open(os.path.join(folderPath, fileName), 'r', encoding='utf-8') as f:
            fileContent = f.read()
            print(fileContent)
            # give file content to AI

            # write/append content to new file.



# take each file in the folder
selectedFolder = selectFolder()
getFolderContent(selectedFolder)


# submit it to open ai api with query

# get results back and append to output file with text for the of file name

# append the SQL code to a new file with all the sql submissions

