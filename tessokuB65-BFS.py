N,T = map(int,input().split())

connect=[ [] for _ in range(N+1)]

for _ in range(N-1):
    A,B = map(int,input().split())
    connect[A].append(B)
    connect[B].append(A)

#print(connect)

from collections import deque
que = deque()
que.append(T)

visited = [False] *(N+1)
visited[T] = True

dist = [0] *(N+1)

while que:
    now = que.popleft()
    
    for to in connect[now]:
        if not visited[to]:
            dist[to] = dist[now] + 1
            visited[to] = True
            que.append(to)
#頂点Tからの距離を求めた
#print(dist[1:])

#距離の大きい順にソートする
nodes = [(dist[i],i) for i in range(1,N+1) ]
nodes.sort(reverse=True)
#print(nodes)

# 動的計画法
dp = [0] *(N+1)
visited = [False] *(N+1)

for _, now in nodes:

    visited[now] = True
    for to in connect[now]:
        if not visited[to]:
            dp[to] = max(dp[to], dp[now] + 1)

print(*dp[1:])
#=====================================
