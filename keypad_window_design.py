# Kim Schalk
# 17/08/2022
# Keypad Window Design - Version 1

# Import Libraries
from tkinter import *
from matplotlib import font_manager

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"
keypad_buttons_colour = "#efefef"

# Keypad Window
root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=2, pady=7, padx=7, sticky=E)

# Password Label
label_border = Frame(root, bg="black")
label_border.grid(row=1, column=0, columnspan=3, pady=10)
password_label = Label(label_border, text="* * * *", fg="black", bg=keypad_buttons_colour, font=("Inconsolata", 12),
                       bd=0)
password_label.grid(row=0, column=0, ipadx=72, ipady=3, pady=1, padx=1)

# Buttons 1-9
button_frame = Frame(root, bg=background_colour)
button_frame.grid(row=2, column=0, columnspan=3, padx=15, pady=10)
one_button = Button(button_frame, text="1", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                    relief="solid")
one_button.grid(row=0, column=0, ipadx=19, padx=7, pady=7)
two_button = Button(button_frame, text="2", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                    relief="solid")
two_button.grid(row=0, column=1, ipadx=17, padx=7, pady=7)
three_button = Button(button_frame, text="3", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                      relief="solid")
three_button.grid(row=0, column=2, ipadx=17, padx=7, pady=7)
four_button = Button(button_frame, text="4", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                     relief="solid")
four_button.grid(row=1, column=0, ipadx=17, padx=7, pady=7)
five_button = Button(button_frame, text="5", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                     relief="solid")
five_button.grid(row=1, column=1, ipadx=17, padx=7, pady=7)
six_button = Button(button_frame, text="6", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                    relief="solid")
six_button.grid(row=1, column=2, ipadx=17, padx=7, pady=7)
seven_button = Button(button_frame, text="7", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                      relief="solid")
seven_button.grid(row=2, column=0, ipadx=17, padx=7, pady=7)
eight_button = Button(button_frame, text="8", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                      relief="solid")
eight_button.grid(row=2, column=1, ipadx=17, padx=7, pady=7)
nine_button = Button(button_frame, text="9", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                     relief="solid")
nine_button.grid(row=2, column=2, ipadx=17, padx=7, pady=7)

# Other Buttons (Delete, 0, and Enter)
delete_button = Button(button_frame, text="Delete", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 8), bd=1,
                       relief="solid")
delete_button.grid(row=3, column=0, ipadx=7, ipady=7, padx=7, pady=7)
zero_button = Button(button_frame, text="0", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12), bd=1,
                     relief="solid")
zero_button.grid(row=3, column=1, ipadx=17, padx=7, pady=7)
enter_button = Button(button_frame, text="Enter", fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 8), bd=1,
                      relief="solid")
enter_button.grid(row=3, column=2, ipadx=9, ipady=7, padx=7, pady=7)

# End of Program
root.mainloop()
