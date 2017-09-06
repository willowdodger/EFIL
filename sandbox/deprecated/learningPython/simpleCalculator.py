# gaunam info is uzerio
principal = input("Enter value for principal: ")
number = input("Enter value for number: ")
rateOfInterest = input("Enter value for rate of interest: ")

# konvertuojam gauta informacija is userio i integerius (nes tikimes gauti int)
principal = int(principal)
number = int(number)
rateOfInterest = int(rateOfInterest)

# tada sudauginam ir atspausdinam
simpleInterest = (principal*number*rateOfInterest)/100
print(simpleInterest)
