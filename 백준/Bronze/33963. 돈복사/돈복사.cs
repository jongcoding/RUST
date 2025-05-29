using System;

class Program
{
    static void Main()
    {
        long n = long.Parse(Console.ReadLine()!);

        int d = n.ToString().Length;
 
        long threshold = 1;
        for (int i = 0; i < d; i++)
            threshold *= 10;

        int count = 0;

        while (n*2 < threshold)
        {
            n *= 2;
            count++;
        }

        Console.WriteLine(count);
    }
}
