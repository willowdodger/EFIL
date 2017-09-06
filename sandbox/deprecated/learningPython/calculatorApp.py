from tkinter import *
import math
import parser  # will help to solve mathematical operations

root = Tk()
root.title("Calculator")

# get the users input and place in the textfield/input box
i = 0


# factorial = math.factorial()


def getVariables(num):
    global i  # keeps track to where the number must be placed
    display.insert(i, num)  # at witch index position you want to place number
    i += 1  # next time it will append i to be position 1, so 1234567...


def getOperation(operator):
    global i
    lengthOfOperator = len(operator)  # after getting operator, we calculate it's length
    display.insert(i, operator)
    i += lengthOfOperator  # we increment global i with operators length


def calculate():
    entireString = display.get()
    try:
        a = parser.expr(entireString).compile()
        result = eval(a)
        clearAll()
        display.insert(0, result)
    except Exception:
        clearAll()
        display.insert(0, "Error")


def clearAll():  # delleting the entire display
    display.delete(0, END)  # from where to where delete, from 0 to END, means all


def undo():  # delete single element
    entireString = display.get()  # gets all the input value as string
    if len(entireString):
        newString = entireString[:-1]  # that it would specify 1 element
        clearAll()  # then it deletes all from string
        display.insert(0, newString)  # puts all old string as new but with -1 string
    else:
        clearAll()
        display.insert(0, "Error")


def myFactorial():
    stringOfInput = display.get()  # breaks is 5+5, because it cant be a string
    try:
        gotNumber = int(stringOfInput)
        fact = 1
        while (gotNumber > 0):
            fact = fact * gotNumber
            gotNumber = gotNumber - 1
        clearAll()
        display.insert(0, fact)
    except ValueError:
        clearAll()
        display.insert(0, "Error, only numbers can be factorials.")


# adding the input field
display = Entry(root)  # input field is Entry()
display.grid(row=1, columnspan=7, sticky=W + E)  # adding to main field layout

# adding buttons to the calculator
Button(root, text="1", command=lambda: getVariables(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: getVariables(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: getVariables(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: getVariables(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: getVariables(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: getVariables(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: getVariables(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: getVariables(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: getVariables(9)).grid(row=4, column=2)

# adding other buttons to calculator
Button(root, text="AC", command=lambda: clearAll()).grid(row=5, column=0)  # removes everything from input field
Button(root, text="0", command=lambda: getVariables(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: getOperation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: getOperation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: getOperation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: getOperation("/")).grid(row=5, column=3)

# adding new operations
Button(root, text="pi", command=lambda: getOperation("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: getOperation("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: getOperation("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: getOperation("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!", command=lambda: myFactorial()).grid(row=3, column=5)
Button(root, text=")", command=lambda: getOperation(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda: getOperation("**2")).grid(row=5, column=5)
Button(root, text=",", command=lambda: getOperation(",")).grid(row=5, column=5)

root.mainloop()
