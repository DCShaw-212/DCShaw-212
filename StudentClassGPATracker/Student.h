#pragma once

#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Student
{

	private:
		//variables

		string firstName;
		string lastName;
		vector<vector<string>> classData;
		//string course;
		//string term;
		char grade;
		int numOfCredits;
		string creditString;
		//double totalPoints;
		//double totalCredits;
		double GPA;




	public:

		//Prototypes

		//full name for student class
		Student(string, string);

		//full name default constructor
		Student();

		// returns first name data member
		string getFirstName();

		// 1 string parameter. sets student first name to string
		void setFirstName(string);

		// returns last name data member
		string getLastName();

		// 1 string parameter. sets student last name to string
		void setLastName(string);

		// 1 string parameter. returns nothing. prints term such as "Fall 2021"
		void printTerm(string);

		//accepts 2 string for class and term. 1 char for grade. 1 int for numOfCredits
		// creates a string vector that represents the class, adds that vector to the 2D vector representing the class
		void addClass(string, string, char, int);


		//Calculates GPA. No parameters. returns a double. 
		double calcGPA();

		//Calculates GPA by term. 1 string parameter to accept term. returns a double.
		double calcGpaByTerm(string);

};

