# Kim Schalk
# 22/08/2022
# Child Selection Window Design - Version 1

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"

# Keypad Window
root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=0, pady=7, padx=7, sticky=E)

# Child Resized Images
nikau_image = Image.open("nikau_profile_icon.png")
nikau_image = nikau_image.resize((40, 40))
nikau_icon = ImageTk.PhotoImage(nikau_image)
tia_image = Image.open("tia_profile_icon.png")
tia_image = tia_image.resize((40, 40))
tia_icon = ImageTk.PhotoImage(tia_image)
hana_image = Image.open("hana_profile_icon.png")
hana_image = hana_image.resize((40, 40))
hana_icon = ImageTk.PhotoImage(hana_image)

# Child Buttons
nikau_frame = Frame(root, bd=1, relief="solid", bg=button_colour)
nikau_frame.grid(row=1, column=0, ipadx=3, padx=10, pady=5)
nikau_button = Button(nikau_frame, text="  Nikau - $98.00", image=nikau_icon, compound=LEFT, fg="black",
                      bg=button_colour, font=("Comfortaa", 12), bd=0, relief="solid", anchor="w")
nikau_button.grid(row=1, column=0, pady=5, padx=10, ipadx=23, ipady=4)

tia_frame = Frame(root, bd=1, relief="solid", bg=button_colour)
tia_frame.grid(row=2, column=0, ipadx=3, padx=10, pady=5)
tia_button = Button(tia_frame, text="  Tia - $98.00", image=tia_icon, compound=LEFT, fg="black", bg=button_colour,
                    font=("Comfortaa", 12), bd=0, relief="solid", anchor="w")
tia_button.grid(row=2, column=0, pady=5, padx=10, ipadx=35, ipady=4)

hana_frame = Frame(root, bd=1, relief="solid", bg=button_colour)
hana_frame.grid(row=3, column=0, ipadx=3, padx=10, pady=(5, 20))
hana_button = Button(hana_frame, text="  Hana - $98.00", image=hana_icon, compound=LEFT, fg="black", bg=button_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid", anchor="w")
hana_button.grid(row=3, column=0, pady=5, padx=10, ipadx=24, ipady=4)

# End of Program
root.mainloop()
