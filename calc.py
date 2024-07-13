from tkinter import *
from enum import Enum

class Functions(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    NON = 5

currentNumber = 0
memNumber = 0
answer = 0
func = Functions.NON

# Number Buttons
def click_number(number: int):
    global currentNumber
    currentNumber = currentNumber * 10 + number
    update_display()

# Function Buttons
def click_function(function: Functions):
    global func, memNumber, currentNumber
    func = function
    memNumber = currentNumber
    currentNumber = 0
    update_display()

# Equals Button
def click_equals():
    global answer, func, memNumber, currentNumber
    if func == Functions.ADD:
        answer = memNumber + currentNumber
    elif func == Functions.SUB:
        answer = memNumber - currentNumber
    elif func == Functions.MUL:
        answer = memNumber * currentNumber
    elif func == Functions.DIV:
        answer = memNumber / currentNumber if currentNumber != 0 else 0  # Avoid division by zero
    else:
        answer = currentNumber
    
    currentNumber = answer
    func = Functions.NON
    update_display()

def update_display():
    screen.config(text=str(currentNumber))

# GUI
root = Tk()

screen = Label(root, text="0", bg="#DDDDDD", fg="#222222", font=("Arial", 24))
screen.grid(column=0, row=0, columnspan=4, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('X', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('=', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit():
        Button(root, text=text, padx=20, pady=20, command=lambda x=int(text): click_number(x)).grid(row=row, column=col)
    elif text in '+-X/':
        func_map = {'+': Functions.ADD, '-': Functions.SUB, 'X': Functions.MUL, '/': Functions.DIV}
        Button(root, text=text, padx=20, pady=20, command=lambda x=func_map[text]: click_function(x)).grid(row=row, column=col)
    elif text == '=':
        Button(root, text=text, padx=20, pady=20, command=click_equals).grid(row=row, column=col)
    elif text == 'C':
        Button(root, text=text, padx=20, pady=20, command=lambda: (globals().update(currentNumber=0, memNumber=0, answer=0, func=Functions.NON), update_display())).grid(row=row, column=col)

root.mainloop()