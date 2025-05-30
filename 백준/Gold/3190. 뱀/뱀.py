import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
k=int(input())
data=[[0]*(n+1) for _ in range(n+1)]
info=[]
for _ in range(k):
    a,b=map(int, input().split())
    data[a][b]=1
l=int(input())
for _ in range(l):
    x,c=input().split()
    info.append((int(x),c))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(dir, c):
    if c=="L":
        dir=(dir-1)%4
    else:
        dir=(dir+1)%4
    return dir

def simulate():
    x,y=1,1
    data[x][y]=2
    dir=0
    time=0
    index=0
    q=deque([(x,y)])
    while True:
        nx=x+dx[dir]
        ny=y+dy[dir]

        if 1<=nx and nx<=n and 1<=ny and ny <=n and data[nx][ny]!=2:
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx,ny))
                px,py= q.popleft()
                data[px][py]=0
            if data[nx][ny]==1:
                data[nx][ny]=2
                q.append((nx,ny))
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1
        if index <len(info) and time==info[index][0]:
            dir=turn(dir,info[index][1])
            index+=1
    return time
print(simulate())