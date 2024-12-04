N, M = map(int, input().split())

# グラフの初期化
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1  # 0-indexedに変換
    B -= 1  # 0-indexedに変換
    G[A].append((B, C))  # 双方向の道路
    G[B].append((A, C))

# DFSを使用して最大距離を計算する関数
def dfs(node, current_distance, visited):
    visited[node] = True  # 現在のノードを訪問済みにする
    max_distance = current_distance  # 現在の距離を記録

    for neighbor, length in G[node]:
        if not visited[neighbor]:  # 訪問していないノードにのみ移動
            # 隣接ノードに移動し、距離を加算
            max_distance = max(max_distance, dfs(neighbor, current_distance + length, visited))

    visited[node] = False  # 他の経路探索のために訪問状態をリセット
    return max_distance

ans = 0
# 各街からスタート
for v in range(N):
    visited = [False] * N  # 訪問状態をリセット
    tmp = dfs(v, 0, visited)  # vからスタート
    ans = max(ans, tmp)  # 最大距離を更新

print(ans)


#####
# pypyで提出

# 再帰回数上限を10^6へ変更(再帰関数を使うときはとりあえず書いておく)
import sys
sys.setrecursionlimit(10**6)

# 入力の受け取り
N,M=map(int, input().split())

# 繋がっている頂点の情報を受け取り
connect=[[] for i in range(N+1)]
# M回
for i in range(M):
    # 入力の受け取り
    A,B,C=map(int, input().split())
    # A→Bへは長さC
    connect[A].append([B,C])
    # B→Aへは長さC
    connect[B].append([A,C])

# 答え
ans=0

# DFS
# now：今いる街　dist：スタートから今いる街までの距離
def DFS(now,dist):
    # ansを更新できるように
    global ans
    # 答えを更新
    ans=max(dist,ans)

    # 今いる街から行ける街(to)とその距離(cost)を順に代入
    for to,cost in connect[now]:
        # 次に行ける街にまだ訪問していなければ
        if visited[to]==False:
            # 訪問済みにする
            visited[to]=True
            # 次の街へ
            DFS(to,dist+cost)
            # 戻ってきたら訪問済みを取り消す
            visited[to]=False

# start=1~N
for start in range(1,N+1):
    # 訪問済みかを確認するリスト
    visited=[False]*(N+1)
    # スタート地点を訪問済みにする
    visited[start]=True
    # スタート地点から開始
    DFS(start,0)

# 答えの出力
print(ans)
