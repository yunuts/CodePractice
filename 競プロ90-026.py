
import sys
sys.setrecursionlimit(10**9)
N = int(input())
connect = [set() for i in range(N)]
for i in range(N-1):
        A,B = map(int,input().split())
        A -= 1
        B -= 1
        connect[A].add(B)
        connect[B].add(A)

colors = [-1] * N

def DFS(now,color):
    colors[now] = color
    for neighbor in connect[now]:
        if colors[neighbor] == -1 : #訪問されていない場合   
            DFS(neighbor,1 - color)


DFS(1,0)

#色分けされた頂点を確認する
color_0 = [i +1 for i, c in enumerate(colors) if c == 0]
color_1 = [i +1 for i, c in enumerate(colors) if c == 1]

#print(color_0,color_1)
#色分けされた頂点から頂点を選ぶ
if len(color_0) >= N // 2:
    print(*color_0[: N // 2])
else:
    print(*color_1[: N // 2])



'''#DFSが終わった後、すべての頂点が訪問されたかを確認します。
#すべての頂点が訪問されていなければ、その辺を取り除くとグラフが連結でなくなるので、
#その辺は「橋」です。


import sys
sys.setrecursionlimit(10**6)
N, M = map (((input()
path_dat = [list(map(int, input().split())) for _ in range(M)]


def DFS(now,visited,connect):
    visited[now] = True
    for to in connect[now]:
        if visited[to] == False : #訪問されていない場合   
            DFS(to,visited,connect)


result = 0
for i in range(M):

#グラフを外して考える

    in_use = path_dat[:i] + path_dat[i+1:]

    connect = [[] for _ in range(N)]
    for a,b in in_use:
        a -= 1
        b -= 1
        connect[a].append(b)
        connect[b].append(a)

    visited = [False] * N
    DFS(0,visited,connect)


    if not all(visited):
        result += 1
print(result)'''


'''
connect = [[] for i in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    connect[A].append(B)

#print(connect)
from collections import deque
def BFS(start_city):
    # start_city から start_city には必ずいける
    cnt = 1 
    # 訪問済み都市リスト
    visited = [False] * N
    visited[start_city] = True

    que = deque()

    que.append(start_city)
#que が空になるまで行う
    while 0 < len(que):
        ## 今いる都市
        now_city = que.popleft()
       
        for to_city in connect[now_city]:
        
            if visited[to_city] == False:
                cnt += 1
                # to_city を訪問済みにする
                visited[to_city] = True
                # キューへ追加
                que.append(to_city)

    return cnt

ans = 0
for x in range(N):
    ans+=BFS(x)

print(ans)'''