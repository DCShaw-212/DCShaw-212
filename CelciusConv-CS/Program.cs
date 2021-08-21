//Name: Dustin Shaw
//Purpose: The purpose of this program is to take the user input of temprature(in Celcius) and conver it to fahranheit and kelvin


using System;

namespace Shaw_Assign1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Loop gives them 3 attempts to do the right thing
            for (int i = 0; i < 3; i++)
            {

                try
                {
                    //Welcome message
                    Console.Write("This program will convert celcius temperature in kelvin and fahrenheit.");

                    //Asks the user for input
                    Console.Write("Please enter a temperature in Celcius: ");

                    //Stores input from user into variable
                    string input = Console.ReadLine();

                    //converts input from string into a double
                    double C = double.Parse(input);

                    //Equations for temperature conversion

                    double fahrenheitConv = (C * 9 / 5) + 32;

                    double kelvinConv = C + 273.15;

                    //Output conversions to the user

                    Console.WriteLine("The temperature in Kelvin is: " + kelvinConv);
                    Console.WriteLine("The temperature in Fahrenheit is: " + fahrenheitConv);
                }
                catch
                {
                    Console.WriteLine("You didn't enter a number.");



                }
            }

        }
    }
}
