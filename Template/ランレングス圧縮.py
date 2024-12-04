##ABC329 C

n = int(input())
s = input()

mx = [0] * 26  # 26文字のためのリストを初期化
l = 0

while l < n:
    r = l + 1
    while r < n and s[l] == s[r]:
        r += 1
    c = ord(s[l]) - ord('a')  # 文字をインデックスに変換
    mx[c] = max(mx[c], r - l)  # 最大連続数を更新
    l = r

ans = sum(mx)  # mx の合計を計算
print(ans)
