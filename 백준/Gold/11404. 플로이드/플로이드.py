import sys
input = sys.stdin.readline

v = int(input().strip())  # 도시 수
e = int(input().strip())  # 버스 노선 수

inf = float('inf')
graph = [[inf] * (v + 1) for _ in range(v + 1)]

# 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1, v + 1):
    graph[i][i] = 0

# 간선 정보 입력 (중복 간선 처리)
for _ in range(e):
    src, dst, weight = map(int, input().split())
    graph[src][dst] = min(graph[src][dst], weight)  # 중복 간선 중 최소 비용 저장

# 플로이드-워셜 알고리즘 수행
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if graph[i][k] != inf and graph[k][j] != inf:  # inf + 숫자 = overflow 방지
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력 (갈 수 없는 경우 0으로 출력)
for i in range(1, v + 1):
    for j in range(1, v + 1):
        print(0 if graph[i][j] == inf else graph[i][j], end=" ")
    print()
