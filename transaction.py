# Kim Schalk
# 30/08/2022
# Transaction - Version 1

# Import Libraries
from tkinter import *
from matplotlib import font_manager

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"

# Variable to hold amount of money
amount = 123


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.config(bg=background_colour)
        self.main_window.title("Allowance Tracker")
        self.main_window.grid()

        self.money = StringVar()
        self.money.set("$123.00")

        self.money_label = Label(self.main_window, textvariable=self.money, bg=background_colour,
                                 font=("Comfortaa", 22))
        self.money_label.grid(row=0, column=0, padx=10, pady=10)

        self.add_transaction_button = Button(self.main_window, text="Add Transaction", bg=button_colour,
                                             font=("Comfortaa", 9), bd=0, relief="solid",
                                             command=lambda: self.go_to_transaction(self))
        self.add_transaction_button.grid(row=1, column=0, padx=10, pady=10)
        self.add_transaction_button.config(width="13")

        self.main_window.mainloop()

    @staticmethod
    def go_to_transaction(partner):
        Transaction()


class Transaction:
    def __init__(self):
        self.transaction_window = Toplevel()
        self.transaction_window.config(bg=background_colour)

        self.amount_entry = Entry(self.transaction_window, font=("Comfortaa", 10), bd=1)
        self.amount_entry.grid(row=0, column=0, padx=10, pady=10)

        self.enter_button = Button(self.transaction_window, text="Enter", bg=button_colour, font=("Comfortaa", 12),
                                   bd=1, relief="solid", command=self.decrease_amount)
        self.enter_button.grid(row=1, column=0, padx=10, pady=10)

    def decrease_amount(self):
        entry = int(self.amount_entry.get())
        global amount
        amount -= entry
        print(amount)


# main routine
if __name__ == "__main__":
    MainWindow()
