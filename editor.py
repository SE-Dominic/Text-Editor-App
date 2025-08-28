from tkinter import *
from tkinter import ttk

'''
Objectives: Text Editor
    - create text area with ability to write and edit
    - add scrollbars to allow better navigation
    - create a file menu that allows user to:
        - clear text area
        - open new text file into editor
        - save/ save-as functionality
    - insert basic editing: 
        - copy, cut, paste
        - undo, redo
    - light/ dark mode functionality
'''

def get_resolution():
    root = Tk()
    root.withdraw() #prevents window from popping up

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

if __name__ == "__main__":
    width, height = get_resolution()
    window = Tk()
    window.title("TEXT EDITOR APP")
    window.geometry(f"{width}x{height}")
    window.exec()