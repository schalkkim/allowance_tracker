# Kim Schalk
# 22/08/2022
# Child Selection Window Design - Version 2

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"

# Child Images
nikau_image = Image.open("nikau_profile_icon.png")
tia_image = Image.open("tia_profile_icon.png")
hana_image = Image.open("hana_profile_icon.png")

# List of Children
children = [["nikau", "nikau_profile_icon.png", 98.00, nikau_image], ["hana", "hana_profile_icon.png", 98.00, hana_image],
            ["tia", "tia_profile_icon.png", 98.00, tia_image]]

# Keypad Window
root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=0, pady=7, padx=7, sticky=E)

# Child buttons in a loop
row = 1
for child in children:
    # Resizing Images
    child[3] = child[3].resize((40, 40))
    child[3] = ImageTk.PhotoImage(child[3])

    # Buttons
    button_frame = Frame(root, bd=1, relief="solid", bg=button_colour)
    button_frame.grid(row=row, column=0, ipadx=3, padx=10, pady=5)
    text = "  {} - ${:.2f}".format(child[0].capitalize(), child[2])
    button = Button(button_frame, text=text, image=child[3], compound=LEFT, fg="black", bg=button_colour,
                    font=("Comfortaa", 12), bd=0, relief="solid", anchor="w")
    button.grid(row=0, column=0, pady=5, padx=10, ipady=4)
    button.config(width=185)
    if child == children[-1]:
        button_frame.grid(pady=(5, 20))
    row += 1

# End of Program
root.mainloop()
