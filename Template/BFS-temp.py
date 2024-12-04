DX = [1,-1,0,0]
DY = [0,0,1,-1]
#=====================================
H,W = map(int,input().split())

C_h,C_w = map(int,input().split())
D_h,D_w = map(int,input().split())

C_h -= 1
C_w -= 1
D_h -= 1
D_w -= 1

S = [ list(input()) for _ in range(H) ]

from collections import deque
INF = float('inf')
def BFS():
    
    dist = [[INF]*W for _ in range(H)]
    que = deque()

    # Start from the initial position with cost 0
    que.append((C_h,C_w,0))
    dist[C_h][C_w] = 0

    while len(que) > 0:

        x_now,y_now,cost = que.popleft()

        for dx,dy in zip(DX,DY):
            
            x_next = x_now + dx
            y_next = y_now + dy

            if x_next < 0 or y_next < 0 or x_next>=H or y_next >=W:
                continue
            if S[x_next][y_next] == '#':
                continue

            if dist[x_next][y_next] > cost:
                dist[x_next][y_next] = cost #dist[x_now][y_now]
                que.appendleft((x_next,y_next,cost)) # 通常移動は優先して探索する

        
         # Check teleport moves (after normal moves are processed)
        next_cost = cost + 1
        for dx in range(-2,3):
            for dy in range(-2,3):
                if dx ==0 and dy ==0:
                    continue

                x_next = x_now + dx
                y_next = y_now + dy

                if x_next < 0 or y_next < 0 or x_next >= H or y_next >= W:
                    continue
                
                if S[x_next][y_next] == '#':
                    continue

                if dist[x_next][y_next] > next_cost:
                    dist[x_next][y_next] = next_cost
                    que.append((x_next, y_next,next_cost))  # 魔法による移動は通常の移動よりも後に処理

   # print(dist)
    return dist[D_h][D_w] if dist[D_h][D_w] < float('inf') else -1


#for i in range(H):
#    for j in range(W):
#        if A[i][j] == '#':
#            X.append(i)
#            Y.append(j)


print(BFS())



############################
# ABC 327 D 

from collections import deque

def bfs(start, groups, adj):
    queue = deque([start])
    groups[start] = 0  # 初期グループを 0 に設定
# groups[v]: 頂点 v が現在どのグループ（0 または 1）に属しているかを示す

    while queue:
        v = queue.popleft()
        for neighbor in adj[v]:
            if groups[neighbor] == -1:  # まだ訪問していない場合
                groups[neighbor] = 1 - groups[v]  # 隣接する頂点を反対のグループに設定
                queue.append(neighbor)
            elif groups[neighbor] == groups[v]:  # 隣接する頂点が同じグループなら不可能
                return False
    return True

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1-indexed のため N+1 の配列を作成
adj = [[] for _ in range(N+1)]

# 隣接リストの作成
for i in range(M):
    adj[A[i]].append(B[i])
    adj[B[i]].append(A[i])

# 各頂点のグループを -1（未訪問）で初期化
groups = [-1] * (N + 1)
# groups[v]: 頂点 v が現在どのグループ（0 または 1）に属しているかを示す

# 全ての頂点で BFS を開始
for v in range(1, N+1):
    if groups[v] == -1:  # 未訪問の場合
        if not bfs(v, groups, adj):  # グループ 0 で BFS 開始
            print('No')
            exit()


print('Yes')

