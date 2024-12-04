from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def BFS(root: Node, target: Node) -> int:
    queue = deque([root])  # ノードを保持するキュー
    visited = set()        # 訪問済みノードを追跡するセット
    visited.add(root)      # ルートノードを訪問済みに追加
    step = 0               # ルートから現在のノードまでのステップ数

    # BFS開始
    while queue:
        size = len(queue)  # 現在のキューのサイズを取得
        # 現在のキューにあるノードをすべて処理
        for _ in range(size):
            cur = queue.popleft()  # キューの先頭のノードを取得

            # ターゲットノードに到達したらステップ数を返す
            if cur == target:
                return step

            # 隣接ノードをすべて探索
            for next_node in cur.neighbors:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)

        # ステップを1増加
        step += 1

    return -1  # ルートからターゲットノードへのパスがない場合
