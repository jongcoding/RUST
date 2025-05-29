using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        var sw = new StreamWriter(Console.OpenStandardOutput());
        string[] parts = sr.ReadLine().Split();
        int N = int.Parse(parts[0]);
        int M = int.Parse(parts[1]);
        var graph = new List<int>[N + 1];
        for (int i = 1; i <= N; i++)
            graph[i] = new List<int>();

        for (int i = 0; i < M; i++)
        {
            parts = sr.ReadLine().Split();
            int A = int.Parse(parts[0]);
            int B = int.Parse(parts[1]);
            graph[B].Add(A);
        }

        int[] visited = new int[N + 1];
        int mark = 0;
        int[] reachCount = new int[N + 1];
        int[] queue = new int[N + 1];

        for (int start = 1; start <= N; start++)
        {
            mark++;
            int head = 0, tail = 0;
            visited[start] = mark;
            queue[tail++] = start;
            int cnt = 1;

            while (head < tail)
            {
                int u = queue[head++];
                foreach (int v in graph[u])
                {
                    if (visited[v] != mark)
                    {
                        visited[v] = mark;
                        queue[tail++] = v;
                        cnt++;
                    }
                }
            }

            reachCount[start] = cnt;
        }

        int maxCnt = 0;
        for (int i = 1; i <= N; i++)
            if (reachCount[i] > maxCnt)
                maxCnt = reachCount[i];

        for (int i = 1; i <= N; i++)
        {
            if (reachCount[i] == maxCnt)
                sw.Write(i + " ");
        }
        sw.Flush();
    }
}
