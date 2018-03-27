namespace Car
{
    class TupleXY
    {
        public int _x;
        public int _y;

        public TupleXY(int x, int y)
        {
            _x = x;
            _y = y;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            testCar();
            Console.WriteLine("Complete!");
            Console.ReadKey();
        }

        public static void testCar()
        {
            int speed = 10;
            int radius = 10;
            int fidelity = 10;
            List<TupleXY> listCoordinates = genCircle(radius, fidelity);
            drive(listCoordinates, speed);
        }

        public static List<TupleXY> genCircle(int radius, int fidelity)
        {
            List<TupleXY> list = new List<TupleXY>();
            for (int i = 0; i < fidelity; i++)
            {
                double t = 2 * Math.PI * i / fidelity;
                int x = (int)Math.Round(radius * Math.Cos(t));
                int y = (int)Math.Round(radius * Math.Sin(t));
                TupleXY tup = new TupleXY(x, y);
                list.Add(tup);
            }
            return (list);
        }

        public static void drive( List<TupleXY> list, int speed)
        {
            double degreePrior = 0.0;
            TupleXY tupPrior = new TupleXY(0, 0);
            foreach ( TupleXY tup in list )
            {
                double degree = calcDegree(tupPrior._x, tupPrior._y, tup._x, tup._y);
                double dist = calcDistance(tupPrior._x, tupPrior._y, tup._x, tup._y);
                turn(degreePrior, degree, dist, speed);
                tupPrior = tup;
                degreePrior = degree;
            }
        }

        public static double calcDistance(int x1, int y1, int x2, int y2)
        {
            double deltaX = x2 - x1;
            double deltaY = y2 - y1;
            double dist = Math.Sqrt((deltaX * deltaX) + (deltaY * deltaY));
            return (dist);
        }

        public static double calcDegree( int x1, int y1, int x2, int y2 )
        {
            double deltaX = x2 - x1;
            double deltaY = y2 - y1;
            double rad = Math.Atan2(deltaY, deltaX);
            double deg = rad * (180 / Math.PI);
            if (deg < 0) deg = 360 + deg;
            return (deg);
        }

        public static void turn( double degreeCurrent, double degree, double distance, int speed )
        {
            Console.WriteLine("Current Degree: " + degreeCurrent);
            Console.WriteLine("Degree: " + degree);
            Console.WriteLine("Distance: " + distance);
            Console.WriteLine("Speed: " + speed);
        }
	}
}