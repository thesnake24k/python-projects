from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email_user = email_user_input.get()
    password = password_input.get()
    if website == "" or email_user == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are detail entered: \n Email: {email_user}\n"
                                                              f"Password: {password}\n Is it ok to save")
        if is_ok:
            with open("info.txt", mode="a") as file:
                file.write(f"{website} | {email_user} | {password}\n")
                website_input.delete(0, END)
                email_user_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


def add():
    pass


window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

website_text = Label(text="Website:")
email_user_text = Label(text="Email/Username:")
password_text = Label(text="Password:")
website_input = Entry(width=45)
email_user_input = Entry(width=45)
password_input = Entry(width=34)
button_generate = Button(text="Generate", command=generate, width=8)
button_add = Button(text="Add", width=38, command=save)

website_input.focus()
email_user_input.insert(0, "med.yuri@gmail.com")

canvas.grid(row=0, column=1)
website_text.grid(row=1, column=0)
email_user_text.grid(row=2, column=0)
password_text.grid(row=3, column=0)
website_input.grid(row=1, column=1, columnspan=2)
email_user_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)
button_add.grid(row=4, column=1, columnspan=2)
button_generate.grid(row=3, column=2)

window.mainloop()
