W = int(input())
N,K = map(int,input().split())

A = []
B = []

for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[0] * (W+1) for _ in range(K+1)]

dp[0][0] = 0 # 

# dp[i][sum_w] := i-1 番目までの問題を解き、合計の得点が
# sum_p を超えないように(もしくは、ピッタリの時)選んだときの、

#dp[i][j] ← N個の整数のうち最初の i個の整数の中からいくつか選んだ総和を 
# jにできるかどうか


#dp [K][W] = K 枚以下、幅 W 以下

for i in range(N): # i 番目以下
    for j in range(K,-1,-1): # 大きい順に行う
        for k in range(W+1):
            # i を選ばない場合
            # dp[j][k] の値はそのまま dp[j][k]

            # i を選ぶ場合
            if j + 1 <= K and k + A[i] <= W:
                dp[j+1][k+A[i]] = max(dp[j+1][k+A[i]], 
                                      dp[j][k] + B[i])



ans=0
for j in range(K+1):
    for k in range(W+1):
        ans=max(ans,dp[j][k])

print(ans)

