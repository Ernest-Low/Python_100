# Day 27 - Tkinter Miles to KM Basic GUI
# Tried to use frames.. maybe next time.
# Seems very similar to CSS Flexbox

from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20)

# frame1 = Frame(window)
# frame1.grid(column = 0, row = 1)
# frame2 = Frame(window)
# frame2.grid(column = 1, row = 0)
# frame3 = Frame(window)
# frame3.grid(column = 2, row = 0)

def calculate () :
    try :
        miles = int(miles_entry.get())
        calculated = miles * 1.609
        km_reveal.config(text = calculated)
    except :
        km_reveal.config(text = "Invalid value")



miles_text = Label(text = "Miles", font = ("Arial", 18, "normal"))
miles_text.grid(column = 2, row = 0)
miles_text.config(padx = 15, pady = 5)
equal_to = Label(text = "is equal to", font = ("Arial", 18, "normal"))
equal_to.grid(column = 0, row = 1)
equal_to.config(padx = 15, pady = 5)
km_text = Label(text = "Km", font = ("Arial", 18, "normal"))
km_text.grid(column = 2, row = 1)
km_text.config(padx = 15, pady = 5)

miles_entry = Entry(width=20)
miles_entry.focus()
miles_entry.grid(column = 1, row = 0)

km_reveal = Label(text = "0", font = ("Arial", 18, "normal"))
km_reveal.grid(column = 1, row = 1)
km_reveal.config(padx = 0, pady = 5)




button = Button(text = "Calculate", command = calculate)
button.grid(column = 1, row = 3)
button.config(padx = 5, pady = 5)



# for widget in frame1.winfo_children() :
#     widget.grid(padx = 0, pady = 5)
# for widget in frame2.winfo_children() :
#     widget.grid(padx = 0, pady = 5)
# for widget in frame3.winfo_children() :
#     widget.grid(padx = 0, pady = 5)

window.mainloop()