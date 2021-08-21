// Shaw_Assgn4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//File Name: Shaw_Assgn4
//Version: 1ish
//Description: Takes user's input of Celcius and converts it to Fahrenheit and Kelvin
//Programmer: Dustin Shaw

#include <iostream>
#include <string>

using namespace std;
using std::string;


int main()
{
    //set attempts for correct input

    bool attempt = true
        ;
    //Introduce program to user and prompt for input

    cout << "This program converts Celcius to Fahrenheit and Kelvin\n";
    

    cout << "Please enter a number in Celcius: " << endl;

    cout << "" << endl;

    //intialize celcius input

    string celciusInput = "";

    do
    {
        try 
        {
            //Store input from user as a string variable for celcius input


            cin >> celciusInput;


            //Converts the celcius input from a string into a double (for math reasons)

            double celcius = stod(celciusInput);

            
            

            //Equation to concert celcius into fahrenheit

            double fahrenheitConv = (celcius * 9 / 5) + 32;

            //Equation to convert celcius into kelvin

            double kelvinConv = celcius + 273.15;

            //Sets output to two decimal places

            cout.setf(ios::fixed);
            cout.setf(ios::showpoint);
            cout.precision(2);

            //Output conversion to the user
            cout << "\n";
            cout << "Conversions:" << endl;
            cout << "" << endl;
            cout << celcius << " degrees Celcius" << endl;
            cout << fahrenheitConv << " degress Fahrenheit" << endl;
            cout << kelvinConv << " degress Kelvin" << endl;

            //Change attempt to false to exit the program
            attempt = false;

        }

        catch (exception e)
        {
            cout << "\n";
            cout << "Please enter a number...";
            
        };
        


    } while (attempt);

   











        
    
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
