#Dustin Shaw

###The purpose of this program is to take in information from the user and calculate
##the cost of cdl permits in the state of Pennsylvania. 


#initialize variables and constants

#constants
HAZMATFEE = 17.00
MONTHS = 12
CLASSFEE = 5.00
PHOTOFEE = 9.50
INCREASEFEE = 17.00

#variables

currentMnth = 0
currentYear = 0
expMnth = 0
expYear = 0
restr = 0
endorse = 0
total = 0
mnthsToExp = 0

#welcome code

print("The purpose of this program is to calculate the cost of a CDL permit in the \n state of Pennsylvania. As this may very individual to individual.\n")


#input from the user

#current date
currentMnth = input("What is the current month? 1 - 12 \n")

currentMnth = int(currentMnth)

if currentMnth > 12 or currentMnth < 1:
    print("invalid selction \n")
    currentMnth = input("What is the current month? 1 - 12 \n")
    currentMnth = int(currentMnth)
    

currentYear = input("What is the current year? \n")

currentYear = int(currentYear)

#expiration date of the permit
expMnth = input("What is the expiration month? 1 - 12 \n")

expMnth = int(expMnth)

if expMnth > 12 or expMnth < 1:
    print("invalid selection\n")
    expMnth = input("What is the expiration month? 1 - 12\n")
    expMnth = int(expMnth)

expYear = input("What is the expiration year?\n")
expYear = int(expYear)

if expYear < currentYear:
    print("invalid selection\n")
    expYear = input("What is the expiration year?\n")
    expYear = int(expYear)

# # of restrictions


restr = input("How many restrictions are being removed?\n")
restr = int(restr)

if restr > 5:
    print("That's too many. They can only remove 5.")
    restr = input("How many restrictions are being removed?\n")
    restr = int(restr)

total = total + restr * 5

# # of endsorements

endorse = input("How many endorsements are being added?\n")
endorse = int(endorse)

if endorse > 5:
    print("That's too many. They can only add 5.")
    endorse = input("How many endorsements are being added?\n")
    endorse = int(endorse)

total = total + endorse * 5


#class added?

classDesired = input("Is a class desired? y/n \n")

if classDesired == 'Y' or classDesired == 'y':
    total += CLASSFEE
    

# # Hazmat?
hazmat = input("Are they adding hazmat? y/n \n")

if hazmat == 'Y' or hazmat == 'y':
    total += HAZMATFEE


# Increase Fee

mnthsToExp = (expYear * MONTHS + expMnth) - (currentYear * MONTHS + currentMnth)

if mnthsToExp >= 7 and mnthsToExp <= 12:
    total += INCREASEFEE

elif mnthsToExp >= 13 and mnthsToExp <= 24:
    total += INCREASEFEE * 2

elif mnthsToExp >= 25 and mnthsToExp <= 36:
    total += INCREASEFEE * 3

elif mnthsToExp >= 37 and mnthsToExp <= 48:
    total += INCREASEFEE * 4



# photo fee

total += PHOTOFEE


# format total
total = format(total, ".2f")


# output total cost of permit to the user

print("The total cost of the permit will be: $", total)

    

