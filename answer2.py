N, M = map(int, input().split())
L = list(map(int, input().split()))

# 幅Wが達成可能か確認する関数
def judge(W):
    # 文字数
    moji = 0
    # 行数
    row = 1  # 最初の行をカウントするため1で初期化

    i = 0
    while i < N:
        # 次の単語を同じ行に配置できない場合
        if W < moji + L[i]:
            row += 1  # 行を増やす
            moji = 0  # 文字数をリセット

        # 次の単語を同じ行に配置できる場合
        if moji + L[i] <= W:
            moji += L[i] + 1  # 次の単語のために1を追加

        i += 1


    if row <= M:
        return True
    else:
        return False

good = max(L)  # 最小の横幅
bad = sum(L) + (N - 1) + 1  # 最大の横幅

# 二分探索
while abs(good-bad)>1:  # 1の差になったら終了
    mid = (good + bad) // 2
    if judge(mid):
        bad = mid  # 幅が達成可能なら右を更新
    else:
        good = mid  # 達成不可能なら左を更新

# 答えの出力
print(bad)  # 最小の横幅を出力
