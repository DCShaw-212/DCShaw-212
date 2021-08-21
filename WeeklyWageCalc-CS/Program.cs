//Name: Dustin Shaw
//Purpose: The purpose of this program is to compute the users weekly wage based on their paycode status

using System;

namespace Shaw_Assn2
{
    class Program
    {
        static void Main(string[] args)
        {   //Introduction
            Console.WriteLine("This program will compute your weekly wage.");
            Console.WriteLine("");

            //paycodes & Instructions
            Console.WriteLine("Paycodes");
            Console.WriteLine("1. Manager");
            Console.WriteLine("2. Hourly Worker");
            Console.WriteLine("3. Commission");
            Console.WriteLine("4. Piece Worker");
            Console.WriteLine("Type 5 to exit the program");
            

            //Starts loops to give attempts at entering proper paycode
            

            for (int count = 0; count < 10; count++)
            {
                try
                {
                    //prompt user for input and store input as a variable
                    Console.Write("Please enter your paycode: ");
                    string input = Console.ReadLine();

                    //Test whether input was valid or not
                    int payCode;
                    if (int.TryParse(input, out payCode))
                    {
                        if (payCode == 1)
                        {
                            //Manager Pay
                            //Gets fixed weekly pay from the manager

                            Console.Write("Enter a manager's fixed weekly pay: $");
                            string manPayText = Console.ReadLine();
                            double manPay = double.Parse(manPayText);
                            Console.WriteLine("The weekly pay as a manager would be: " + manPay.ToString("C"));
                            Console.WriteLine("Press any key to exit.");
                            Console.ReadKey();
                            Console.WriteLine("Exiting Program");
                            
                            count = 10;


                        }
                        else if (payCode == 2)
                        {
                            //Hourly Worker
                            //Get hourly pay from the user and hours worked and calculates weekly pay

                            Console.Write("Enter the hourly rate of pay: $");
                            string hrPay = Console.ReadLine();
                            double wage = double.Parse(hrPay);

                            Console.Write("Enter the number of hours worked this week (not including overtime, max 40 hours): ");
                            string regHrs = Console.ReadLine();
                            double normHours = double.Parse(regHrs);

                            Console.Write("Enter hours of overtime worked  this week: ");
                            string ovrHrs = Console.ReadLine();
                            double overHours = double.Parse(ovrHrs);

                            double normRate = wage * normHours;
                            double extraTime = (wage * 1.5) * overHours;

                            double hourlyWeekPay = normRate + extraTime;

                            Console.WriteLine("The weekly pay as an hourly worker would be: " + hourlyWeekPay.ToString("C"));
                            Console.WriteLine("Press any key to exit.");
                            Console.ReadKey();
                            Console.WriteLine("Exiting Program");
                            
                            count = 10;
                        }
                        else if (payCode == 3)
                        {
                            //Commission worker
                            //Gets gross sales from commission worker and gives weekly pay

                            Console.Write("Enter the gross sales made for the week: $");
                            string grossSales = Console.ReadLine();
                            double numGrossSales = double.Parse(grossSales);

                            double commWeeklyPay = 250 + (5.7 * numGrossSales) / 100;

                            Console.WriteLine("The weekly pay as a commission worker would be: " + commWeeklyPay.ToString("C"));
                            Console.WriteLine("Press any key to exit.");
                            Console.ReadKey();
                            Console.WriteLine("Exiting Program");
                            count = 10;
                        }
                        else if (payCode == 4)
                        {
                            //Piece Worker
                            //Gets items produced and pay per item from user to calculate weekly pay


                            Console.Write("Enter the fixed amount earned per item prduced: $");
                            string earnedPerItem = Console.ReadLine();
                            double numPerItem = double.Parse(earnedPerItem);

                            Console.Write("Enter the number of Items produced this week: ");
                            string itemsPerWeek = Console.ReadLine();
                            double numPerWeek = double.Parse(itemsPerWeek);

                            double pieceWeeklyPay = numPerItem * numPerWeek;

                            Console.WriteLine("The weekly pay as a pieceworker would be: " + pieceWeeklyPay.ToString("C"));
                            Console.WriteLine("Press any key to exit.");
                            Console.ReadKey();
                            Console.WriteLine("Exiting Program");
                            count = 10;

                        }
                        else if (payCode == 5)
                        {
                            Console.WriteLine("Exiting Program");
                            count = 10;

                        }

                    }
                    else
                    {
                        Console.WriteLine("");
                        Console.WriteLine("Invalid Selection, please try again.");
                        
                    }




                }

                catch
                {
                    Console.WriteLine("Invalid Input, Please try again.");
                    Console.WriteLine("");
                   
                }
            }
        }
    }
}
