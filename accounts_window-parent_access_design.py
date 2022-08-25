# Kim Schalk
# 24/08/2022
# Accounts Window - Parent Access - Version 1

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

months = ["August", "July", "June", "May"]

root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Profile Image
hana_image = hana_image.resize((50, 50))
hana_image = ImageTk.PhotoImage(hana_image)
image_panel = Label(root, image=hana_image, bg=background_colour)
image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

name_label = Label(root, text="Hana", font=("Comfortaa", 25, "bold"), bg=background_colour)
name_label.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="w")

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

# Account Labels
account_balance_label = Label(root, text="Account Balance:", bg=background_colour, font=("Comfortaa", 10))
account_balance_label.grid(row=1, column=0, columnspan=3, pady=(5, 0))
amount_label = Label(root, text="$123.00", bg=background_colour, font=("Comfortaa", 22))
amount_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))
bonus_frame = Frame(root, bg=button_colour)
bonus_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10))
bonus_label1 = Label(bonus_frame, text="Hana is on track for a bonus!", bg=button_colour, font=("Comfortaa", 9))
bonus_label1.grid(row=0, column=0, padx=20, pady=(5, 0))
bonus_label2 = Label(bonus_frame, text="Days until bonus: 46", bg=button_colour, font=("Comfortaa", 9, "italic"))
bonus_label2.grid(row=1, column=0, padx=20, pady=(0, 5))

# Transactions Components
transactions_label = Label(root, text="Previous Transactions:", bg=background_colour, font=("Comfortaa", 10, "bold"))
transactions_label.grid(row=4, column=0, columnspan=3, sticky=W, pady=5, padx=5)
left_button = Button(root, text="ᐸ", bg=background_colour, font=("Comfortaa", 12), bd=0)
left_button.grid(row=5, column=0, sticky=E)
right_button = Button(root, text="ᐳ", bg=background_colour, font=("Comfortaa", 12), bd=0)
right_button.grid(row=5, column=2, sticky=W)
chosen_month = StringVar()
chosen_month.set("Sort By Date")
sort_by_date_dropdown = OptionMenu(root, chosen_month, *months)
sort_by_date_dropdown.grid(row=5, column=1)

# Past Transactions with Scrollbar
transactions_frame = Frame(root)
transactions_frame.grid(row=6, column=0, columnspan=3, padx=20, pady=(10, 15), stick="nw")
transactions_frame.grid_rowconfigure(0, weight=1)
transactions_frame.grid_columnconfigure(0, weight=1)
transactions_frame.grid_propagate(False)
transactions_canvas = Canvas(transactions_frame)
transactions_canvas.grid(row=0, column=0, sticky=NSEW)
transactions_scrollbar = Scrollbar(transactions_frame, orient="vertical", command=transactions_canvas.yview)
transactions_scrollbar.grid(row=0, column=1, sticky=NS)
transactions_canvas.configure(yscrollcommand=transactions_scrollbar.set)
transactions_labels_frame = Frame(transactions_canvas)
transactions_canvas.create_window((0, 0), window=transactions_labels_frame, anchor="nw")
transaction1_background = Label(transactions_labels_frame, bd=0, bg="#f3f3f3")
transaction1_background.grid(row=0, column=0, columnspan=2, ipady=3)
transaction1_background.config(width=28)
transaction1_label = Label(transactions_labels_frame, text="Jacket", font=("Comfortaa", 10), bd=0, bg="#f3f3f3")
transaction1_label.grid(row=0, column=0, sticky="w")
transaction1_cost_label = Label(transactions_labels_frame, text="-$98.00 ", font=("Comfortaa", 10), bd=0, bg="#f3f3f3")
transaction1_cost_label.grid(row=0, column=1, sticky="e")
transaction2_background = Label(transactions_labels_frame, bd=0, bg="#d9d9d9")
transaction2_background.grid(row=1, column=0, columnspan=2, ipady=3)
transaction2_background.config(width=28)
transaction2_label = Label(transactions_labels_frame, text="Scarf", font=("Comfortaa", 10), bd=0, bg="#d9d9d9")
transaction2_label.grid(row=1, column=0, sticky="w")
transaction2_cost_label = Label(transactions_labels_frame, text="-$12.00 ", font=("Comfortaa", 10), bd=0, bg="#d9d9d9")
transaction2_cost_label.grid(row=1, column=1, sticky="e")
transaction3_background = Label(transactions_labels_frame, bd=0, bg="#f3f3f3")
transaction3_background.grid(row=2, column=0, columnspan=2, ipady=3)
transaction3_background.config(width=28)
transaction3_label = Label(transactions_labels_frame, text="Tennis Shoes", font=("Comfortaa", 10), bd=0, bg="#f3f3f3")
transaction3_label.grid(row=2, column=0, sticky="w")
transaction3_cost_label = Label(transactions_labels_frame, text="-$120.00 ", font=("Comfortaa", 10), bd=0, bg="#f3f3f3")
transaction3_cost_label.grid(row=2, column=1, sticky="e")
transaction4_background = Label(transactions_labels_frame, bd=0, bg="#d9d9d9")
transaction4_background.grid(row=3, column=0, columnspan=2, ipady=3)
transaction4_background.config(width=28)
transaction4_label = Label(transactions_labels_frame, text="Scarf", font=("Comfortaa", 10), bd=0, bg="#d9d9d9")
transaction4_label.grid(row=3, column=0, sticky="w")
transaction4_cost_label = Label(transactions_labels_frame, text="-$12.00 ", font=("Comfortaa", 10), bd=0, bg="#d9d9d9")
transaction4_cost_label.grid(row=3, column=1, sticky="e")
transaction5_background = Label(transactions_labels_frame, bd=0, bg="#f3f3f3")
transaction5_background.grid(row=4, column=0, columnspan=2, ipady=3)
transaction5_background.config(width=28)
transaction5_label = Label(transactions_labels_frame, text="Tennis Shoes", font=("Comfortaa", 10), bd=0, bg="#f3f3f3")
transaction5_label.grid(row=4, column=0, sticky="w")
transaction5_cost_label = Label(transactions_labels_frame, text="-$120.00 ", font=("Comfortaa", 10), bd=0, bg="#f3f3f3")
transaction5_cost_label.grid(row=4, column=1, sticky="e")
# Allows resizing of labels
transactions_labels_frame.update_idletasks()
# Change size of the box
transactions_frame.config(width=225, height=100)
# Set scrolling region
transactions_canvas.config(scrollregion=transactions_canvas.bbox("all"))

# Buttons
button_frame = Frame(root, bg="black")
button_frame.grid(row=7, column=0, columnspan=3, pady=(0, 20))
add_transaction_button = Button(button_frame, text="Add Transaction", bg=button_colour, font=("Comfortaa", 9), bd=0, relief="solid")
add_transaction_button.grid(row=0, column=0, padx=(1, 1), pady=(1, 1))
add_transaction_button.config(width="13")
add_payment_button = Button(button_frame, text="Add Payment", bg=button_colour, font=("Comfortaa", 9), bd=0, relief="solid")
add_payment_button.grid(row=0, column=1, padx=(0, 1), pady=(1, 1))
add_payment_button.config(width="13")
statistics_button = Button(button_frame, text="Statistics", bg=button_colour, font=("Comfortaa", 9), bd=0, relief="solid")
statistics_button.grid(row=1, column=0, padx=(1, 1), pady=(0, 1))
statistics_button.config(width="13")
export_button = Button(button_frame, text="Export", bg=button_colour, font=("Comfortaa", 9), bd=0, relief="solid")
export_button.grid(row=1, column=1, padx=(0, 1), pady=(0, 1))
export_button.config(width="13")

# End of Program
root.mainloop()
