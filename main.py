# Kim Schalk
# 09/06/2022
# Main Program - Version 1 - Keypad

# Import Libraries
from tkinter import *
from matplotlib import font_manager

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"
keypad_buttons_colour = "#efefef"

# Pin Numbers
parent_access_pin = "1234"
child_access_pins = ["0000", "4587", "6534"]
pin_number = ""


# Keypad window
class Keypad:
    def __init__(self):
        self.keypad_window = Tk()
        self.keypad_window.title("Allowance Tracker")
        self.keypad_window.config(bg=background_colour)

        # Help Button
        self.help_image = PhotoImage(file="help_image.png")
        self.help_button = Button(self.keypad_window, image=self.help_image, fg="black", bg=background_colour,
                                  activebackground=background_colour,
                                  font=("Comfortaa", 12), bd=0, relief="solid")
        self.help_button.grid(row=0, column=2, pady=7, padx=7, sticky=E)

        # Password Label
        self.label_border = Frame(self.keypad_window, bg="black")
        self.label_border.grid(row=1, column=0, columnspan=3, pady=10)
        self.asterixes = StringVar()
        self.asterixes.set("")
        self.password_label = Label(self.label_border, textvariable=self.asterixes, fg="black", bg=keypad_buttons_colour,
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

    def delete(self, partner):
        global pin_number
        partner.asterixes.set("")
        pin_number = ""

    def enter(self, partner):
        global parent_access_pin
        global child_access_pins
        global pin_number
        if pin_number in child_access_pins:
            self.access = False
            print(self.access)
        elif pin_number == parent_access_pin:
            self.access = True
            print(self.access)
        else:
            self.delete(partner)


# main routine
if __name__ == "__main__":
    Keypad()
