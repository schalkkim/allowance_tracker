# Kim Schalk
# 25/08/2022
# Statistics Window Design - Version 1

# Import Libraries
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Access downloaded fonts on computer
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

# Colours used in the program
background_colour = "#93c47d"
button_colour = "#d9ead3"

# Child Images
hana_image = Image.open("hana_profile_icon.png")

# Child Names
children = ["Nikau", "Hana", "Tia"]

root = Tk()
root.title("Allowance Tracker")
root.configure(bg=background_colour)

# Profile Image
hana_image = hana_image.resize((50, 50))
hana_image = ImageTk.PhotoImage(hana_image)
image_panel = Label(root, image=hana_image, bg=background_colour)
image_panel.grid(row=0, column=0, padx=5, pady=(20, 0))

name_label = Label(root, text="Statistics", font=("Comfortaa", 25, "bold"), bg=background_colour)
name_label.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="w")

# Help Button
help_image = PhotoImage(file="help_image.png")
help_button = Button(root, image=help_image, fg="black", bg=background_colour, activebackground=background_colour,
                     font=("Comfortaa", 12), bd=0, relief="solid")
help_button.grid(row=0, column=2, pady=7, padx=7, sticky=NE)

# Graph Information
data2 = {'Month': ["Jan", "Feb", "March", "April", "May"],
         'Amount_Of_Money': [24, 36, 12, 7, 63]
         }
df2 = DataFrame(data2, columns=['Month', 'Amount_Of_Money'])
figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().grid(row=1, column=0, columnspan=3)
df2 = df2[['Month', 'Amount_Of_Money']].groupby('Month').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)

# End of Program
root.mainloop()
