#include "Student.h"
#include <string>
#include <iostream>
#include <vector>

using namespace std;

//Function for Student (accepts 2 strings and returns them)
Student::Student(string firstName, string lastName)
{

}

//Student function that does nothing
Student::Student() {}

//getFirstName() returns value of first name data member
string Student::getFirstName()
{
	return firstName;
}

//setFirstName() takes 1 string parameter and sets students first name to that string
void Student::setFirstName(string firstNameIn)
{
	firstName = firstNameIn;
}

//getLastName() returns value of last name data member
string Student::getLastName()
{
	return lastName;
}

//setLastName() takes 1 string parameter and sets students last name to the string
void Student::setLastName(string lastNameIn)
{
	lastName = lastNameIn;
}

//void printTerm()
void Student::printTerm(string termIn)
{
	
	// loops through the 2D vector to find each row and print them to the console
	for (int i = 0; i < classData.size(); i++)
	{

		vector <string> eachClass = classData[i];

	

		if (eachClass[1] == termIn)
		{
			cout << eachClass[0];
			cout << " ";
			cout << eachClass[2] + " ";
			cout << " ";
			cout << eachClass[3] << endl;
		}

		   
		
	}
}

//creates a string vector that represents the class, adds that vector to the 2D vector representing the class

void Student::addClass(string course, string term, char grade, int numOfCredits)
{
	bool repeatedClass = false;
	string gradeString = string(1, grade);

	//loop through all classes
	for (int i = 0; i < classData.size(); i++)
	{
		vector <string> eachClass = classData[i];
		

		//if class matches the input class name, updates the term and grade
		if (course == classData[i][0])
		{
			classData[i][1] = term;
			classData[i][2] = gradeString;
			repeatedClass = true;
		}
	}
	repeatedClass = false;

	//If repeatedClass is still false, add on the new class
	if (repeatedClass == false)
	{
		grade = gradeString[0];
		creditString = to_string(numOfCredits);
		vector <string> newClass = { course, term, gradeString, creditString };
		classData.push_back(newClass);

	}
};



// use double for loop to go through the 2D Array of add Class and find the average grade

double Student::calcGPA()
{
	
	double totalPoints = 0;
	double totalCredits = 0;
	double pointsEarned = 0;

	for (int i = classData.size() - 1; i >= 0; i--)
	{
		//data for each row aka each class

		vector <string> eachClass = classData[i];

		//find grade position and set it to stringGrade
		// in each row grade is index position 2


		string stringGrade = eachClass[2];

		grade = stringGrade[0];

		//conditionals to set letter grade to a double representitave 

		if (grade == 'A')
		{
			pointsEarned = 4.0;
		}
		else if (grade == 'B')
		{
			pointsEarned = 3.0;
		}

		else if (grade == 'C')
		{
			pointsEarned = 2.0;

		}
		else if (grade == 'D')
		{
			pointsEarned = 1.0;
		}
	
		else
		{
			pointsEarned = 0.0;
		}

		//grabs the credit string from vector eachClass
		creditString = eachClass[3];

		//set numOfCredits to integer conversion of creditString
		numOfCredits = stoi(creditString);

		

		//summing up the total points for weighted averaging

		totalPoints = totalPoints + (pointsEarned * numOfCredits);

		totalCredits = totalCredits + numOfCredits;
	}
	
	GPA = totalPoints / totalCredits;



	return GPA;
}

// calculates GPA by term

double Student::calcGpaByTerm(string term)
{
    
	double totalPoints = 0;
	double totalCredits = 0;
	double pointsEarned = 0;
	
	

	for ( int i = classData.size() - 1; i >= 0; i--)
	{
		//data for each row aka each class

		vector <string> eachClass = classData[i];

		//find the term for each row and check if it equals the row. 

		if (term == eachClass[1]) 
		{
			//find grade position and set it to stringGrade
		// in each row grade is index position 2


			string stringGrade = eachClass[2];

			grade = stringGrade[0];

			//conditionals to set letter grade to a double representitave 

			if (grade == 'A')
			{
				pointsEarned = 4.0;
			}
			else if (grade == 'B')
			{
				pointsEarned = 3.0;
			}

			else if (grade == 'C')
			{
				pointsEarned = 2.0;

			}
			else if (grade == 'D')
			{
				pointsEarned = 1.0;
			}

			else
			{
				pointsEarned = 0.0;
			}

			//grabs the credit string from vector eachClass
			creditString = eachClass[3];

			//set numOfCredits to integer conversion of creditString
			numOfCredits = stoi(creditString);

			//summing up the total points for weighted averaging

			totalPoints = totalPoints + (pointsEarned * numOfCredits);

			totalCredits = totalCredits + numOfCredits;
		}

		}

		GPA = totalPoints / totalCredits;



	return GPA;
}
