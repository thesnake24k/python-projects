# import tkinter
# window = tkinter.Tk()
# window.minsize(600, 600)
# window.title("learning tkinter")
#
# # create a Label
# my_label = tkinter.Label(text="I'm so excited to learn tkinter", font=("Arial", 24, "bold"))
#
#
# my_label.pack(side="top")
# # 2 different way to change the text(or any other argument) inside a label
# my_label["text"] = "New text"
# my_label.config(text="Very new text")
#
#
# # Create a button
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text="I got clicked")
#     my_text = text_input.get()
#     input_value.config(text=my_text)
#
#
# button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
#
#
# # Create an Entry
# text_input = tkinter.Entry(width=100)
# text_input.pack()
#
#
# # another label for text input
# input_value = tkinter.Label(text="", font=("Arial", 20, "italic"))
# input_value.pack()
#
# window.mainloop()

from tkinter import *


# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
