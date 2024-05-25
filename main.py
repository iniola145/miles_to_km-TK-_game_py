from tkinter import *


def calculate():
    input_value = float(input_num.get())
    km = round(input_value * 1.609)
    label_2.config(text=km)


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=30, pady=30)

# Label
label = Label()
label.config(text="is equal to")
label.grid(row=1, column=0)

# Entry
input_num = Entry(width=7)
input_num.insert(END, str(0))
input_num.grid(row=0, column=1)

# Label2
label_2 = Label()
label_2.config(text="0")
label_2.grid(row=1, column=1)

# Button
calculate_button = Button()
calculate_button.config(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

# Label3
label_3 = Label()
label_3.config(text="Miles")
label_3.grid(row=0, column=2)

# Label4
label_4 = Label()
label_4.config(text="Km")
label_4.grid(row=1, column=2)

window.mainloop()
