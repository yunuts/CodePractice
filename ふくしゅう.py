from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 次と前のスロットの変換を定義
        next_slot = {str(i): str((i + 1) % 10) for i in range(10)}
        prev_slot = {str(i): str((i - 1) % 10) for i in range(10)}
        
        # 死んだ組み合わせと訪問済みの組み合わせをセットに格納
        visited_combinations = set(deadends)
        
        # 初期状態が死んだ状態の場合はすぐに-1を返す
        if "0000" in visited_combinations:
            return -1
        
        # BFS用のキュー
        pending_combinations = deque(["0000"])
        visited_combinations.add("0000")
        
        # 回数
        turns = 0

        while pending_combinations:
            # 現在のレベルのノード数（探索する組み合わせ数）
            curr_level_nodes_count = len(pending_combinations)

            for _ in range(curr_level_nodes_count):
                current_combination = pending_combinations.popleft()
                
                # 目標に達した場合、回数を返す
                if current_combination == target:
                    return turns
                
                # 各ホイールを進めるか戻す
                for wheel in range(4):
                    for direction in [next_slot, prev_slot]:
                        new_combination = list(current_combination)
                        new_combination[wheel] = direction[new_combination[wheel]]
                        new_combination_str = "".join(new_combination)

                        # 新しい組み合わせが未訪問かつ死んでいない場合、キューに追加
                        if new_combination_str not in visited_combinations:
                            pending_combinations.append(new_combination_str)
                            visited_combinations.add(new_combination_str)

            # 1ターン進んだので回数を増加
            turns += 1

        return -1
