# Kim Schalk
# 09/06/2022
# Main Program - Version 3 - Child Access

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

# Images
nikau_image = Image.open("nikau_profile_icon.png")
tia_image = Image.open("tia_profile_icon.png")
hana_image = Image.open("hana_profile_icon.png")

# Child Information
child_information = [["Nikau", "nikau_profile_icon.png", 98.00, nikau_image, "0000"],
                     ["Hana", "hana_profile_icon.png", 98.00, hana_image, "4567"],
                     ["Tia", "tia_profile_icon.png", 98.00, tia_image, "8765"]]


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
                                  font=("Comfortaa", 12), bd=0, relief="solid", command=lambda: self.go_to_help(self))
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

        # Buttons 1-9
        self.button_frame = Frame(self.keypad_window, bg=background_colour)
        self.button_frame.grid(row=2, column=0, columnspan=3, padx=15, pady=10)

        self.one_button = Button(self.button_frame, text="1", fg="black", bg=keypad_buttons_colour,
                                 font=("Comfortaa", 12), bd=1, relief="solid",
                                 command=lambda: self.pin_number(self, "1"))
        self.one_button.grid(row=0, column=0, ipadx=19, padx=7, pady=7)
        self.two_button = Button(self.button_frame, text="2", fg="black", bg=keypad_buttons_colour,
                                 font=("Comfortaa", 12), bd=1, relief="solid",
                                 command=lambda: self.pin_number(self, "2"))
        self.two_button.grid(row=0, column=1, ipadx=17, padx=7, pady=7)
        self.three_button = Button(self.button_frame, text="3", fg="black", bg=keypad_buttons_colour,
                                   font=("Comfortaa", 12), bd=1, relief="solid",
                                   command=lambda: self.pin_number(self, "3"))
        self.three_button.grid(row=0, column=2, ipadx=17, padx=7, pady=7)
        self.four_button = Button(self.button_frame, text="4", fg="black", bg=keypad_buttons_colour,
                                  font=("Comfortaa", 12), bd=1, relief="solid",
                                  command=lambda: self.pin_number(self, "4"))
        self.four_button.grid(row=1, column=0, ipadx=17, padx=7, pady=7)
        self.five_button = Button(self.button_frame, text="5", fg="black", bg=keypad_buttons_colour,
                                  font=("Comfortaa", 12), bd=1, relief="solid",
                                  command=lambda: self.pin_number(self, "5"))
        self.five_button.grid(row=1, column=1, ipadx=17, padx=7, pady=7)
        self.six_button = Button(self.button_frame, text="6", fg="black", bg=keypad_buttons_colour,
                                 font=("Comfortaa", 12), bd=1, relief="solid",
                                 command=lambda: self.pin_number(self, "6"))
        self.six_button.grid(row=1, column=2, ipadx=17, padx=7, pady=7)
        self.seven_button = Button(self.button_frame, text="7", fg="black", bg=keypad_buttons_colour,
                                   font=("Comfortaa", 12), bd=1, relief="solid",
                                   command=lambda: self.pin_number(self, "7"))
        self.seven_button.grid(row=2, column=0, ipadx=17, padx=7, pady=7)
        self.eight_button = Button(self.button_frame, text="8", fg="black", bg=keypad_buttons_colour,
                                   font=("Comfortaa", 12), bd=1, relief="solid",
                                   command=lambda: self.pin_number(self, "8"))
        self.eight_button.grid(row=2, column=1, ipadx=17, padx=7, pady=7)
        self.nine_button = Button(self.button_frame, text="9", fg="black", bg=keypad_buttons_colour,
                                  font=("Comfortaa", 12), bd=1, relief="solid",
                                  command=lambda: self.pin_number(self, "9"))
        self.nine_button.grid(row=2, column=2, ipadx=17, padx=7, pady=7)

        # Other Buttons (Delete, 0, and Enter)
        self.delete_button = Button(self.button_frame, text="Delete", fg="black", bg=keypad_buttons_colour,
                                    font=("Comfortaa", 8), bd=1, relief="solid", command=lambda: self.delete(self))
        self.delete_button.grid(row=3, column=0, ipadx=7, ipady=7, padx=7, pady=7)
        self.zero_button = Button(self.button_frame, text="0", fg="black", bg=keypad_buttons_colour,
                                  font=("Comfortaa", 12), bd=1, relief="solid",
                                  command=lambda: self.pin_number(self, "0"))
        self.zero_button.grid(row=3, column=1, ipadx=17, padx=7, pady=7)
        self.enter_button = Button(self.button_frame, text="Enter", fg="black", bg=keypad_buttons_colour,
                                   font=("Comfortaa", 8), bd=1, relief="solid", command=lambda: self.enter(self))
        self.enter_button.grid(row=3, column=2, ipadx=9, ipady=7, padx=7, pady=7)

        # End of Program
        self.keypad_window.mainloop()

    # Get pin number
    @staticmethod
    def pin_number(partner, number):
        global pin_number
        pin_number += number
        print(pin_number)
        partner.asterixes.set(partner.asterixes.get() + "* ")

    @staticmethod
    def delete(partner):
        global pin_number
        partner.asterixes.set("")
        pin_number = ""

    def enter(self, partner):
        global parent_access_pin
        global child_information
        global pin_number
        for child in child_information:
            if pin_number in child:
                self.access = False
                print(child)
                self.child = child
                partner.keypad_window.destroy()
                Account(self)
        if pin_number == parent_access_pin:
            self.access = True
            partner.keypad_window.destroy()
            Account(self)
        else:
            self.delete(partner)

    @staticmethod
    def go_to_help(partner):
        HelpWindow(partner)


class HelpWindow:
    def __init__(self, partner):
        self.help_window = Toplevel()
        self.help_window.config(bg=background_colour)

        partner.help_button.config(state=DISABLED)
        self.help_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(self, partner))

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

    @staticmethod
    def close_window(partner, partner2):
        partner.help_window.destroy()
        partner2.help_button.config(state=ACTIVE)


class Account:
    def __init__(self, partner):
        self.account_window = Tk()
        self.account_window.title("Allowance Tracker")
        self.account_window.configure(bg=background_colour)

        # Profile Image
        self.child_image = partner.child[3].resize((50, 50))
        self.child_image = ImageTk.PhotoImage(self.child_image)
        self.image_panel = Label(self.account_window, image=self.child_image, bg=background_colour)
        self.image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

        self.name_label = Label(self.account_window, text=partner.child[0], font=("Comfortaa", 25, "bold"), bg=background_colour)
        self.name_label.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="w")

        # Help Button
        help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.account_window, image=help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour, font=("Comfortaa", 12), bd=0, relief="solid",
                                  command=lambda: self.go_to_help(self))
        self.help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

        # Account Labels
        self.account_balance_label = Label(self.account_window, text="Account Balance:", bg=background_colour,
                                           font=("Comfortaa", 10))
        self.account_balance_label.grid(row=1, column=0, columnspan=3, pady=(5, 0))
        self.amount_label = Label(self.account_window, text="${:.2f}".format(partner.child[2]), bg=background_colour,
                                  font=("Comfortaa", 22))
        self.amount_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))
        self.bonus_frame = Frame(self.account_window, bg=button_colour)
        self.bonus_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10))

        if partner.child[2] > 50:
            bonus = "{} is on track for a bonus!".format(partner.child[0])
        else:
            bonus = "{} needs to earn money to get the bonus!".format(partner.child[0])

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
        for transaction in range(1, 6):
            if transaction % 2 == 0:
                colour = "#d3d3d3"
            else:
                colour = "#f3f3f3"
            self.transaction_background = Label(self.transactions_labels_frame, bd=0, bg=colour)
            self.transaction_background.grid(row=row, column=0, columnspan=2, ipady=3)
            self.transaction_background.config(width=28)
            self.transaction_label = Label(self.transactions_labels_frame, text="Tennis Shoes", font=("Comfortaa", 10),
                                           bd=0, bg=colour)
            self.transaction_label.grid(row=row, column=0, sticky="w")
            self.transaction_cost_label = Label(self.transactions_labels_frame, text="-$123.00 ",
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
                                             font=("Comfortaa", 9), bd=0, relief="solid")
        self.add_transaction_button.grid(row=0, column=0, padx=(1, 1), pady=(1, 1))
        self.add_transaction_button.config(width="13")

        if partner.access:
            self.add_payment_button = Button(self.button_frame, text="Add Payment", bg=button_colour,
                                             font=("Comfortaa", 9), bd=0, relief="solid")
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

    @staticmethod
    def go_to_help(partner):
        HelpWindow(partner)


# main routine
if __name__ == "__main__":
    Keypad()
