# Kim Schalk
# 26/08/2022
# Help Window Design - Version 1

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

# Components
name_label = Label(root, text="Help", font=("Comfortaa", 25, "bold"), bg=background_colour)
name_label.grid(row=0, column=0, padx=5, pady=(15, 10))

transactions_frame = Frame(root)
transactions_frame.grid(row=1, column=0, padx=20, pady=(0, 30), stick="nw")
transactions_frame.grid_rowconfigure(0, weight=1)
transactions_frame.grid_columnconfigure(0, weight=1)
transactions_frame.grid_propagate(False)
transactions_canvas = Canvas(transactions_frame, bg=button_colour)
transactions_canvas.grid(row=0, column=0, sticky=NSEW)
transactions_scrollbar = Scrollbar(transactions_frame, orient="vertical", command=transactions_canvas.yview)
transactions_scrollbar.grid(row=0, column=1, sticky=NS)
transactions_canvas.configure(yscrollcommand=transactions_scrollbar.set)
transactions_labels_frame = Frame(transactions_canvas)
transactions_canvas.create_window((0, 0), window=transactions_labels_frame, anchor="nw")

information = """To start enter your pin

Choose the child who's account you 
would like to view, if you only have
one child, you will go straight to
the accounts page.

On the accounts page you can view
the amount of money the child has
and their previous transactions. You
can sort their transactions by month
by using the dropdown menu to choose
a month, or by using the arrows to
change months.
To add money to a child, push the
"add payment" button. This will take
you to a window where you can enter
the reason and the amount.
To remove money, push the "add
transaction" button. This will take
you to a window where you can add the
item they bought and the cost.
To export their previous transactions,
press the "export" button."""

information_label = Label(transactions_labels_frame, text=information, bg=button_colour, font=("Comfortaa", 9),
                          justify=LEFT)
information_label.grid(row=0, column=0)

# Allows resizing of labels
transactions_labels_frame.update_idletasks()
# Change size of the box
transactions_frame.config(width=260, height=260)
# Set scrolling region
transactions_canvas.config(scrollregion=transactions_canvas.bbox("all"))

# End of Program
root.mainloop()
