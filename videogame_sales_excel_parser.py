#Name: Dustin Shaw
#Purpose: Parse through an excel file to find answers to data questions

#Open the CSV file for reading
file = open("vgsales.csv")

#Skip the row with all the headers
next(file)

#Declare your variables here before the loop
rpgCount = 0
NESCount = 0
PS3_TakeTwo = 0
PS3_Action_TakeTwo = 0
Japan_Num1_Game = ""
Japan_Num1_Sales = 0
Globe_Puzzle_Fav = ""
Globe_Sales = 0
SpoGloSales = 0
SpoGloName = ""
Nin_Total = 0
total_count = 0
gameList = []
highestGameSales = []
old_list = []
year = 10000


#For each line in the file...
for line in file:
    
    #...split that line into a row by the commas.
    #We can now get each individual piece of data for the row by indexing
    #   it with row[#]
    row = line.split(",")
    
    ##1. Count the number of Role-Playing games – This is the one I completed for you as an example
    if row[3] == "Role-Playing":
        rpgCount += 1


    ##2. Count the number of NES games on the list
        #Hint: row[3] gives us the genre. Which row[?] gives us the platform?
        #How would we compare that platform to the string NES?
    if row[1] == "NES":
        NESCount += 1
        


    ##3. Count the number of PS3 games published by Take-Two Interactive in the file
        #Hint: Now you need to check both the platform AND the publisher
    if row[1] == "PS3"  and row[4] == "Take-Two Interactive":
        PS3_TakeTwo += 1


    ##4. Count the number of PS3 games in the Action genre published by Take-Two Interactive in the file
        #Similar to the last one, but now we also need to check the genre, for 3 checks total
    if row[1] == "PS3" and row[3] == "Action" and row[4] == "Take-Two Interactive":
        PS3_Action_TakeTwo += 1


    ##5. Determine the name and japan-based sales amount of the game that sold the most in Japan
        #Hint: On D2L, there is a FileParseExample that also parses a CSV.
        #   #4 on that is very similar to this.
    if float(row[7]) > Japan_Num1_Sales:
           Japan_Num1_Sales = float(row[7])
           Japan_Num1_Game = row[0]

        
    ##6. Detemine the name and global sales amount of the highest selling (globally) Puzzle game
        #Hint: This one is closer to #5 or #6 in FileParseExample
    if row[3] == "Puzzle":

        if float(row[9]) > Globe_Sales:
            Globe_Sales = float(row[9])
            Globe_Puzzle_Fav = (row[0])



    ##7. Determine the name and global sales amount for the highest selling Sports game that's not on the Wii 
        #Hint: Close to #5 in FileParseExample again. Remember that we can check if something is not equal
            #to something else as easily as we can check if it is equal
    if row[1] != "Wii" and row[3] == "Sports" and float(row[9]) > SpoGloSales:
        SpoGloSales = float(row[9])
        SpoGloName = row[0]
                
            


    ##8. Detemine the percentage of games on the list that Nintendo sold
        #Hint: The percentage of games is the number of games that Nintendo sold over the total number of games, times 100
        #   To get the number of games made by Nintendo, check the publisher to see if it's "Nintendo"
        #   To get the total count, just increment a count outside of an if statement
    total_count += 1
    if row[4] == "Nintendo":
        Nin_Total += 1
    NinSoldPerc = (Nin_Total/total_count) * 100
    NinSoldPerc = format(NinSoldPerc,".2f")

  


    ##9. Print the names of ALL games on the files published by LEGO Media
        #Hint: In the variables section before the loop, create an empty list
        #      Here, if the publisher is "LEGO Media", append the name (index 0) of the game to the list
        #      Where you print your variables, printing len(listName) will give you the number of items in the list,
        #           and printing listname will give you the names
    if row[4] == "LEGO Media":
        gameList.append(row[0])
    
          
 
    ##10. Print the names of all games with at least 10 million global sales
        #Hint: Very similar to #9, but check if the Global Sales column is greater than or equal to 20
    if float(row[9]) >= 20:
        highestGameSales.append(row[0])

        
    ##11. Determine the oldest game in the file.  If there's a tie for the oldest game (there is), print out ALL of the tying games' names and how many there are.
        #Hint: This is a tough problem. First find the year and convert it to an integer.
        #   Now, there are 3 possible situations:
        #       1. The year is the oldest (lowest) year we've seen
        #       2. The year is equal to the oldest (lowest) year we've seen
        #       3. The year is greater than the oldest (lowest) year we've seen
        #
        #   For possibility 3, we don't care about this because we are looking for the lowest year
        #   For possibility 2, there is a tie for the oldest game, so we just need to add the name of
        #       the new game to the list of games
        #   For possibility 1, we have found a new oldest game, so we need to do a couple of things:
        #           1. Update the year stored as the lowest year to the new year
        #           2. Clear the list of names (set it back to [])
        #           3. Add the name of the new game to the list.
        #
        #      A visual example (Note that our list needs to contains the NAMES, but
        #      here I'm using the years to make it easier to follow!
        #
        #       [1999,1999,1999] <-- We have 3 games with the lowest year, 1999
        #       -->1999          We find a new game with a year of 1999
        #       [1999,1999,1999,1999]  We add that game to the list
        #       --> 1997         We find a new game with year of 1997
        #       [1997]           We make that game the only game in the list, since the others are no longer the oldest game

        #Determine lowest year, giving the oldest game.
        #Add the games with the oldest year to the old list. 

    if int(row[2]) < year:
         year = int(row[2])
         old_list = []
         

    if int(row[2]) == year:
        
        old_list.append(row[0])
       

   
    

#### THE LOOP ENDS HERE #####
        
#1. Print the number of RPG games
print("The number of RPG games is: ", rpgCount)


#2. Print the number of NES games
print("The number of NES games is: ", NESCount)

#3. Print the number of PS3 games published by Take-Two Interactive
print("The number of PS3 games published by Take-Two Interactive is: ", PS3_TakeTwo)

#4. Print the number of Action-genre PS3 games published by Take-Two Interactive
print("The number of Action-genre PS3 games published by Take-Two Interactive is: ", PS3_Action_TakeTwo)

#5. Print the game with the most sales in Japan, and how many sales there were
print("The number 1 game sold in Japan is", str(Japan_Num1_Game) ,"and sold around", str(Japan_Num1_Sales) ,"million copies.")

#6. Print the highest selling (globally) puzzle game and how many millions of copies it sold globally
print("The worlds highest selling puzzle game is", str(Globe_Puzzle_Fav), "and it sold about", str(Globe_Sales) ,"million copies")

#7. Print the highest selling (globally) sports game not on the wii, and how many millions of copies it sold globally
print("The highest globally sold sports game (not on wii) is", str(SpoGloName) , "and it sold roughly" , SpoGloSales ,  "million copies.")

#8. Print the percentage of games in the file sold by Nintendo
print("Ninteno has sold about", NinSoldPerc, " percent of the games listed.")

#9. Print how many games from LEGO Media made the list and all of their names

print("There are",len(gameList),"from Lego Media and their names are", str(gameList))


#10. Print how many games sold over 20,000,000 copies, and all of their names
print("These companies sold over 20,000,000 copies: ", str(highestGameSales))

#11. Print all the games that tie for the oldest game, how many there were, and what year they were released
print("The title of the oldest games goes to", str(old_list), "They were released in the year",year)





file.close()
 

