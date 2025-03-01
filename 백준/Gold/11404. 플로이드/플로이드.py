import sys
input=sys.stdin.readline

v=int(input())
e=int((input()))
inf=float('inf')
graph=[[inf] * (v+1) for _ in range(v+1)]

for _ in range(e):
    src,dst,weight=map(int, input().split())
    graph[src][dst] = min(graph[src][dst], weight)


for k in range(1, v+1):
    graph[k][k]=0
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j]= min (graph[i][j], graph[i][k]+graph[k][j])


for i in range(1, v+1):
    for j in range(1, v + 1):
        print(0 if graph[i][j] == inf else graph[i][j], end=" ")
    print()
    