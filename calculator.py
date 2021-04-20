from tkinter import *
from time import sleep
root = Tk()                                                     # Create a window
root.title('Calculator')                                        # Give Title
e = Entry(root, width=40, borderwidth=5)                        # Give an input column
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)         # Put it on root window
e.insert(0, '0')                                                # entry column will have 0
current_number = 0


# Function for command of buttons


def button_func(number):                                            # For getting number on screen
    current = e.get()
    e.delete(0, END)
    e.insert(0, float(current)*10+int(number))


def button_clear_func():                                            # Used for Clear Button
    e.delete(0, END)
    e.insert(0, '0')


def button_add_func():                                              # For addition
    f_num = e.get()
    global current_number
    global math
    math = 'add'
    current_number = f_num
    e.delete(0, END)
    e.insert(0, '0')


def button_sub_func():
    f_num = e.get()
    global current_number
    global math
    math = 'sub'
    current_number = f_num
    e.delete(0, END)
    e.insert(0, '0')


def button_mul_func():
    f_num = e.get()
    global current_number
    global math
    math = 'mul'
    current_number = f_num
    e.delete(0, END)
    e.insert(0, '0')


def button_div_func():
    f_num = e.get()
    global current_number
    global math
    math = 'div'
    current_number = f_num
    e.delete(0, END)
    e.insert(0, '0')


def button_equal_func():                                            # After pressing equal button
    b = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, float(current_number)+float(b))
    if math == 'sub':
        e.insert(0, float(current_number) - float(b))
    if math == 'mul':
        e.insert(0, float(b) * float(current_number))
    if math == 'div':
        try:
            e.insert(0, float(current_number) / float(b))
        except ZeroDivisionError:
            error_label = Label(root, text='ERROR')
            error_label.grid(row=7, column=0, columnspan=3)
            error_label.after(3000, error_label.destroy)
            button_clear_func()


def button_square_func():
    square_number = e.get()
    e.delete(0, END)
    e.insert(0, float(float(square_number)**2))


# Create Buttons
button_1 = Button(root, padx=40, pady=25, text='1', command=lambda: button_func(1))
button_2 = Button(root, padx=40, pady=25, text='2', command=lambda: button_func(2))
button_3 = Button(root, padx=40, pady=25, text='3', command=lambda: button_func(3))
button_4 = Button(root, padx=40, pady=25, text='4', command=lambda: button_func(4))
button_5 = Button(root, padx=40, pady=25, text='5', command=lambda: button_func(5))
button_6 = Button(root, padx=40, pady=25, text='6', command=lambda: button_func(6))
button_7 = Button(root, padx=40, pady=25, text='7', command=lambda: button_func(7))
button_8 = Button(root, padx=40, pady=25, text='8', command=lambda: button_func(8))
button_9 = Button(root, padx=40, pady=25, text='9', command=lambda: button_func(9))
button_0 = Button(root, padx=40, pady=25, text='0', command=lambda: button_func(0))
button_clear = Button(root, padx=30, pady=25, text='Clear', command=button_clear_func)
button_add = Button(root, padx=40, pady=24, text='+', command=button_add_func)
button_equal = Button(root, padx=91, pady=25, text='=', command=button_equal_func)
button_square = Button(root, padx=40, pady=25, text='Square', command=button_square_func)
button_sub = Button(root, padx=40, pady=24, text='-', command=button_sub_func)
button_mul = Button(root, padx=40, pady=24, text='*', command=button_mul_func)
button_div = Button(root, padx=40, pady=24, text='/', command=button_div_func)

# Put all buttons on window

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_square.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)


root.mainloop()
