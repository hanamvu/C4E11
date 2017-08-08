using System;

namespace HomeworkSS6
{
	class MainClass
	{
		public static void Main (string[] args)

		{	/*
			Excercise 2
			*/
			Console.Write ("Hello");
			Console.Write (",my name ");
			Console.Write ("is B-max");
			Console.WriteLine ();

			/*
			Excercise 1
			*/
			Console.WriteLine ("Hey bro, what's your name?\n");
			string dude_name = Console.ReadLine ();
			Console.WriteLine ("Wanna some joke? Let's begin!");

			Console.WriteLine ("How height you are? Give me your answear in centimeters please!");
			double	height = Convert.ToDouble(Console.ReadLine ());
			Console.WriteLine ("Excuse me, but how about your weight? This is a private question.");
			int	weight = Convert.ToInt32(Console.ReadLine ());

			float	BMI = weight / (long)Math.Pow ((height / 100), 2);
			if (BMI < 16) {
				Console.WriteLine ("Hollyshit {0}, YOU ARE SERVERELY UNDERWEIGHT!", dude_name);
			} else {
				if (BMI < 18.5) {
					Console.WriteLine ("{0}, you're underweight bro, buy Appeton Weight Gain Milk now!", dude_name);
				}
				else  {
					if (BMI < 25) {
						Console.WriteLine ("Hey {0}.Normal. How?", dude_name);
					}
						else {
							if (BMI < 30) {
								Console.WriteLine ("Hmm, Overload, Overweight, {0} !", dude_name);
							}
							else{
							Console.WriteLine ("What can i say, you're like BigMom {0}. Obese! !", dude_name);
							}
						}

					}
				}

			/*
			Excercise 3
			*/
			PrintStar fuctPrint = new PrintStar ();
			fuctPrint.rows = 9;
			fuctPrint.stars = 16;
			fuctPrint.printStar (fuctPrint.stars, fuctPrint.rows);

			}
					
		}

}
