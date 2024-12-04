N,M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

INF = float('inf')

# DPテーブルの初期化
# dp[i][j]: i日目に都市jにいるときの疲労度の最小値
dp = [[INF] *  (N+1) for _ in range(M+1)]
# 初期化
dp[0][0] = 0 

# DPテーブルの更新
for i in range(M):
    for j in range(N):
        # 待機する場合
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        # 移動する場合
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + D[j]*C[i])


tmp=INF
for i in range(M+1):
    result = min(tmp,dp[i][N])
    tmp = result

#result = min(dp[i][N] for i in range(M+1))

print(result)