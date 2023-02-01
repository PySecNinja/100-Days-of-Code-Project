from tkinter import *

def calculate_button():
    miles_inputted = input_for_miles.get()
    conversion = round(float(miles_inputted) * 1.609)
    km_conversion.config(text=conversion)
    
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Labels
miles_label =  Label(text="Miles")
miles_label.grid(column=4, row=0)

km_label = Label(text="Kilometers")
km_label.grid(column=4, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_conversion = Label(text="0")
km_conversion.grid(column=3, row=1)

# Entry
input_for_miles = Entry(width=7, justify=CENTER)
input_for_miles.grid(column=3, row=0)
input_for_miles.focus()

# Button
button = Button(text="Calculate", command=calculate_button)
button.grid(column=3, row=3)

window.mainloop()