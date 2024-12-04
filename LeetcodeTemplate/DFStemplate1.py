def dfs(cur, target, visited):
    # cur が target と一致する場合
    if cur == target:
        return True
    
    # cur の隣接ノードを訪問
    for next_node in cur.neighbors:  # 各隣接ノードを調べる
        if next_node not in visited:  # まだ訪れていない場合
            visited.add(next_node)  # 訪問済みにする
            # 再帰的に DFS を呼び出し、ターゲットを見つけたら True を返す
            if dfs(next_node, target, visited):
                return True
    
    # すべての隣接ノードを調べても見つからなかった場合
    return False

# 使用例
visited = set()  # 訪問したノードを保持
result = dfs(node_a, node_c, visited)
print(result)  # 出力: True
