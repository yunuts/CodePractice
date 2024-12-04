N, W = 3, 4
w = [2, 1, 3]
v = [3, 2, 4]

def rec(n, sw, sv):
    if n == N:
        return sv
    
    result = 0  # 初期化

    # 物を選ばない場合
    score = rec(n + 1, sw, sv)
    result = max(result, score)

    # 物を選ぶ場合
    if sw + w[n] <= W:
        score = rec(n + 1, sw + w[n], sv + v[n])
        result = max(result, score)

    return result

# 初期条件で関数を呼び出す
print(rec(0, 0, 0))
#####################################################################

INF = 2** 60

N = int(input())
h = list(map(int,input().split()))

def rec(i):
    if i==0:
        return 0
    
    result = INF

    if i-1 >=0:
        result = min(result, rec(i-1) + abs(h[i] - h[i-1]))

    if i-2 >= 0:
        result = min(result, rec(i-2) + abs(h[i]-h[i-2]))

    return result

print(rec(N-1))

#####################################################################

INF = 2** 60

N = int(input())
h = list(map(int,input().split()))


result = INF
def rec(i):
    if i==0:
        return 0

    if i-1 >=0:
        result = min(result, rec(i-1) + abs(h[i] - h[i-1]))

    if i-2 >= 0:
        result = min(result, rec(i-2) + abs(h[i]-h[i-2]))

    return result

print(rec(N-1))

INF = 2** 60

N = int(input())
h = list(map(int,input().split()))

dp =[INF] * N

dp[0] = 0

for i in range(N):
    if i-1 >= 0:
        dp[i] = min(dp[i],dp[i-1]+abs(h[i]-h[i-1]))

    if i-2 >= 0:
        dp[i] = min(dp[i],dp[i-2]+abs(h[i]-h[i-2]))

print(dp[N-1])

=======================================================

N = int(input())

x=[]
y=[]
h=[]


G=(-1)*3
for i in range(N):
    xt,yt,ht = map(int,input().split())
    x.append(xt)
    y.append(yt)
    h.append(ht)
    if ht>1:
        G = (xt,yt,ht)

ans=[]

for i in range(101):
    for j in range(101):
        #仮の高さを計算
        V = G[2] + abs(G[0]-i) + abs(G[1]-j) 
        V = max(V,0)
        for k in range(N):
            VV = V - abs(X[k]-i) - abs(Y[k]-j)
            VV = max(VV,0)
            if H[k] != VV:
                flag= False
                break
        if flag:
            ans.append((i,j,V))

print(cx,cy,H)

=====================================================================
import math
N= int(input())
A=list(map(int,input().split()))

s=[0]*(N+1)
from collections import defaultdict
nums=defaultdict(int)

for i in range(N):
    num = A[i]
    #answer=[i for i in range(1,num+1) if num%i ==0]
    for i in range(1,int(math.sqrt(num)) + 1):
        if num % i ==0:
            nums[i] += 1
            if i!= num // i:
                nums[num//i] += 1 

#    for j in range(len(answer)):
#        nums[answer[j]] += 1


max_num = -1
for key in nums:
    if nums[key] == 2:
        max_num = max(max_num, key)

print(max_num)

