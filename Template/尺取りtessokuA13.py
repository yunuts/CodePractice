N,K=map(int,input().split())
A=list(map(int,input().split()))

R = 0
ans = 0


#しゃくとり法

for i in range(N):

    while R < N and A[R] - A[i] <= K:
        R += 1

    ans += (R-i-1)

print(ans)

##360D 
N,T = map(int,input().split())

S = input()

X = list(map(int,input().split()))

right = []
left = []

# 正を向いているあり
for i in range(N):
    if S[i] == '1':
        right.append(X[i])
    elif S[i] == '0':
        left.append(X[i])

right.sort()
left.sort()

#print(right,left)

#尺取り

R = 0
ans = 0
L = 0
#左側
for i in range(len(right)):
    
    while R < len(left) and left[R] - right[i] < 0:
        R += 1

    while L < len(left) and left[L] - right[i] <= T*2:
        L += 1

    ans += L-R

print(ans)