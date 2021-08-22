// Shaw_Assn5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//Name: Dustin Shaw
//Purpose: This program uses a Class and pointers to access student data

#include <iostream>
#include <string>
#include "Student.h"
#include <iomanip>

int main()
{
    Student keepAtIt;
    keepAtIt.setFirstName("Doesn't");
    keepAtIt.setLastName("Giveup");
    keepAtIt.addClass("MATH270", "Fall 2020", 'F', 4);
    keepAtIt.addClass("MATH270", "Spring 2021", 'D', 4);
    keepAtIt.addClass("CIS202", "Spring 2021", 'F', 3);
    keepAtIt.addClass("MATH270", "Fall 2021", 'B', 4);
    keepAtIt.addClass("CIS202", "Spring 2021", 'A', 3);

    Student nerd;
    nerd.setFirstName("Dorky");
    nerd.setLastName("McDorkface");
    nerd.addClass("CIS202", "Fall 2020", 'A', 3);
    nerd.addClass("CIS244", "Spring 2021", 'A', 3);
    nerd.addClass("CIS254", "Fall 2021", 'B', 3);
    nerd.addClass("CIS253", "Fall 2021", 'A', 3);

    cout << nerd.getFirstName() << " " << nerd.getLastName() << "'s GPA is: " << setprecision(2) << nerd.calcGPA() << endl;

    

    cout << keepAtIt.getFirstName() << " " << keepAtIt.getLastName() << "'s GPA is: " << keepAtIt.calcGPA() << endl;

    Student allOver;
    allOver.setFirstName("All");
    allOver.setLastName("Over");
    allOver.addClass("CIS254", "Fall 2021", 'A', 3);
    allOver.addClass("MATH270", "Fall 2021", 'B', 4);
    allOver.addClass("HEALTH110", "Fall 2021", 'C', 2);
    allOver.addClass("CIS422", "Fall 2021", 'D', 5);
    allOver.addClass("IDK101", "Fall 2021", 'F', 1);

    cout << allOver.getFirstName() << " " << allOver.getLastName() << "'s GPA is: " << allOver.calcGPA() << endl;

    cout << "==========Everyone's Fall 2021 Term==========" << endl;
    cout << nerd.getLastName() + ", " + nerd.getFirstName() + ":" << endl;
    nerd.printTerm("Fall 2021");
    cout << endl;

    cout << keepAtIt.getLastName() + ", " + keepAtIt.getFirstName() + ":" << endl;
    keepAtIt.printTerm("Fall 2021");
    cout << endl;

    cout << allOver.getLastName() + ", " + allOver.getFirstName() + ":" << endl;
    allOver.printTerm("Fall 2021");
    cout << endl;

    cout << "==========Everyone's Fall 2021 GPA===========" << endl;
    cout << nerd.getLastName() + ", " + nerd.getFirstName() + ": ";
    cout << nerd.calcGpaByTerm("Fall 2021") << endl;

    cout << keepAtIt.getLastName() + ", " + keepAtIt.getFirstName() + ": ";
    cout << keepAtIt.calcGpaByTerm("Fall 2021") << endl;

    cout << allOver.getLastName() + ", " + allOver.getFirstName() + ": ";
    cout << allOver.calcGpaByTerm("Fall 2021") << endl;

};



// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
