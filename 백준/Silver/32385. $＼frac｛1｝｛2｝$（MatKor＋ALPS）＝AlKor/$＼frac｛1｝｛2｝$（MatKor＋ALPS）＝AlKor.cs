using System;
using System.Text;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine()!);
        long S = (long)(N - 1) * N / 2;

        var sb = new StringBuilder();
        for (int i = 1; i < N; i++)
        {
            sb.Append(i).Append(' ');
        }
        sb.Append(-S).Append(' ').Append(0);

        Console.WriteLine(sb.ToString());
    }
}
