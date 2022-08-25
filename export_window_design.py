# Kim Schalk
# 25/08/2022
# Export Window Design - Version 1

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

root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Profile Image
hana_image = hana_image.resize((50, 50))
hana_image = ImageTk.PhotoImage(hana_image)
image_panel = Label(root, image=hana_image, bg=background_colour)
image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

name_label = Label(root, text="Export", font=("Comfortaa", 25, "bold"), bg=background_colour)
name_label.grid(row=0, column=1, padx=5, pady=(20, 10), sticky="w")

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

export_text = """Enter the name of the file you would 
like to save the document as, it cannot 
contain any of the following 
characters: /\:*?”<>| and it cannot 
have the same name as an existing file."""
export_label = Label(root, text=export_text, bg=background_colour, font=("Comfortaa", 8), justify=LEFT)
export_label.grid(row=1, column=0, columnspan=3, padx=20, pady=5)

filename_entry = Entry(root, bd=1)
filename_entry.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
filename_entry.config(width=35)
enter_button = Button(root, text="Enter", bg=button_colour, font=("Comfortaa", 12), bd=1, relief="solid")
enter_button.grid(row=3, column=0, columnspan=3, pady=10, ipadx=25)

# End of Program
root.mainloop()
