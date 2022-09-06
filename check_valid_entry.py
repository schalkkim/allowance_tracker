# Kim Schalk
# 07/09/2022
# Check Valid Entry - Version 2

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from tkinter import messagebox

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Accounts Window")
        self.main_window.config(bg=background_colour)

        self.item_entry = Entry(self.main_window)
        self.item_entry.grid(row=0, column=0, padx=10, pady=10)
        self.enter_button = Button(self.main_window, text="Enter", bg=button_colour, font=("Comfortaa", 12),
                                   bd=1, relief="solid", command=lambda: self.check_valid_entry(self))
        self.enter_button.grid(row=2, column=0, padx=10, pady=10)

        self.main_window.mainloop()

    @staticmethod
    def check_valid_entry(partner):
        try:
            amount = partner.item_entry.get()
            if amount[0] == "$":
                amount = float(amount[1:])
                print(amount)
            else:
                amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Not a valid entry")


# main routine
if __name__ == "__main__":
    MainWindow()
