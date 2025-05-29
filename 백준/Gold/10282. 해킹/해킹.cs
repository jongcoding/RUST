using System;
using System.Collections.Generic;

class Program
{
    const int INF = int.MaxValue;
    static void Main()
    {
        int T = int.Parse(Console.ReadLine()!);
        while(T-- > 0)
        {
            var line = Console.ReadLine()!.Split();
            int n = int.Parse(line[0]);
            int d = int.Parse(line[1]);
            int c = int.Parse(line[2]);

            var adj = new List<(int v, int w)>[n+1];
            for(int i = 0; i <= n; i++)
                adj[i] = new List<(int, int)>();

            for(int i = 0; i < d; i++)
            {
                var parts = Console.ReadLine()!.Split();
                int a = int.Parse(parts[0]);
                int b = int.Parse(parts[1]);
                int s = int.Parse(parts[2]);
                adj[b].Add((a, s));
            }

            var dist = new int[n+1];
            for(int i = 1; i <= n; i++) dist[i] = INF;
            dist[c] = 0;

            var pq = new PriorityQueue<(int t, int u), int>();
            pq.Enqueue((0, c), 0);

            while(pq.Count > 0)
            {
                var cur = pq.Dequeue();
                int t = cur.t, u = cur.u;
                if(t > dist[u]) continue;
                foreach(var edge in adj[u])
                {
                    int v = edge.v, w = edge.w;
                    int nt = t + w;
                    if(dist[v] > nt)
                    {
                        dist[v] = nt;
                        pq.Enqueue((nt, v), nt);
                    }
                }
            }

            int cnt = 0, last = 0;
            for(int i = 1; i <= n; i++)
            {
                if(dist[i] < INF)
                {
                    cnt++;
                    last = Math.Max(last, dist[i]);
                }
            }
            Console.WriteLine($"{cnt} {last}");
        }
    }
}
