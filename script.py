import os
import tkinter as tk
from tkinter import filedialog
import openai
from config import OPENAI_API_KEY, AI_PROMPT, FEEDBACK_OUTPUT_FILE, SUBMISSIONS_OUTPUT_FILE

def selectFolder():
    root = tk.Tk()
    root.withdraw()

    folderPath = filedialog.askdirectory(title="Select the submissions folder")

    if folderPath:
        print(f"Selected folder: {folderPath}")
    else:
        print("No folder selected.")
    return folderPath

def resetOutputFiles():
    with open(FEEDBACK_OUTPUT_FILE, 'w') as f:
        f.write('')
    with open(SUBMISSIONS_OUTPUT_FILE, 'w') as f:
        f.write('')

def appendToFile(fileName, header, content):
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write("## " + header + "\n\n" + content + "\n\n")

# Maybe a file to remove comments, but IDK I want to see thier comments. But we might want to strip them for the AI
def getAIFeedback(inputText):
        openai.api_key = OPENAI_API_KEY
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= AI_PROMPT + inputText,
            temperature=0.5,
            max_tokens=1000,
            n=1,
            stop=None,
            timeout=5
        )
        if response.choices:
            return response.choices[0].text.strip()
        else:
            return None


#todo, rename to something more accurate or other refactor so getFolderContent name isn't so stupid
def getFolderContent(folderPath):
    for fileName in os.listdir(folderPath):
        with open(os.path.join(folderPath, fileName), 'r', encoding='utf-8') as f:
            fileContent = f.read()
            print(f'Getting feedback on {fileName}')
            feedback = getAIFeedback(fileContent)
            appendToFile(FEEDBACK_OUTPUT_FILE, fileName, feedback)
            appendToFile(SUBMISSIONS_OUTPUT_FILE, fileName, fileContent)

resetOutputFiles()
selectedFolder = selectFolder()
getFolderContent(selectedFolder)
