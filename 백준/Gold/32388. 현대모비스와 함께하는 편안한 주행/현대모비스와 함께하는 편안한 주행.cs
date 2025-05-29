using System;

class Program
{
    static void Main()
    {
        var parts = Console.ReadLine()!.Split();
        long a = long.Parse(parts[0]);
        long b = long.Parse(parts[1]);
        int n = int.Parse(Console.ReadLine()!);

        int V = n + 2;

        double[] xs = new double[V];
        double[] ys = new double[V];
        double[] rs = new double[V];

        xs[0] = 0.0; 
        ys[0] = 0.0; 
        rs[0] = 0.0;

        xs[V-1] = a;
        ys[V-1] = b;
        rs[V-1] = 0.0;

        for (int i = 1; i <= n; i++)
        {
            parts = Console.ReadLine()!.Split();
            xs[i] = double.Parse(parts[0]);
            ys[i] = double.Parse(parts[1]);
            rs[i] = 1.0;
        }

        const double INF = double.PositiveInfinity;
        double[] dist = new double[V];
        bool[] used = new bool[V];
        for (int i = 0; i < V; i++)
            dist[i] = INF;
        dist[0] = 0.0;

        for (int iter = 0; iter < V; iter++)
        {
            int u = -1;
            double best = INF;
            for (int i = 0; i < V; i++)
            {
                if (!used[i] && dist[i] < best)
                {
                    best = dist[i];
                    u = i;
                }
            }
            if (u == -1) break;
            used[u] = true;

            for (int v = 0; v < V; v++)
            {
                if (used[v]) continue;
                double dx = xs[u] - xs[v];
                double dy = ys[u] - ys[v];
                double d = Math.Sqrt(dx * dx + dy * dy) - (rs[u] + rs[v]);
                if (d < 0) d = 0.0;
                double nd = dist[u] + d;
                if (nd < dist[v])
                    dist[v] = nd;
            }
        }

        Console.WriteLine(dist[V-1].ToString("F10"));
    }
}
