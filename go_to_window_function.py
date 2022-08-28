# Kim Schalk
# 26/08/2022
# Go to Window Function - Version 2

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"

root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Open a New Window
def go_to_window(button):
    new_window = Tk()
    new_window.title("Allowance Tracker")
    new_window.config(bg=background_colour)
    root.destroy()
    def close_window(button):
        new_window.destroy()
    new_window.protocol("WM_DELETE_WINDOW", lambda: close_window(button))

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid", command=lambda: go_to_window(help_button))
help_button.grid(row=0, column=0, pady=7, padx=7, sticky=NE)

# End of Program
root.mainloop()
