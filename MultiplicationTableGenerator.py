#Multiplication table generator
#This program genereates a multiplication table based on a user specified number
#written by: Dustin Shaw

#Get number to create table for. User generated.

userNum = int(input("Please enter a whole number you're generating the table for: "))

#Request how many rows the user would like

mikeRowes = int(input("How many rows in the table would you like?: "))

#Generate header for the multiplication table

print("\nMultiplaction table for the number", userNum)
print("\n============================================\n")

#Calculate the values for the user specified numbers and prints to the console
product = 0

for i in range (1, mikeRowes + 1):
    product = userNum * i
    print(userNum, 'x', i, product)
