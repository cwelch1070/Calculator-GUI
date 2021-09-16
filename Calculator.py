#https://www.youtube.com/watch?v=YXPyB4XeYLA
#stoped at 1:16:31
from tkinter import*
from typing import Match

root = Tk()
#Changes name at the top when window opens
root.title("Simple Calculator")

#Text back size
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Function to tell the buttons with the numbers what to do when clicked
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#Function to tell the clear button what to do  
def button_clear():
    e.delete(0, END)

#function to tell the add button what to do 
def button_add():
    first_number = e.get()
    global f_num
    global math 
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math 
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math 
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_subtract():
    first_number = e.get()
    global f_num
    global math 
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)
    

#Funtion to tell the equal button what to do
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if(math == "addition"):
         e.insert(0, f_num + int(second_number))
    
    if(math == "multiplication"):
         e.insert(0, f_num * int(second_number))
         
    if(math == "divide"):
         e.insert(0, f_num / int(second_number))
         
    if(math == "subtract"):
         e.insert(0, f_num - int(second_number))

#customizes each button and pass the specific data through that each is intended for
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
#Customizes the non number buttons. They do not need lambda because they are not passing data 2 ways only 1
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_multiply = Button(root, text="x", padx=39, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=39, pady=20, command=button_divide)
button_subtract = Button(root, text="-", padx=39, pady=20, command=button_subtract)

#Decides the postion where each button is located on the screen to make look like a calculator
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

button_clear.grid(row=5, column=0, columnspan=2)
button_add.grid(row=4, column=1)
button_subtract.grid(row=6, column=2)
button_multiply.grid(row=4, column=2)
button_divide.grid(row=5, column=2)
button_equal.grid(row=6, column=0, columnspan=2)

#main loop to keep window up on screen
root.mainloop()