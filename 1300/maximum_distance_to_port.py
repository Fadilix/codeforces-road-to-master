from collections import defaultdict, deque
import sys

n, m, k = map(int, sys.stdin.readline().split())
cities = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)

port = cities[0]

for i in range(1, m + 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * (n + 1)
dist[1] = 0

q = deque([1])

while q:
    node = q.popleft()
    for nei in graph[node]:
        if dist[nei] == -1:
            dist[nei] = dist[node] + 1
            q.append(nei)

result = [0] * (k + 1)


for city in range(1, n + 1):
    ptype = cities[city - 1]
    result[ptype] = max(result[ptype], dist[city])

print(*result[1:])
