import sys

n = int(sys.stdin.readline())
a = list(range(1, n))
s = (n-1)*n//2
a.append(-s)
a.append(0)
print(*a)

