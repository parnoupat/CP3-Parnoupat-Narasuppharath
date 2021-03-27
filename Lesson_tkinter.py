from tkinter import *

def sayHelloWorld():
    print("Hello world")

mainWindow = Tk()
button = Button(mainWindow,text = "Click me", command = sayHelloWorld, width=20).grid(row=0, column=0)
button2 = Button(mainWindow,text = "Click me", command = sayHelloWorld).grid(row=1, column=1)
label = Label(mainWindow, text = "Hello World", width=20 , font=("Helvetica",76),anchor=W).grid(row=0,column=1)
# button.place(x = 50, y=20)
# button2.place(x = 50, y=50)
mainWindow.mainloop()
