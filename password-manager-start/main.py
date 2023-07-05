from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_TYPE = "Courier"
FONT_SIZE = 15

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_file():
    filename = "data.txt"
    entries = [website_input.get(), email_user_input.get(), password_input.get()]
    content = " | ".join(entries)

    if len(website_input.get()) < 1 or len(password_input.get()) < 1:
       return messagebox.showinfo("Information", "Please make sure all info is entered.")

    is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: "
                                                              f"\nEmail: {email_user_input.get()}"
                                                              f"\nPassword: {password_input.get()}"
                           )


    if is_ok:
        with open(filename, "a") as file:
            file.write(content + "\n")

        website_input.delete(0, 'end')
        password_input.delete(0, 'end')



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


# labels
website_label = Label(text="Website:",font=(FONT_TYPE, FONT_SIZE))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:",font=(FONT_TYPE, FONT_SIZE))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:",font=(FONT_TYPE, FONT_SIZE))
password_label.grid(column=0, row=3)

# input boxes

website_input = Entry(width=35)
print(website_input.get())
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_input.focus()


email_user_input = Entry(width=35)
print(email_user_input.get())
email_user_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_user_input.insert(0, "nostro37@gmail.com")

password_input = Entry(width=21)
print(password_input.get())
password_input.grid(column=1, row=3)

# buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightthickness=0, command=write_to_file)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()