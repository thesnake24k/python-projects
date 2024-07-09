import tkinter
window = tkinter.Tk()
window.minsize(600, 600)
window.title("learning tkinter")

# create a Label
my_label = tkinter.Label(text="I'm so excited to learn tkinter", font=("Arial", 8, "bold"))


my_label.grid(column=0, row=0)
# 2 different way to change the text(or any other argument) inside a label
my_label["text"] = "New text"
my_label.config(text="Very new text")


# Create a button
def button_clicked():
    print("I got clicked")
    my_label.config(text="I got clicked")
    my_text = text_input.get()
    input_value.config(text=my_text)


button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="click me", command=button_clicked)
button2.grid(column=2, row=0)

# Create an Entry
text_input = tkinter.Entry(width=100)
text_input.grid(column=3, row=2)


# another label for text input
input_value = tkinter.Label(text="", font=("Arial", 20, "italic"))


window.mainloop()
