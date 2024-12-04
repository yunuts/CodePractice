#ABC 362 D
import heapq
import sys
input = sys.stdin.readline

def dijkstra(G,s): # s = start
    INF = 10**18
    dist = [INF] * N

    dist[s] = 0
    pq = [(0,s)] # (distant,vertex)

    while pq:
        d,v = heapq.heappop(pq)
        if d > dist[v]:
            continue

        for u, weight in G[v]:
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heapq.heappush(pq,(nd,u))
    
    return dist


N,M = map(int,input().split())

A = list(map(int,input().split()))

G = [[] for _ in range(N)]

for i in range(M):
    U,V,B = map(int,input().split())
    U -= 1
    V -= 1
    G[U].append((V,B+A[V]))
    G[V].append((U,B+A[U]))

dist = dijkstra(G,0)

for i in range(N):
    dist[i] += A[0]

print(*dist[1:])


###########  ABC340

import heapq

def dijkstra(G,s):
    INF = float('inf')
    dist = [INF] * (N+1)

    dist[s] = 0
    pq = [(0,s)] # (distant,vertex)

    while pq:
        d,v = heapq.heappop(pq)
        if d > dist[v]:
            continue

        for u ,weight in G[v]:
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heapq.heappush(pq,(nd,u))
    
    return dist

N = int(input())

G = [[] for _ in range(N+1)] # 1からNまでを使う

for i in range(1,N):
    A,B,X = map(int,input().split())

    G[i].append((i+1,A))
    #G[i+1].append((i,A))
    G[i].append((X,B))
    #G[X].append((i,B))

dist =dijkstra(G,1)


print(dist[N])

##############3tessokuA64
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

import heapq
que=[]
heapq.heappush(que,(dist[1],1))


while que:
    
    now = heapq.heappop(que)[1]

    if visited[now] == True:
        continue
    visited[now] = True

    for next in G[now]:

        if dist[next[0]] > dist[now] + next[1]:
            dist[next[0]] = dist[now] + next[1]
            heapq.heappush(que,(dist[next[0]],next[0]))
    

for i in range(1,N+1):
    if dist[i] != INF:
        print(dist[i])
    else:
        print(-1)



###340 D
import heapq

def dijkstra(G,s):
    INF = float('inf')
    dist = [INF] * (N+1)

    dist[s] = 0
    pq = [(0,s)] # (distant,vertex)

    while pq:
        d,v = heapq.heappop(pq)
        if d > dist[v]:
            continue

        for u ,weight in G[v]:
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heapq.heappush(pq,(nd,u))
    
    return dist

N = int(input())

G = [[] for _ in range(N+1)] # 1からNまでを使う

for i in range(1,N):
    A,B,X = map(int,input().split())

    G[i].append((i+1,A))
    #G[i+1].append((i,A))
    G[i].append((X,B))
    #G[X].append((i,B))

dist =dijkstra(G,1)


print(dist[N])