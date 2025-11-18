import sys

input =sys.stdin.readline




def main():
    INF = 10**9
    C,N = map(int ,input().split())
    citis=[]
    
    for _ in range(N):
        a,b=map(int, input().split())
        citis.append((a,b))
    over=max(c for _,c in citis)
    length=C+over
    dp=[INF]*(length+1)
    dp[0]=0
    for a, b in citis:
        for i in range(1, length+1):
            if dp[i-b]+a<dp[i]:
                dp[i]=dp[i-b]+a

    print(min(dp[C:]))
if __name__ == "__main__":
    main()