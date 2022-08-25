# Kim Schalk
# 25/08/2022
# Add Payment Window Design - Version 1

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
hana_image = Image.open("hana_profile_icon.png")

# Child Names
children = ["Nikau", "Hana", "Tia"]

root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Profile Image
hana_image = hana_image.resize((50, 50))
hana_image = ImageTk.PhotoImage(hana_image)
image_panel = Label(root, image=hana_image, bg=background_colour)
image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

name_label = Label(root, text="Payment", font=("Comfortaa", 25, "bold"), bg=background_colour)
name_label.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="w")

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

# Input Labels and Entries
child_label = Label(root, text="Child:", bg=background_colour, font=("Comfortaa", 12, "bold"))
child_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 10))
chosen_child = StringVar()
chosen_child.set("Choose Child")
child_dropdown = OptionMenu(root, chosen_child, *children)
child_dropdown.grid(row=2, column=0, columnspan=2, sticky="w", padx=20)
child_dropdown.config(bg=button_colour, font=("Comfortaa", 8), bd=1, relief="solid")
item_label = Label(root, text="Item:", bg=background_colour, font=("Comfortaa", 12, "bold"))
item_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 10))
item_entry = Entry(root, font=("Comfortaa", 10), bd=1)
item_entry.grid(row=4, column=0, columnspan=3, padx=15)
item_entry.config(width=40)
cost_label = Label(root, text="Cost:", bg=background_colour, font=("Comfortaa", 12, "bold"))
cost_label.grid(row=5, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 10))
cost_entry = Entry(root, font=("Comfortaa", 10), bd=1)
cost_entry.grid(row=6, column=0, columnspan=3, padx=15)
cost_entry.config(width=40)

enter_button = Button(root, text="Enter", bg=button_colour, font=("Comfortaa", 12), bd=1, relief="solid")
enter_button.grid(row=7, column=0, columnspan=3, pady=(30, 20), ipadx=25)

# End of Program
root.mainloop()
