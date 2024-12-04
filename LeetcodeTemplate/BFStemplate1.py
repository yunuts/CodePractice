from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def BFS(root: Node, target: Node) -> int:
    queue = deque()  # ノードを保持するキューを作成
    queue.append(root)  # ルートノードをキューに追加
    step = 0  # ルートから現在のノードまでのステップ数

    # BFS開始
    while queue:
        size = len(queue)  # 現在のキューのサイズを取得
        # 現在のキューにあるノードをすべて処理
        for _ in range(size):
            cur = queue.popleft()  # キューの最初のノードを取得
            if cur == target:
                return step  # ターゲットノードに到達したらステップ数を返す
            
            # 隣接ノードをすべて探索
            for next_node in cur.neighbors:
                queue.append(next_node)
        
        step += 1  # ステップを増加

    return -1  # ルートからターゲットノードへのパスがない場合
