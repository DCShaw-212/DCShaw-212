#Calculate surface area of a triangular prism

#Get base measurement from the user

base = float(input("What is the base measurement: "))

#Get height measurement from the user 

height = float(input("What is the height measurement: "))

#Get length measurement from the user

length = float(input("What is the length measurement: "))

#Get a side measurement from the user

side = float(input("What is a side measurement: "))

#Using the equation sa = (b * h) + 2(l * s) + (l * b) to calculate the surface area of the prism

surfaceArea = (base * height) + 2 * (length * side) + (length * base)



print("The surface area of the triangular prism is: ", surfaceArea)
