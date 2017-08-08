using System;

namespace HomeworkSS6
{
	public class PrintStar
	{
		public int stars;
		public int rows;
		public PrintStar ()
		{
		}
		public void printStar(int stars,int rows)
		{
			Console.WriteLine ("Print {0}  stars!", stars);

			for (int i=0;i<stars;i++) {
				Console.Write ("*");
			}
			Console.WriteLine ();
			Console.WriteLine ("----------------------------------------");			

			Console.WriteLine ("Print {0} (stars and xs) x {1} row ", stars, 1);
			for (int i=0;i<stars;i++) {
				Console.Write ("x*");
			}
			Console.WriteLine ();
			Console.WriteLine ("----------------------------------------");	

			Console.WriteLine ("Print {0} (stars and xs) x {1} rows !",stars, rows);
			for (int i=0;i<rows;i++) {
				for (int j = 0; j < stars; j++) {
					if (i % 2 == 0) {
						Console.Write ("x*");
					} else {
						Console.Write ("*x");
					}

				}
				Console.WriteLine ();
			}

		}
	}
}

