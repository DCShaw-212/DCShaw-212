#DogYears
#This program converts human years into dog years, and uses an if-elif-else chain to state a comment
#Written by: Dustin Shaw


# Get the two dogs ages from the user
print("You'll enter the age of two dog's in human years and I'll convert it to human years.\n")

dog1 = float(input("Please enter the first dog's age: "))

dog2 = float(input("Please enter the second dog's age: "))

#calculate dog1's age in dog years

if dog1 <= 2:
    dog1 = dog1 * 10.5
   
else:
    dog1 = (dog1 - 2) * 4 + 21

print("Dog1 is", dog1, "in dog years.")

#Calculate dog2's age in dog years

if dog2 <= 2:
    dog2 = dog2 * 10.5

else:
    dog2 = (dog2 -2) * 4 + 21

print("Dog2 is", dog2, "in dog years.")

#Chain of if-elif-else producing the output

if dog1 == dog2:
    print("They have been friends since birth")

elif dog1 > dog2 or dog1 > 50:
    print("senior")

elif dog1 >= 35 and dog2 >= 35:
    print("They could be president.")

elif dog2 <= 21:
    print("puppy.")

else:
    print("Cats are better anyway!")


