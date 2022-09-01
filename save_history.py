# Kim Schalk
# 01/09/2022
# Save History - Version 1

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"

row = 0
transactions = 0


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Accounts Window")
        self.main_window.config(bg=background_colour)

        self.transactions_frame = Frame(self.main_window)
        self.transactions_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 15), stick="nw")
        self.transactions_frame.grid_rowconfigure(0, weight=1)
        self.transactions_frame.grid_columnconfigure(0, weight=1)
        self.transactions_frame.grid_propagate(False)
        self.transactions_canvas = Canvas(self.transactions_frame)
        self.transactions_canvas.grid(row=0, column=0, sticky=NSEW)
        self.transactions_scrollbar = Scrollbar(self.transactions_frame, orient="vertical",
                                                command=self.transactions_canvas.yview)
        self.transactions_scrollbar.grid(row=0, column=1, sticky=NS)
        self.transactions_canvas.configure(yscrollcommand=self.transactions_scrollbar.set)
        self.transactions_labels_frame = Frame(self.transactions_canvas)
        self.transactions_canvas.create_window((0, 0), window=self.transactions_labels_frame, anchor="nw")

        self.add_transaction_button = Button(self.main_window, text="Add Transaction", bg=button_colour,
                                             font=("Comfortaa", 9), bd=0, relief="solid",
                                             command=lambda: self.go_to_transaction(self))
        self.add_transaction_button.grid(row=1, column=0, padx=10, pady=10)
        self.add_transaction_button.config(width="13")

        # Allows resizing of labels
        self.transactions_labels_frame.update_idletasks()
        # Change size of the box
        self.transactions_frame.config(width=225, height=100)
        # Set scrolling region
        self.transactions_canvas.config(scrollregion=self.transactions_canvas.bbox("all"))

        self.main_window.mainloop()

    @staticmethod
    def go_to_transaction(partner):
        TransactionWindow(partner)


class TransactionWindow:
    def __init__(self, partner):
        self.transaction_window = Toplevel()
        self.transaction_window.config(bg=background_colour)

        self.item_entry = Entry(self.transaction_window)
        self.item_entry.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = Entry(self.transaction_window)
        self.amount_entry.grid(row=1, column=0, padx=10, pady=10)
        self.enter_button = Button(self.transaction_window, text="Enter", bg=button_colour, font=("Comfortaa", 12),
                                   bd=1, relief="solid", command=lambda: self.save_history(partner))
        self.enter_button.grid(row=2, column=0, padx=10, pady=10)

    def save_history(self, partner):
        item = self.item_entry.get()
        amount = float(self.amount_entry.get())
        global row
        global transactions
        transactions += 1
        if transactions % 2 == 0:
            colour = "#d3d3d3"
        else:
            colour = "#f3f3f3"
        partner.transaction_background = Label(partner.transactions_labels_frame, bd=0, bg=colour)
        partner.transaction_background.grid(row=row, column=0, columnspan=2, ipady=3)
        partner.transaction_background.config(width=28)
        partner.transaction_label = Label(partner.transactions_labels_frame, text=item, font=("Comfortaa", 10), bd=0, bg=colour)
        partner.transaction_label.grid(row=row, column=0, sticky="w")
        partner.transaction_cost_label = Label(partner.transactions_labels_frame, text="-${:.2f} ".format(amount), font=("Comfortaa", 10), bd=0, bg=colour)
        partner.transaction_cost_label.grid(row=row, column=1, sticky="e")

        row += 1


# main routine
if __name__ == "__main__":
    MainWindow()
