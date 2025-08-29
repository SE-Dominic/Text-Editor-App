from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
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

def get_resolution() -> int:
    root = Tk()
    root.withdraw() #prevents window from popping up

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor App")
        s_width, s_height = get_resolution()
        self.root.geometry(f"{s_width}x{s_height}")

        #text area
        custom_font = tkFont.Font(family="Arial", size=20)
        text_area = Text(self.root, bg="#EDE9DD", fg="#964B00", font=custom_font, width=s_width - 300, height=s_height - 300)
        text_area.pack(fill="both", expand=True)
        
        #menu
        '''
        dropdown options:
            - clear text
            - open new text file
            - save / save-as 
        '''
        def clearText(txt_area : Text) -> None:
            txt_area.delete('1.0', 'end-1c') #delete all text
        self.menubar = Menu(self.root)
        #add file button and functionality
        file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu = file)
        file.add_command(label = "New File", command = None)
        file.add_command(label = "Clear All", command = clearText(text_area))
        file.add_command(label = "Save", command = None)
        file.add_command(label = "Save As...", command = None)
        file.add_command(label="Exit", command = root.destroy)
        #editing
        '''
        Buttons:
            - undo
            - redo
            - copy
            - cut
            - paste
            - find
        '''
        #light/dark mode
        '''button that changes the background to be a 'dark mode' theme '''
        root.config(menu = self.menubar)



if __name__ == "__main__":
    root = Tk()
    editor = TextEditor(root)
    root.mainloop()

