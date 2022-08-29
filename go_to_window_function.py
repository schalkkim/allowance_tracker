# Kim Schalk
# 26/08/2022
# Go to Window Function - Version 3

# Import Libraries
from tkinter import *
from matplotlib import font_manager

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.config(bg=background_colour)
        self.main_window.title("Allowance Tracker")
        self.main_window.grid()
        # Help Button
        self.help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.main_window, image=self.help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour, font=("Comfortaa", 12), bd=0, relief="solid",
                                  command=self.go_to_new_window)
        self.help_button.grid(row=0, column=0, pady=7, padx=7, sticky=NE)
        self.main_window.mainloop()

    def go_to_new_window(self):
        NewWindow(self)


class NewWindow:
    def __init__(self, partner):
        self.new_window = Tk()
        self.new_window.config(bg=background_colour)
        self.new_window.title("Allowance Tracker")
        self.new_window.grid()

        partner.main_window.destroy()

        self.new_window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.new_window.mainloop()

    def close_window(self):
        self.new_window.destroy()
        MainWindow()


# main routine
if __name__ == "__main__":
    MainWindow()
