from tkinter import *


def b_cal():
    ml = mile_input.get()
    k = round(float(ml) * 1.60934)
    result.config(text=k)


window = Tk()
window.minsize(width=300, height=200)
window.config(pady=50, padx=50)
is_equal = Label(text="is equal to")
mile_input = Entry(width=20)
miles = Label(text="Miles")
km = Label(text="Km")
result = Label(text="")
but = Button(text="Calculate", command=b_cal)

is_equal.grid(column=0, row=1)
mile_input.grid(column=1, row=0)
miles.grid(column=2, row=0)
km.grid(column=2, row=1)
but.grid(row=2, column=1)
result.grid(row=1, column=1)
window.mainloop()
