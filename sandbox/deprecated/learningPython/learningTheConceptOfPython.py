# print(49**(1/2)) #traukti sakni
#
# print(98/7)
# print(98//7)
#
# print(7/3)
# print(7%3)
#
# print(2343%2) #jeigu 0 tai lygu, jeigu 1 nelygiai dalinasi
# print(7%(5//2))
#
#
# print('He\'s a nice guy')
#
# print("He is a \"good guy\"")

# kad useris galeetu ivesti info pythonui
# input('Please enter a value: ')

# print('Hello mike \n welcome to the club') # \n - reiskia nauja eilute


# print("hello"+" world") # + sujungia dvi reiksmes viena su kita,
# kaip ir 5+5 bus 55, o ne 10
# print("5"+"5")

# print("rob"*3) # daugina kiek kartu bus spausdinama reiksme "string"
# # print("rob"*"10") # negalima dauginti string'u
# name = 1;
# print(name)


###variables
#
# a=10
# b=20
# c=a+b
# print(c)
# name="Rolandas"
# print(name, "has", c, "yers old")
#
# # padidinant nurodyta skaiciu kiek norim
# personsAge=26
# personsAge=personsAge+1
# print(personsAge)
# # geriau taip:
# personsAge+=1
# print(personsAge)
#
# personsAge-=5
# print(personsAge)
#
# personsAge*=2
# print(personsAge)
#
#
# b="hello"
# b+=" world"
# print(b, personsAge)

#### if conditions
# personsAge = int(input("Enter your age: "))
# if personsAge>=18:
#     print("You are adult")
# else:
#     print("You are not an adult")

#### else if  in python is elif statement
# marksFromStudents = int(input("Enter you'r marks: "))
# if marksFromStudents >= 90:
#     print("Grade A")
# elif marksFromStudents >= 70:
#     print("Grade B")
# elif marksFromStudents >= 60:
#     print("Grade C")
# elif marksFromStudents < 60:
#     print("Grade D")

#### Lists in python
# namesOfPeople = ["jogurtas"],["Rolandas", "Petras", "John", "Dambel"]
# print(namesOfPeople[0][1])
# numbers = [1,2,3,4]
# print(numbers[0])
# abc = []
# print(abc)

# numbers = [1,1,1,1,1]
# numbers[2] = 5
# print(numbers[2])

# numbers = [1,1,1,1,1]
# newnumbers = [2,2,2,2,2]
# print(numbers+newnumbers)
# print(numbers[2]+newnumbers[1])
# print(numbers*3)

# fruits = ["apple", "mango", "peach"]
# print("apple" in fruits)

#### list functions
# fruits = ["apple", "mango", "peach", "orange"]
# print(fruits.index("orange"))

####range functions
# numbers = list(range(10, 20, 5))
# print(numbers)

####code reuse and functions

# def testFunction():
#     print("Rolandas")
#     print("testč")
#     print("london")
#
#
# testFunction()

####for loop
# for variableX in range(1,11,2):
#     # print(variableX)
#     print("Rolandas")


# fruits = ["apple", "mango", "peach"]
# for variableFruits in fruits:
#     print(variableFruits)

# for variableX in range(0,21,2):
#     print(variableX)

####boolean logic
# userName = "admin"
# password = "admin123"
# if userName == "admin" or password == "admin123":
#     print("Valid user")
# else:
#     print("Invalid user")

#### while loop
# counter = 0
# while (counter < 10):
#     print(counter)
#     counter += 1
#
# name = "as"
# print(name)

##########################################
####section 3####

####coding challange part 1


# myFavoriteFood = ["Apple", "Banana", "Orange", "Peach", "Kiwi"]
# print(myFavoriteFood[2])
# myFavoriteFood.append("Appbanana")
# print(myFavoriteFood)
# myFavoriteFood.insert(3, "tacos")
# print(myFavoriteFood)

####coding challenge part 2
#
# for printMyName in range(1,6):
#     print("I am a programmer")
#
# def squareOfValues():
#     #padariau sakni, nes galvojau kad square yra saknis
#     # square = 1
#     # while(square<10):
#     #     print(square**(1/2))
#     #     square+=1
#
#     #o turejo buti taip:
#     for x in range(1,10):
#         print(x*x)
#
# squareOfValues()


# #test
# def testFunction(name):
#     print(name)
#
#
#
# testFunction("petras")

####returning values from functions
# def add(a, b):
#     c = a + b
#     return c
#
#
# result = add(100, 200)
# print(result)

#### passing functions as arguments to another functions
# def add(a, b):
#     return a + b
#
#
# def square(c):
#     return c * c
#
# print(square(add(10, 10)))

####modules in python
# import random
#
# for x in range(5):
#     result = random.randint(1,1111111111)
#     print(result)

####coding challange 4

# def bmiCalculator(weight, height):
#     BMI = weight / (height ** 2)
#     return BMI
#
#
# w = int(input("enter your weight: "))
# h = float(input("enter your height: "))
#
# result = bmiCalculator(w, h)
# print(result)
#
#
# def calculate_BMI(new_weight, new_height):
#     new_bmi = new_weight/(pow(new_height, 2))
#     return new_bmi
#
# weight = float(input('Enter weight in Kgs'))
# height = float(input('Enter height in meters'))
# bmi = calculate_BMI(weight, height)
# print(bmi)

#################################################
####exception handling
# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print("Error: Don't enter 0 value dud...")

####finaly block
# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print("Error: Don't enter 0 value dud...")
# finally:
#     print("This is going to execute no matter what")

####file handling
# open
# read
# write
# close

# open file with w - write mode
# openAndReadFile = open("demo.txt","w")



# reading data from demo.txt file
# openAndReadFile = open("sandbox/demo.txt","r")
# content = openAndReadFile.readline()
# print(content)

# opening and adding data to file
# file = open("sandbox/demo.txt", "w")
# file.write("this is the text writen to file")
# file.close()
#
# file2 = open("sandbox/demo.txt", "r")
# content = file2.read()
# print(content)
# file2.close()
#
# # a = append mode only adds value
# file3 = open("sandbox/demo.txt", "a")
# file3.write("this is the new line text")
# file3.close()

####coding challenge 5
# def handlesDivisionByZero(a, b):
#     try:
#         result = a / b
#         print(result)
#     except ZeroDivisionError:
#         print("Division by zero was handled.")
#
#
# handlesDivisionByZero(5, 0)

####coding challenge 6
# file = open("sandbox/demos.txt", "w")
# file.write("random content is writen to the file...")
# file.close()
#
# file = open("sandbox/demos.txt", "r")
# contentOfFile = file.read()
# print(contentOfFile)
# file.close()
#
# file = open("sandbox/demos.txt", "a")
# file.write("\nSecond random text is written without removing first code...")
# file.close()

#  file = open("sandbox/demos.txt", "r+")
# file.write("random content is writen to the file...")
#
# contentOfFile = file.read()
# print(contentOfFile)
# file.close()
#
# file = open("sandbox/demos.txt", "a")
# file.write("\nSecond random text is written without removing first code...")
# file.close()

######################################
# test1 = input("Hello, what is your name? ")
# print("Nice to meat you", test1,".My name is EFIL")
# test = int(input("How old are you? "))

# test2 = float(input("Enter your weight: "))
# test3 = float(input("Enter your height: "))
#
# print("Your name is: ", test1, "and your age is: ", test)
# print("Your KMI is: ", test2/(test3**2))
######################################
####dictionaries

# dictionary - this is key:value "John":32
# people = {"John":32, "Rob":23}
# print(people["John"]) #returns value - 32

####dictionaries functions
# numbers = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five"
# }
#
# # is value exists in dictionary
# print(3 in numbers)
# # get function of dictionary data
# print(numbers.get(7, "Key not found"))
#

####tuples - you can't change values like in list
# fruits = ("apple", "Mango", "Peach")
# print(fruits[1])

####list slicing
# number = [1, 2, 3, 4, 5, 6, 7, 8]
# print(number[2:5]) #providing from where to where show
#
# print(number[2:])
#
# print(number[1:3:5])

####list comprehension _:kvadratu
# list = [x ** 2 for x in range(5) if x ** 2 % 2 == 0]  # sitas % zenklas reiskia more of
# print(list)

#### String formatting
# shange integer to string
# numbers = [1, 2, 3, 4, 5, 6]
# newString = "numbers:{0},{1},{2}".format(numbers[0], numbers[1], numbers[2])
# print(newString)

# a = "{x}/{y}".format(x=100,y=200)
# print(a)

####string functions
# print(", ".join(["apple", "banana", "mango"])) #join function

# print("Hello there".replace("there", "world")) #replace function

# data mine
# newString = "This is a string"
# print(newString.startswith("This"))
# print(newString.endswith("is"))

# replace to upper or lower case
# newString = "This is a string"
# print(newString.upper())
# print(newString.lower())

####numeric functions
# print(min(1, 2, 3, 4, 5))
# print(max(1, 2, 3, 4, 5))
# print(abs(-203)) #core value without sign of value


#########################################
####coding challenge 7
# products = {"apple":200, "banana":20}
# print(products["apple"])
#
# products = {"Chair": 40, "Sofa": 500, "Table": 90, "Monitor": 100, "Carpet": 200}
#
# newproduct = input('Enter product name')
#
# if (newproduct in products):
#     print(products.get(newproduct))
# else:
#     print('Product Not Found')

####coding challenge 8
# lists = [x == 1 for x in range(101) if x ** 2 % 2 == 1]
# print(lists)
#
# new_list = list(range(1, 100))
#
# for x in new_list:
#
#     if x % 2 != 0:
#         print(x)

#####################################################
####functional programming
# def addTen(x):
#     return x+10
#
# def twice(func, arg):
#     return func(func(arg))
#
# print(twice(addTen,10))

####lambdas in python
# def square(x):
#     return x ** 2
#
#
# print(square(4))
#
# # now with lambda
# print((lambda x: x ** 2)(30))

####map
# newList = [10, 20, 30, 40, 50]
# result = list(map(lambda x: x + 2, newList))
# print(result)

####Filters to use with lambdas
# newList = [1, 3, 4, 5, 7, 2, 9, 11, 13]
#
# result = list(filter(lambda x: x % 2 == 0, newList))
# #filter() is used to filter out from list
# print(result)

####Generators
# def function():
#     counter = 0
#     while counter < 5:
#         yield counter
#         counter += 1
#
# for x in function():
#     print(x)

# generator to generate list of numbers
# def evenNumbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
#
# print(list(evenNumbers(21)))

####coding challenge 9
# print(products["apple"])

#
# products = {"apple":20, "banana":30, "peach":12}
#
# def forStudentsDiscount(productPrice):
#     discountedForStudent = productPrice - (productPrice*0.1)
#     return discountedForStudent
#
# def forAdditionalDiscount(prodPrice):
#     additDiscountPrice = prodPrice - (prodPrice*0.05)
#     return additDiscountPrice
#
#
#
# provideProductToDiscount = input("Enter product to discount: ") #useris duoda produkta
# fullProductsPrice = products[provideProductToDiscount] #susirandu jo kaina
#
# areYouAStudent = input("Are you a student (type: 'Yes' or 'No')?: ") #ar studentas
# if areYouAStudent == "Yes": #jei taip
#     doYouNeedAdditionalDiscount = input("Do you need additional "
#                                         "discount (type: 'Yes' or 'No')?: ")
#     if doYouNeedAdditionalDiscount == "Yes":
#         resultForStudents = forStudentsDiscount(fullProductsPrice)
#         additionalDiscount = forAdditionalDiscount(resultForStudents)
#         print(additionalDiscount)
#     else:
#         resultForStudents = forStudentsDiscount(fullProductsPrice)
#         print(resultForStudents)
#
# elif areYouAStudent == "No":
#     resultForOthers = forAdditionalDiscount(fullProductsPrice)
#     print(resultForOthers)
# else:
#     print("You have provided", areYouAStudent,
#           "but it had to be 'Yes', or no without parentheses")



# kitaip pagal mokytoja, nors ir mano veikia, bet..
# def student_discount(price):
#     price = price - (price * 10) / 100
#     return price
#
#
# def additional_discount(newprice):
#     newprice = newprice - (newprice * 5) / 100
#     return newprice
#
#
# selling_price = 100
#
# # applying both discounts simultaneously
#
# print(additional_discount(student_discount(selling_price)))

####coding challenge 10
# print((lambda x: x*(x+5)**2)(5))

####coding challenge 11
# def discountProducts(productsToDiscount):
#     result = list(map(lambda x: x-(x*10)/100, productsToDiscount))
#     return result
# listOfProducts = [10,20,30,40]
# print(discountProducts(listOfProducts))

#################################################
#######Object oriented programming###############
#################################################

####class
# class students:
#     # atributes
#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact
#
#     # method
#     def getData(self):
#         print("Accepting data")
#         self.name = input("Enter name here: ")
#         self.contact = input("Enter contact here: ")
#
#     # method
#     def putData(self):
#         print("The name is:" + self.name, "This is the contact:" + self.contact)
#
#
# ####object creation
# # John = students("Blank", 0)
# # John.getData()
# # John.putData()
#
# ####inheritance - paveldimi metodai is kitu klasiu,
# nurodant prie naujos klases tarp ()
# class scienceStudent(students):
#     def __init__(self, age):
#         self.age = age
#
#     def science(self):
#         print("I'm a science student.")
#
#
# Rob = scienceStudent(20)
# Rob.science()
# Rob.getData()
# Rob.putData()

####Recursion - function that calls it self until something happens
# factorial of a number pvz. 3 - 3*2*1=6, 5 - 5*4*3*2*1 = 120
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * (factorial(x - 1))
#
# print(factorial(5))

####Sets - like collections or list, difference only unique elements in it
# numbers = {1, 2, 3, 4, 5, 6}
# numbers.add(7)
# numbers.remove(1)
# print(numbers)
# seta = {1, 2, 3, 4, 5}
# setb = {4, 5, 6, 7, 8}
#
# # print(seta | setb)  # uninion of 2 sets without dublicates
# # print(seta & setb)  # what are the same elements of these sets
#
# print(seta - setb)  # all values from seta with removed setb dublicates

####itertools - module
# from itertools import count
#
# for i in count(3):
#     print(i)
#     if i >= 20:
#         break

# from itertools import accumulate, takewhile
#
# numbers = list(accumulate(range(8)))
# print(numbers)
# print(list(takewhile(lambda x: x <= 6, numbers)))
# print(list(takewhile(lambda x: x <= 10, numbers)))

####operator overloading
# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # operator overloading
#     def __add__(self, other):  # operation overloading on addition
#         x = self.x + other.x
#         y = self.y + other.y
#         return point(x, y)
#
#     # define result
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
#
#
# point1 = point(1, 4)
# point2 = point(2, 8)
# point3 = point(1, 2)
#
# print(point1 + point2 + point3)

####data hiding or encapsulation
# hifing data from other code and to allow to see it to particualar code
# class myclass:
#     __hiddenVariable = 1
#
#     def add(self,increment):
#         self.__hiddenVariable+=increment
#         print(self.__hiddenVariable)
#
#
# objectOne = myclass()
# objectOne.add(1)
# print(objectOne.__hiddenVariable) # cannot to access variablia outside class



####coding challenge 12
# class desktop:
#     def dekSpec(self):
#         print("weight == 100")
#
# class laptop:
#     def lapSpec(self):
#         print("Screen = 1024x512")
#
#
# class computer(desktop, laptop):
#     def getspecs(self):
#         desktop.dekSpec(self)
#         laptop.lapSpec(self)
#
#     def displayspecs(self):
#         results = computer.getspecs(self)
#         return results
#
#
# result = computer()
# res = result.displayspecs()
# print(res)

####coding challenge 13
# class Number:
#     def __init__(self, x):
#         self.x = x
#
#     def __mul__(self, other):
#         x = self.x + other.x
#         return x
#
#
# number_a = Number(3)
#
# number_b = Number(4)
#
# print(number_a * number_b)

##########################################################################
####regular expressions - fro string manipulation#########################
##########################################################################

####regular expression
# import re
#
# pattern = r"eggs"
#
# if re.match(pattern, "eggseggseggsbacon"):
#     print("match found")
# else:
#     print("No match found")

####serch & find all functions
# import re
#
# pattern = r"eggs"
#
# if re.match(pattern, "baconeggseggsbacon"):
#     print("match found")
# else:
#     print("No match found")
#
#
# if re.findall(pattern, "baconeggseggsbacon"):
#     print("match found")
# else:
#     print("No match found")
#
# if re.search(pattern, "baconeggseggsbacon"):
#     print("match found")
# else:
#     print("No match found")
#
# print(re.findall(pattern, "baconeggseggsbacon"))
# print(re.search(pattern, "baconeggseggsbacon"))


####find & replace using regualr expresion
# import re
#
# string = "My name is John, Hi I'm John."
# myPattern = r"John"
# newString = re.sub(myPattern, "Rob", string)
# print(newString)

####the dot metacharacter
# import re
#
# mmyPattern = r"gr..y" #gr at the beginning and y at the end, .. means anything in the middle
#
# if re.match(mmyPattern, "grasy"):
#     print("Match found")

####Caret & dollar metacharacter :: ^$
# import re
#
# myPattern = r"^gr.y$"
# if re.match(myPattern, "gray"):
#     print("match 1")

####character class > verifys is good patern is followed
# import re
#
# myPattern = r"[A-Z][A-z][0-9]" #pattern
# if re.search(myPattern, "Za1"):
#     print("Match found")
# else:
#     print("match not found")

####star (*) metacharacters
# import re
#
# myPattern = r"eggs(bacon)*"#enny character can be repeated 0 or multiple times
#                             #when it's betwean () and * at the end
# if re.match(myPattern, "eggsbacon"):
#     print("match found")
# else:
#     print("match no found")

####Group
# import re
#
# myPattern = r"bread(eg.s)*(test)bread"
#
# if re.match(myPattern, "breadeggseggsbread"):
#     print("found")
# else:
#     print("not")
