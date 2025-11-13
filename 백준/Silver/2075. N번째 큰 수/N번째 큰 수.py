import sys
from collections import deque
import heapq


input=sys.stdin.readline
data=[]
def main():
    n= int(input())

    for _ in range(n):
        num_list=map(int ,input().split())

        for num in num_list:
            if len(data)<n:
                heapq.heappush(data, num)
            else:
                if data[0]<num:
                    heapq.heapreplace(data,num)
                
    print(data[0])


if __name__ == "__main__":
    main()

