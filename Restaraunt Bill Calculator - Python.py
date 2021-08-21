#Request input from user and store input as variable

subTotalMealcost = input("Enter subtotal cost of meal: ")
subTotalMealcost = float(subTotalMealcost)
subTotalMealcost = format(subTotalMealcost, ".2f")

#print(subTotalMealcost)

#calculate tip of 15% using P% * x = y

tip = .15 * float(subTotalMealcost)
tip = format(tip,".2f")

#print(tip)


#calculate tax at 6% using p% * x = y

tax = .06 * float(subTotalMealcost)
tax = format(tax, ".2f")

#print(tax)


#calculate total cost of the meal

totalMealcost = float(subTotalMealcost) + float(tip) + float(tax)
totalMealcost = format(totalMealcost, ".2f")


#print(totalMealcost)

#official output to user

print("Your recommended tip is: " + tip)
print("Your tax is: " + tax)
print("The total cost of the meal: " + totalMealcost)




