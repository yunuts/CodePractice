import sys
sys.setrecursionlimit(10**6)

N,T = map(int,input().split())

connect=[ [] for _ in range(N+1)]

for _ in range(N-1):
    A,B = map(int,input().split())
    connect[A].append(B)
    connect[B].append(A)

print(connect)

rank = [0] * (N+1)
def DFS(parent: int, now: int) -> int:

    for to in connect[now]:
        if to == parent:
            continue

        # now の 数字を元にして、to へ潜っていく
        rank_tmp = DFS(now,to) + 1

        if rank[now] < rank_tmp:
            rank[now] = rank_tmp

    return rank[now]


DFS(-1,T)
print(*rank)