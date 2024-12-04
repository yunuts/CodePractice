N,M = map(int,input().split())

G= [ [] for _ in range(N+1) ]

for _ in range(M):
    A,B,C =map(int,input().split())
    G[A].append((B,C))
    G[B].append((A,C))



INF = float('inf')
visited = [False] * (N+1)
dist = [INF] *(N+1)
dist[1]=0

while True:
    now = -1
    minDist = INF
    
    for i in range(1,N+1):
        if visited[i] == False and minDist > dist[i]:
    
            now = i
            minDist = dist[i]

    if now == -1:
        break

    visited[now] = True
    for next, cost in G[now]:
        dist[next] = min(dist[next],dist[now]+cost)

print(*dist[1:] , sep='\n')