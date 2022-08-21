# Kim Schalk
# 17/08/2022
# Keypad Window Design - Version 2

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

# Buttons 1-9 in a loop
button_frame = Frame(root, bg=background_colour)
button_frame.grid(row=2, column=0, columnspan=3, padx=15, pady=10)
row = 0
column = 0
for button in range(1, 10):
    numbered_button = Button(button_frame, text=button, fg="black", bg=keypad_buttons_colour, font=("Comfortaa", 12),
                             bd=1, relief="solid")
    if button == 4:
        row += 1
    elif button == 7:
        row += 1

    if button == 1:
        ipadx = 19
    else:
        ipadx = 17

    numbered_button.grid(row=row, column=column, ipadx=ipadx, padx=7, pady=7)
    column += 1
    if column == 3:
        column = 0

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
