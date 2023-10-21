from tkinter import*


root = Tk()
# Assiging title to check boxes
root.title("Building CheckBoxes")
# assigning the geometry to tkinter window
root.geometry("500x500")

#Declearing variable to be used in checkboxes
var = StringVar()

# defining a class with click status which will get what is the checkbox after clicking
def change_click_status():
    my_label = Label(root, text=var.get()).pack()

# having a checkbutton defined
check_box = Checkbutton(root, text="Check this box", variable=var, onvalue="ON", offvalue="Off")
check_box.deselect()
check_box.pack()

# Creating a button which user click upon selecting everything to get an output
my_button = Button(root, text="Click Me to get get the results", command=change_click_status)
my_button.pack()

root.mainloop()

# can be applied in where a person s required to take text to ascertain qualification