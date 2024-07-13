from tkinter import * 

root = Tk()

e = Entry(root, width=100, fg="#FFFFFF", bg="#FF0011")
e.pack()
e.get()
e.insert(0, "Enter your name")

def my_click():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text='Enter your name', padx=50, pady=50, command=my_click, fg="#FF0000")
myButton.pack()

root.mainloop()