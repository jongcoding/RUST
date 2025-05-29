import sys, math
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    n = int(input())
    v = n + 2

    xs = [0.0] * v
    ys = [0.0] * v
    rs = [0.0] * v
    xs[n+1], ys[n+1] = float(a), float(b)

    for i in range(1, n+1):
        x, y = map(int, input().split())
        xs[i], ys[i], rs[i] = float(x), float(y), 1.0

    INF = float('inf')
    dist = [INF] * v
    used = [False] * v
    dist[0] = 0.0
    for _ in range(v):

        u = min((dist[i], i) for i in range(v) if not used[i])[1]
        used[u] = True

        for w in range(v):
            if used[w]:
                continue
            dx = xs[u] - xs[w]
            dy = ys[u] - ys[w]
            d = math.hypot(dx, dy) - (rs[u] + rs[w])
            if d < 0:
                d = 0.0
            nd = dist[u] + d
            if nd < dist[w]:
                dist[w] = nd
    print(f"{dist[n+1]:.10f}")
if __name__ == "__main__":
    main()
