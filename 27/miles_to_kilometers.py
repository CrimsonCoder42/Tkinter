from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

def miles_to_kilo():
    new_text = int(input.get())
    conversion = new_text * 1.60934
    total_label.config(text=conversion)

miles_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
miles_label.config(text="Miles")
miles_label.grid(column=3, row=2)

KM_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
KM_label.config(text="KM")
KM_label.grid(column=3, row=3)

total_label = Label(text="", font=("Arial", 24, "bold"))

total_label.grid(column=3, row=3)

button = Button(text="Calculate", command=miles_to_kilo)
button.grid(column=1, row=1)

input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)

window.mainloop()