# simple window creation
from tkinter import *


# create window
# root = Tk()

# newFrame = Frame(root)
# newFrame.pack()
#
# otherFrame = Frame(root)
# otherFrame.pack(side=BOTTOM)
#
# button1 = Button(newFrame, text="Click here", fg="Red")
# button2 = Button(otherFrame, text="Click here", fg="Blue")
#
# button1.pack()
# button2.pack()

####grid format
# label1 = Label(root, text="First Name")
# label2 = Label(root, text="Last Name")
#
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)
#
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)

#####self adjusting widgets
# to fit to window

# label1 = Label(root, text="First", bg="Red", fg="White")
# label1.pack(fill=X) #autoadjusting label width
#
# label2 = Label(root, text="Second", bg="Blue", fg="Green")
# label2.pack(side=LEFT,fill=Y)


#####Handling button clicks
# def doSomething():
#     print("You clicked the button")
#
# button1 = Button(root, text="Click here", command=doSomething)
# button1.pack()

####Using classes

class myButtons:
    def __init__(self, rootOne):
        frame = Frame(rootOne)
        frame.pack()

        self.buttonPrint = Button(frame, text="Click here", command=self.printMessage)
        self.buttonPrint.pack()

        self.buttonQuit = Button(frame, text="Exit window", command=frame.quit)
        self.buttonQuit.pack(side=LEFT)

    def printMessage(self):
        print("Button clicked")


####creating drop down

def function1():
    print("Menu item clicked")


# # create window
# root = Tk()
#
# buttons1 = myButtons(root)
#
# myMenu = Menu(root)  # Menu ir prebuilded class
# root.config(menu=myMenu)
#
# firstSubMenu = Menu(myMenu)  # submenu object created
#
# myMenu.add_cascade(label="File", menu=firstSubMenu)
#
# firstSubMenu.add_command(label="Project", command=function1)
# firstSubMenu.add_command(label="Save", command=function1)
#
# firstSubMenu.add_separator()
#
# firstSubMenu.add_command(label="Exit", command=function1)
#
# # 2nd menu
# newMenu = Menu(myMenu)
# myMenu.add_cascade(label="Edit", menu=newMenu)
# newMenu.add_command(label="Undo", command=function1)
#
# ####toolbar
# toolbar1 = Frame(root, bg="pink")
# insertButton = Button(toolbar1, text="Insert file", command=function1)
# insertButton.pack(side=LEFT, padx=2, pady=3)
#
# printButton = Button(toolbar1, text="Print", command=function1)
# printButton.pack(side=LEFT, padx=2, pady=3)
#
# toolbar1.pack(side=TOP, fill=X)
#
#
#
# ####Making status bar
# statusBar = Label(root, text="This is the status bar", bd=1, relief=SUNKEN, anchor=W)
# statusBar.pack(side=BOTTOM, fill=X)
#
# ####message box
# import tkinter.messagebox
#
# tkinter.messagebox.showinfo("Title", "This is awesome")
#
# #message box that accepss response
# response = tkinter.messagebox.askquestion("Question 1", "Do you like coffe?")
# if response == "yes":
#     print("Here is a coffe for you!")


# create window
root = Tk()

####tkinter drawing

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newLine = canvas.create_line(0, 0, 50, 100)
otherLine = canvas.create_line(10, 10, 100, 100, fill="green")

# wait - make loop to wait before closing button pressed
root.mainloop()
