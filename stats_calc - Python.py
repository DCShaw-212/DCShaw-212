import statistics

import math



#original data inserted here
data = [2.7,2.8,3.0,2.3,2.2,2.8,2.1,2.4]


X = [6.1,5.4,3.9,5.2,6.2,6.5,11.1]
Y = [-1.0,-4.2,-7.0,-4.0,3.6,-0.1,-4.4]

#sorts the data
data.sort()

#finds the number of data points
n = len(data)
xLen = len(X)
yLen = len(Y)

#Find the size of the 

#find min, max and range of the data

maxNum = data[-1]
minNum = data[0]
dataRange = maxNum - minNum


#Find the sum of all data Ex


datatotal = 0
for i in range(n):
    datatotal = datatotal + data[i]
    squaredTotal = datatotal * datatotal

#finds the sum of all X values

xTotal = 0
for i in range(xLen):
    xTotal = xTotal + X[i]

#finds the sum of all Y values

yTotal = 0
for i in range(yLen):
    yTotal = yTotal + Y[i]

#finds the sum of all data values squared

datatotalSquared = 0
for i in range(n):
    dataTwo = data[i] * data[i]
    datatotalSquared = datatotalSquared + dataTwo

#finds the sum of all X values squared

xTotalSquared = 0
for i in range(xLen):
    xTwo = X[i] * X[i]
    xTotalSquared = xTwo + xTotalSquared

#finds the sum of all Y values squared

yTotalSquared = 0
for i in range(yLen):
    yTwo = Y[i] * Y[i]
    yTotalSquared = yTwo + yTotalSquared

#Exy


count = 0
xySum = 0

for i in range(xLen):
    count = X[i] * Y[i]
    xySum += count
    
    
    


#find mean, median, and mode

#mode aka most often occuring (requires a loop and count function to find the most common occuring data set)

most_common = statistics.mode(data)



#median aka the middle number (check if n is even or odd, to find the medians postion)

medianOfData = statistics.median(data)

#find the median posistions to calulate quartiles
Q1List = []
Q3List = []

if n%2 != 0:
    medianPos = (n+1)//2
    for i in range(medianPos):
        Q1List.append(data[i])
    for i in range(medianPos, n):
        Q3List.append(data[i])
else:
    medianPosLow =  math.floor(n/2)
    medianPosHigh = math.ceil(n/2)
    for i in range(medianPosLow):
        Q1List.append(data[i])
    for i in range(medianPosHigh, n):
        Q3List.append(data[i])


#find Q1 , Q3, and IQR



# First quartile (Q1)
Q1 = statistics.median(Q1List)
# Third quartile (Q3)
Q3 = statistics.median(Q3List)
  
# Interquaritle range (IQR)
IQR = Q3 - Q1




#Mean aka the average (find the average of all data set)

datamean = statistics.mean(data)
Xmean = statistics.mean(X)
Ymean = statistics.mean(Y)


#Trimmed Mean - trim 5% off the ends of the data list and then find the average of that

trimTotal = 0

fivePercent = n * .05

fivePercent = math.ceil(fivePercent)

trimN = n - (fivePercent * 2)

for i in range(fivePercent, n - fivePercent):
        trimTotal = trimTotal + data[i]

trimMean = trimTotal / trimN




#Find the sum of all data squared





#Calculates sample standard deviation and sample variance
variantTotal = 0

for i in range(n):
    variantX = (data[i] - datamean)**2
    variantTotal = variantTotal + variantX

variant = variantTotal / (n -1)

standardDeviation = math.sqrt(variant)




#Calculates population standard deviation

popVariant = variantTotal / n

popStandardDeviation = math.sqrt(popVariant)




#Calculates coefficient of variation

coeffOfVar = (standardDeviation / datamean) * 100
    



#find class width

classWidth = (maxNum - minNum) / 5

classWidth = math.ceil(classWidth)

#classWidth = int(classWidth)

#Finding correlation Coefficient

  
# function that returns correlation coefficient.
def correlationCoefficient(X, Y, n) :
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0
      
      
    i = 0
    while i < n :
        # sum of elements of array X.
        sum_X = sum_X + X[i]
          
        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]
          
        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]
          
        # sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]
          
        i = i + 1
       
    # use formula for calculating correlation 
    # coefficient.
    corr = (float)(n * sum_XY - sum_X * sum_Y)/(float)(math.sqrt((n * squareSum_X - 
           sum_X * sum_X)* (n * squareSum_Y - 
           sum_Y * sum_Y)))
    return corr
      

       
# Find the size of array.
n = len(X)
  


  




#find range for each class

##classes = [[],[],[],[],[]]
##for i in range(5):
##    classes.append([])
##
##
##count = 0
##
##for i in range(5):
##    for j in range(classWidth):
##        classes[i].append(data[count])
##        count += 1
##        



###seperate the data points into their classes
##class1 = classes[0]
##class2 = classes[1]
##class3 =  classes[2]
##class4 = classes[3]
##class5 = classes[4]
##
##
##class1Len = len(class1)
##class2Len = len(class2)
##class3Len = len(class3)
##class4Len = len(class4)
##class5Len = len(class5)






print("The entire Data set: \n")
print(data)
print("\n")
print("The total number of data values: ")
print(n , "\n")
print("Total number of X values: " , xLen)
print("Total number of Y values: " , yLen)
print("\n")
print("___________________________________")
print("\n")
print("Sum of all Data: " , datatotal)
print("Sum of all Data Squared:", datatotalSquared)
print("Sum of al X values: ", xTotal)
print("X values squared: ", xTotalSquared)
print("Sum of al Y values: ", yTotal)
print("Y values squared: ", yTotalSquared)
print("\n")
print("The sum of X times Y /Exy:  ", xySum)

print("___________________________________")
print("\n")

print("The class width is ", classWidth, "\n")


#print(Q1List)
#print(Q3List)


print("______________________________________________\n")

print("Minimum:", minNum)
print("Q1: ", Q1)
print("Q2/Median: ", medianOfData)
print("Q3: ", Q3)
print("maximum: ", maxNum)
print("Interquartile Range: ", IQR)
print("\n")

print("Mode: ", most_common)
print("\n")

print("Mean of Data List: ", datamean)
print("Mean of X List: " , Xmean)
print("Mean of Y List: " , Ymean)
print("Trimmed Data Mean: ", trimMean)

print("\n")
print("Variant Total: ", variantTotal)
print("Variant: " , variant)
print("Range: " , dataRange) 
print("Sample Standard Deviation: " , standardDeviation)
print("Population Standard Deviation: " , popStandardDeviation)
print("Coefficient of Variation: " , coeffOfVar)
print("Correlation Coeffecient: " ,correlationCoefficient(X, Y, n))
print("\n")


##print("Class1: \n")
##print(class1)
##print (class1Len)
##                    
##            
##print("____________________________________\n")
##
##print("Class2:\n")
##print(class2)
##print (class2Len)
##
##print("_____________________________________\n")
##
##print("Class 3:\n")
##print(class3)
##print (class3Len)
##
##print("_____________________________________\n")
##      
##print("Class 4:\n" )
##print(class4)
##print (class4Len)
##
##print("_____________________________________\n")
##      
##print("Class 5:\n")
##print(class5)
##print (class5Len)
##
##print("_____________________________________")




