import heapq

n=int(input())

heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap, data)

result=0

while len(heap)!=1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    c=a+b
    result+=c
    heapq.heappush(heap, c)

print(result)
