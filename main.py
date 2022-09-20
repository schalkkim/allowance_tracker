# Kim Schalk
# 09/06/2022
# Main Program - Version 7 - Payment

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"
keypad_buttons_colour = "#efefef"

# Pin Numbers
parent_access_pin = "1234"
pin_number = ""

# Child Information
child_information = [["Nikau", "nikau_profile_icon.png", "102.00", "0000"],
                     ["Hana", "hana_profile_icon.png", "98.01", "4567"],
                     ["Tia", "tia_profile_icon.png", "56.00", "8765"]]

# Transaction Lists
for child in child_information:
    transaction = []
    child.append(transaction)

# Images
for child in child_information:
    child.append(Image.open(child[1]))

for child in child_information:
    child[5] = child[5].resize((45, 45))


# Keypad window
class Keypad:
    def __init__(self):
        self.keypad_window = Tk()
        self.keypad_window.title("Allowance Tracker")
        self.keypad_window.config(bg=background_colour)

        # Help Button
        help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.keypad_window, image=help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour,
                                  font=("Comfortaa", 12), bd=0, relief="solid", command=lambda: self.go_to_help())
        self.help_button.grid(row=0, column=2, pady=7, padx=7, sticky=E)

        # Password Label
        self.label_border = Frame(self.keypad_window, bg="black")
        self.label_border.grid(row=1, column=0, columnspan=3, pady=10)
        self.asterixes = StringVar()
        self.asterixes.set("")
        self.password_label = Label(self.label_border, textvariable=self.asterixes, fg="black",
                                    bg=keypad_buttons_colour,
                                    font=("Inconsolata", 12),
                                    bd=0)
        self.password_label.grid(row=0, column=0, ipadx=5, ipady=3, pady=1, padx=1)
        self.password_label.config(width=24)

        # Buttons 1-9 in a loop
        self.button_frame = Frame(self.keypad_window, bg=background_colour)
        self.button_frame.grid(row=2, column=0, columnspan=3, padx=15, pady=10)
        row = 0
        column = 0
        for button in range(1, 10):
            self.numbered_button = Button(self.button_frame, text=button, fg="black", bg=keypad_buttons_colour,
                                          font=("Comfortaa", 12), bd=1, relief="solid",
                                          command=lambda number=button: self.pin_number(number))
            if button == 4:
                row += 1
            elif button == 7:
                row += 1

            if button == 1:
                ipadx = 19
            else:
                ipadx = 17

            self.numbered_button.grid(row=row, column=column, ipadx=ipadx, padx=7, pady=7)
            column += 1
            if column == 3:
                column = 0

        # Other Buttons (Delete, 0, and Enter)
        self.delete_button = Button(self.button_frame, text="Delete", fg="black", bg=keypad_buttons_colour,
                                    font=("Comfortaa", 8), bd=1, relief="solid", command=lambda: self.delete())
        self.delete_button.grid(row=3, column=0, ipadx=7, ipady=7, padx=7, pady=7)
        self.zero_button = Button(self.button_frame, text="0", fg="black", bg=keypad_buttons_colour,
                                  font=("Comfortaa", 12), bd=1, relief="solid",
                                  command=lambda: self.pin_number("0"))
        self.zero_button.grid(row=3, column=1, ipadx=17, padx=7, pady=7)
        self.enter_button = Button(self.button_frame, text="Enter", fg="black", bg=keypad_buttons_colour,
                                   font=("Comfortaa", 8), bd=1, relief="solid", command=lambda: self.enter())
        self.enter_button.grid(row=3, column=2, ipadx=9, ipady=7, padx=7, pady=7)

        # End of Program
        self.keypad_window.mainloop()

    # Get pin number
    def pin_number(self, number):
        global pin_number
        pin_number += str(number)
        self.asterixes.set(self.asterixes.get() + "* ")

    def delete(self):
        global pin_number
        self.asterixes.set("")
        pin_number = ""

    def enter(self):
        global parent_access_pin
        global child_information
        global pin_number
        for child in child_information:
            if pin_number in child:
                self.keypad_window.destroy()
                Account(False, child)
        if pin_number == parent_access_pin:
            self.keypad_window.destroy()
            ChildSelection()
        else:
            self.delete()

    def go_to_help(self):
        HelpWindow(self)


class HelpWindow:
    def __init__(self, partner):
        self.help_window = Toplevel()
        self.help_window.config(bg=background_colour)

        partner.help_button.config(state=DISABLED)
        self.help_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(partner))

        # Components
        self.name_label = Label(self.help_window, text="Help", font=("Comfortaa", 25, "bold"), bg=background_colour)
        self.name_label.grid(row=0, column=0, padx=5, pady=(15, 10))

        self.information_frame = Frame(self.help_window)
        self.information_frame.grid(row=1, column=0, padx=20, pady=(0, 30), stick="nw")
        self.information_frame.grid_rowconfigure(0, weight=1)
        self.information_frame.grid_columnconfigure(0, weight=1)
        self.information_frame.grid_propagate(False)
        self.information_canvas = Canvas(self.information_frame, bg=button_colour)
        self.information_canvas.grid(row=0, column=0, sticky=NSEW)
        self.information_scrollbar = Scrollbar(self.information_frame, orient="vertical",
                                               command=self.information_canvas.yview)
        self.information_scrollbar.grid(row=0, column=1, sticky=NS)
        self.information_canvas.configure(yscrollcommand=self.information_scrollbar.set)
        self.information_labels_frame = Frame(self.information_canvas)
        self.information_canvas.create_window((0, 0), window=self.information_labels_frame, anchor="nw")

        information = ("To start enter your pin\n"
                       "\n"
                       "Choose the child who's account you \n"
                       "would like to view, if you only have\n"
                       "one child, you will go straight to\n"
                       "the accounts page.\n"
                       "\n"
                       "On the accounts page you can view\n"
                       "the amount of money the child has\n"
                       "and their previous transactions. You\n"
                       "can sort their transactions by month\n"
                       "by using the dropdown menu to choose\n"
                       "a month, or by using the arrows to\n"
                       "change months.\n"
                       "To add money to a child, push the\n"
                       "\"add payment\" button. This will take\n"
                       "you to a window where you can enter\n"
                       "the reason and the amount.\n"
                       "To remove money, push the \"add\n"
                       "transaction\" button. This will take\n"
                       "you to a window where you can add the\n"
                       "item they bought and the cost.\n"
                       "To export their previous transactions,\n"
                       "press the \"export\" button.")

        self.information_label = Label(self.information_labels_frame, text=information, bg=button_colour,
                                       font=("Comfortaa", 9), justify=LEFT)
        self.information_label.grid(row=0, column=0)

        # Allows resizing of labels
        self.information_labels_frame.update_idletasks()
        # Change size of the box
        self.information_frame.config(width=260, height=260)
        # Set scrolling region
        self.information_canvas.config(scrollregion=self.information_canvas.bbox("all"))

    def close_window(self, partner):
        self.help_window.destroy()
        partner.help_button.config(state=ACTIVE)


class Account:
    def __init__(self, access, child):
        self.account_window = Tk()
        self.account_window.title("Allowance Tracker")
        self.account_window.configure(bg=background_colour)

        if access:
            self.account_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window())

        # Profile Image
        child.append(ImageTk.PhotoImage(child[5]))
        self.image_panel = Label(self.account_window, image=child[-1], bg=background_colour)
        self.image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

        self.name_label = Label(self.account_window, text=child[0], font=("Comfortaa", 25, "bold"),
                                bg=background_colour)
        self.name_label.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="w")

        # Help Button
        self.help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.account_window, image=self.help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour, font=("Comfortaa", 12), bd=0, relief="solid",
                                  command=lambda: self.go_to_help())
        self.help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

        # Setting money amount as a variable
        self.money = StringVar()
        self.money.set("${:.2f}".format(float(child[2])))
        child.append(self.money)

        # Account Labels
        self.account_balance_label = Label(self.account_window, text="Account Balance:", bg=background_colour,
                                           font=("Comfortaa", 10))
        self.account_balance_label.grid(row=1, column=0, columnspan=3, pady=(5, 0))
        self.amount_label = Label(self.account_window, textvariable=child[-1], bg=background_colour,
                                  font=("Comfortaa", 22))
        self.amount_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))
        self.bonus_frame = Frame(self.account_window, bg=button_colour)
        self.bonus_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10))

        if float(child[2]) > 50:
            bonus = "{} is on track for a bonus!".format(child[0])
        else:
            bonus = "{} needs to earn money to get the bonus!".format(child[0])

        self.bonus_label1 = Label(self.bonus_frame, text=bonus, bg=button_colour, font=("Comfortaa", 9))
        self.bonus_label1.grid(row=0, column=0, padx=20, pady=(5, 0))
        self.bonus_label2 = Label(self.bonus_frame, text="Days until bonus: 46", bg=button_colour,
                                  font=("Comfortaa", 9, "italic"))
        self.bonus_label2.grid(row=1, column=0, padx=20, pady=(0, 5))

        # Transactions Components
        self.transactions_label = Label(self.account_window, text="Previous Transactions:", bg=background_colour,
                                        font=("Comfortaa", 10, "bold"))
        self.transactions_label.grid(row=4, column=0, columnspan=3, sticky=W, pady=5, padx=5)
        self.left_button = Button(self.account_window, text="ᐸ", bg=background_colour, font=("Comfortaa", 12), bd=0)
        self.left_button.grid(row=5, column=0, sticky=E)
        self.right_button = Button(self.account_window, text="ᐳ", bg=background_colour, font=("Comfortaa", 12), bd=0)
        self.right_button.grid(row=5, column=2, sticky=W)

        months = ["August", "July", "June", "May"]
        self.chosen_month = StringVar()
        self.chosen_month.set("Sort By Date")
        self.sort_by_date_dropdown = OptionMenu(self.account_window, self.chosen_month, *months)
        self.sort_by_date_dropdown.grid(row=5, column=1)
        self.sort_by_date_dropdown.config(bg=button_colour, font=("Comfortaa", 8), bd=1, relief="solid")

        # Past Transactions with Scrollbar
        self.transactions_frame = Frame(self.account_window)
        self.transactions_frame.grid(row=6, column=0, columnspan=3, padx=20, pady=(10, 15), stick="nw")
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

        row = 0
        transactions = 0
        for transaction in child[4]:
            transactions += 1
            if transactions % 2 == 0:
                colour = "#d3d3d3"
            else:
                colour = "#f3f3f3"
            self.transaction_background = Label(self.transactions_labels_frame, bd=0, bg=colour)
            self.transaction_background.grid(row=row, column=0, columnspan=2, ipady=3)
            self.transaction_background.config(width=28)
            self.transaction_label = Label(self.transactions_labels_frame, text=transaction[0], font=("Comfortaa", 10),
                                           bd=0, bg=colour)
            self.transaction_label.grid(row=row, column=0, sticky="w")
            self.transaction_cost_label = Label(self.transactions_labels_frame,
                                                text="${:.2f} ".format(float(transaction[1])),
                                                font=("Comfortaa", 10), bd=0, bg=colour)
            self.transaction_cost_label.grid(row=row, column=1, sticky="e")
            row += 1

        # Allows resizing of labels
        self.transactions_labels_frame.update_idletasks()
        # Change size of the box
        self.transactions_frame.config(width=225, height=100)
        # Set scrolling region
        self.transactions_canvas.config(scrollregion=self.transactions_canvas.bbox("all"))

        # Buttons
        self.button_frame = Frame(self.account_window, bg="black")
        self.button_frame.grid(row=7, column=0, columnspan=3, pady=(0, 20))
        self.add_transaction_button = Button(self.button_frame, text="Add Transaction", bg=button_colour,
                                             font=("Comfortaa", 9), bd=0, relief="solid",
                                             command=lambda: self.transaction(access, child, False))
        self.add_transaction_button.grid(row=0, column=0, padx=(1, 1), pady=(1, 1))
        self.add_transaction_button.config(width="13")

        if access:
            self.add_payment_button = Button(self.button_frame, text="Add Payment", bg=button_colour,
                                             font=("Comfortaa", 9), bd=0, relief="solid",
                                             command=lambda: self.transaction(True, child, True))
            self.add_payment_button.grid(row=0, column=1, padx=(0, 1), pady=(1, 1))
            self.add_payment_button.config(width="13")
            self.statistics_button = Button(self.button_frame, text="Statistics", bg=button_colour,
                                            font=("Comfortaa", 9), bd=0, relief="solid")
            self.statistics_button.grid(row=1, column=0, padx=(1, 1), pady=(0, 1))
            self.statistics_button.config(width="13", state=DISABLED)
            self.export_button = Button(self.button_frame, text="Export", bg=button_colour, font=("Comfortaa", 9), bd=0,
                                        relief="solid")
            self.export_button.grid(row=1, column=1, padx=(0, 1), pady=(0, 1))
            self.export_button.config(width="13")
        else:
            self.statistics_button = Button(self.button_frame, text="Statistics", bg=button_colour,
                                            font=("Comfortaa", 9), bd=0, relief="solid")
            self.statistics_button.grid(row=0, column=1, padx=(0, 1), pady=(1, 1))
            self.statistics_button.config(width="13", state=DISABLED)

        # End of Program
        self.account_window.mainloop()

    def go_to_help(self):
        HelpWindow(self)

    def transaction(self, access, child, payment):
        Transaction(self, access, child, payment)

    def close_window(self):
        self.account_window.destroy()
        ChildSelection()


class ChildSelection:
    def __init__(self):
        self.child_selection_window = Tk()
        self.child_selection_window.title("Allowance Tracker")
        self.child_selection_window.config(bg=background_colour)

        # Help Button
        self.help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.child_selection_window, image=self.help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour, font=("Comfortaa", 12), bd=0, relief="solid",
                                  command=lambda: self.go_to_help())
        self.help_button.grid(row=0, column=0, pady=7, padx=7, sticky=E)

        # Child buttons in a loop
        row = 1
        for child in child_information:
            # Resizing Images
            child.append(ImageTk.PhotoImage(child[5]))

            # Setting money amount as a variable
            self.money = StringVar()
            self.money.set("${:.2f}".format(float(child[2])))
            child.append(self.money)

            # Buttons
            self.button_frame = Frame(self.child_selection_window, bd=1, relief="solid", bg=button_colour)
            self.button_frame.grid(row=row, column=0, ipadx=3, padx=10, pady=5)
            text = "  {} - {}".format(child[0].capitalize(), child[-1].get())
            self.name_button = Button(self.button_frame, text=text, image=child[-2], compound=LEFT, fg="black",
                                      bg=button_colour, font=("Comfortaa", 12), bd=0, relief="solid", anchor="w",
                                      command=lambda name=child[0]: self.go_to_account(name))
            self.name_button.grid(row=0, column=0, pady=5, padx=10, ipady=4)
            self.name_button.config(width=185)
            if child == child_information[-1]:
                self.button_frame.grid(pady=(5, 20))
            row += 1

        # End of Program
        self.child_selection_window.mainloop()

    def go_to_help(self):
        HelpWindow(self)

    def go_to_account(self, name):
        for child in child_information:
            if name in child:
                person = child
        self.child_selection_window.destroy()
        Account(True, person)


class Transaction:
    def __init__(self, partner, access, child, payment):
        self.transaction_window = Toplevel()
        self.transaction_window.config(bg=background_colour)

        child.append(ImageTk.PhotoImage(child[5]))
        self.image_panel = Label(self.transaction_window, image=child[-1], bg=background_colour)
        self.image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

        if payment:
            title = "Payment"
        else:
            title = "Transaction"

        self.name_label = Label(self.transaction_window, text=title, font=("Comfortaa", 25, "bold"),
                                bg=background_colour)
        self.name_label.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="w")

        # Help Button
        help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.transaction_window, image=help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour,
                                  font=("Comfortaa", 12), bd=0, relief="solid")
        self.help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

        # Input Labels and Entries
        if payment:
            reason = "Reason:"
        else:
            reason = "Item:"
        self.item_label = Label(self.transaction_window, text=reason, bg=background_colour,
                                font=("Comfortaa", 12, "bold"))
        self.item_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 10))
        self.item_entry = Entry(self.transaction_window, font=("Comfortaa", 10), bd=1)
        self.item_entry.grid(row=2, column=0, columnspan=3, padx=15)
        self.item_entry.config(width=40)
        self.cost_label = Label(self.transaction_window, text="Amount:", bg=background_colour,
                                font=("Comfortaa", 12, "bold"))
        self.cost_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=20, pady=(20, 10))
        self.cost_entry = Entry(self.transaction_window, font=("Comfortaa", 10), bd=1)
        self.cost_entry.grid(row=4, column=0, columnspan=3, padx=15)
        self.cost_entry.config(width=40)

        self.enter_button = Button(self.transaction_window, text="Enter", bg=button_colour, font=("Comfortaa", 12),
                                   bd=1, relief="solid",
                                   command=lambda: self.add_transaction(partner, access, child, payment))
        self.enter_button.grid(row=5, column=0, columnspan=3, pady=(30, 20), ipadx=25)

    def add_transaction(self, partner, access, child, payment):
        cost = float(self.cost_entry.get())
        if payment:
            child[2] = str(float(child[2]) + cost)
            transaction1 = [self.item_entry.get(), "+" + self.cost_entry.get()]
        else:
            child[2] = str(float(child[2]) - cost)
            transaction1 = [self.item_entry.get(), "-" + self.cost_entry.get()]
        child[4].append(transaction1)
        self.transaction_window.destroy()
        partner.account_window.destroy()
        Account(access, child)


# main routine
if __name__ == "__main__":
    Keypad()
