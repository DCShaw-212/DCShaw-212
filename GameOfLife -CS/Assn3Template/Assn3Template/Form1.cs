//Name: Dustin Shaw
//Purpose: This program opens a window and runs iterations (user specified) based on the rules of conway's game of life





using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Assn3Template
{
    public partial class Form1 : Form
    {
        //Conway's game of Life


        const int PANEL_SIZE = 25;
        const int SQUARE_SIZE = 10;
        Panel[,] panelArray = new Panel[SQUARE_SIZE, SQUARE_SIZE];
        Color[,] colorArray = new Color[SQUARE_SIZE, SQUARE_SIZE];

        
        
        
            
        
        

        

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 0; i < SQUARE_SIZE; i++)
            {
                for (int j = 0; j < SQUARE_SIZE; j++)
                {
                    Panel nextPanel = new Panel();
                    panelArray[i, j] = nextPanel;
                    nextPanel.BackColor = Color.DarkGray;
                    nextPanel.Size = new Size(PANEL_SIZE, PANEL_SIZE);
                    nextPanel.Location = new Point(10 + (PANEL_SIZE + 10) * j, 10 + (PANEL_SIZE + 10) * i);
                    nextPanel.Click += new EventHandler(clickPanel);

                    ((Form)sender).Controls.Add(nextPanel);
                }

            }
        }

        private void clickPanel(object sender, EventArgs e)
        {
            //Cast Panel onto sender so that .BackColor can be accessed

            Panel startingHue = (Panel)(sender);

            //Condtional Statements to change starting color when clicked

            if (startingHue.BackColor == Color.DarkGray)
            {
                 startingHue.BackColor = Color.Green;
            }

            else
            {
                startingHue.BackColor = Color.DarkGray;
            }

            
        }

        private void btnOneIteration_Click(object sender, EventArgs e)
        {
            RunOneIteration();
        }

        public static bool IndicieTest(int i , int j)
        {
            // Conditional statements to test whether neighbors are within bounds

            if (i < 0 || j < 0)
            {
                return false;
            }

            else if (i >= SQUARE_SIZE || j >= SQUARE_SIZE)
            {
                return false;
            }
            else
            {
                return true;
            }

        }

        public void RunOneIteration()
        {
            


            Color[,] colorArray = new Color[SQUARE_SIZE, SQUARE_SIZE];


           

           
            
            
            
             


            //Check to see whether neighbors are green and within bounds of the array

            for (int i = 0; i < SQUARE_SIZE; i++)
            {
                for (int j =0; j < SQUARE_SIZE; j++)
                {
                    //Sets number of neighbors to 0

                    int neighbors = 0;

                    //Checks neighbor to the east

                        if (IndicieTest(i, j + 1))
                        {
                            if (panelArray[i,j+1].BackColor == Color.Green)
                            {
                                neighbors++;
                                
                            }

                        }
                        //Checks neighbor to the southeast
                        if (IndicieTest(i + 1, j +1))
                        {
                            if(panelArray[i + 1, j + 1].BackColor == Color.Green)
                            {
                                neighbors++;

                            }
                        }
                        //Checks neighbor to the south

                        if (IndicieTest(i + 1, j))
                        {
                            if(panelArray[i + 1, j].BackColor == Color.Green)
                            {
                                neighbors++;
                            }
                        }

                        //Checks neighbor to the southwest

                        if (IndicieTest(i + 1, j - 1))
                        {
                            if(panelArray[i + 1, j -1].BackColor == Color.Green)
                            {
                                neighbors++;
                            }
                        }

                        //Checks neighbor to the west

                        if (IndicieTest(i, j - 1))
                        {
                            if(panelArray[i,j-1].BackColor == Color.Green)
                            {
                                neighbors++;
                            }
                        }

                        //Checks neighbor to the northwest

                        if (IndicieTest(i - 1, j - 1))
                        {
                            if (panelArray[i-1,j-1].BackColor == Color.Green)
                            {
                                neighbors++;
                            }
                        }

                        //Checks neighbor to the north

                        if (IndicieTest(i -1 , j))
                        {
                            if(panelArray[i - 1, j].BackColor == Color.Green)
                            {
                                neighbors++;
                            }
                        }

                        //Checks neighbor to the northeast

                        if(IndicieTest(i - 1, j +1))
                        {
                            if(panelArray[i-1, j + 1].BackColor == Color.Green)
                            {
                                neighbors++;
                            }
                        }

                      


                        //Game Logic to change colors 

                        //Underpopulation death

                        if (panelArray[i , j].BackColor == Color.Green && neighbors < 2)
                        {
                            colorArray[i,j] = Color.DarkGray;
                        }

                        //Livin on a Prayer (Continues to next gen)

                        else if (panelArray[i,j].BackColor == Color.Green && neighbors == 2 || neighbors == 3)
                        {
                            
                            
                           colorArray[i,j] = Color.Green;
                            
                           
                        }

                        //OverPopulation Death

                        else if (panelArray[i,j].BackColor == Color.Green && neighbors > 3)
                        {
                            colorArray[i,j] = Color.DarkGray;
                        }

                        //Reproduction (Continues)

                        else if(panelArray[i,j].BackColor == Color.DarkGray && neighbors == 3)
                        {
                            colorArray[i,j] = Color.Green;
                        }

                        else
                        {
                            colorArray[i, j] = Color.DarkGray;
                        }

                        

                       
                        
                    
                    
                            
            }
                }
             
            
            // Sets the backcolor of panel to colorArray
            
            for (int i = 0; i < SQUARE_SIZE; i++)
                         {
                               for (int j = 0; j < SQUARE_SIZE; j++)
                               {
                    
                                panelArray[i , j].BackColor = colorArray[i, j];
                                    
                                 panelArray[i ,j].Refresh();
                    
                               }
                        }   

                
           
            
                
            }

        private void btnMultiIteration_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < numOfIteration.Value; i++)
            {
                RunOneIteration();

                System.Threading.Thread.Sleep(1000);

                Refresh();
            }
        }
    }
}
        
    

