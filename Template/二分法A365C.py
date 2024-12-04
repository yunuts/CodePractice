
#参考
#https://zenn.dev/forcia_tech/articles/20191223_advent_calendar

def func(x, A):
    return sum(min(x, a) for a in A)


N,M=map(int,input().split())
A=list(map(int,input().split()))

if sum(A)<=M:
    print('infinite')
else:
    ok=0 < - ここを A[0] とすると通らない。　条件を確実に満たすゾーンではないから。
    ng=max(A)
    while abs(ok- ng)>1:
        mid=(ok+ng)//2
        tmp = func(mid,A)
        if tmp <= M:
            ok = mid
        else:
            ng = mid

    print(ok)
        
#=======================
#ABC334D
N,Q = map(int,input().split())
R = list(map(int,input().split()))

R.sort()

sum_r = [0]*(N+1)

for i in range(N):
    sum_r[i+1] = sum_r[i] + R[i]
#print(R)
#print(sum_r)


ok = 0
bad = N+1

def is_ok(mid,x):
    return sum_r[mid] <= x

for i in range(Q):
    x = int(input())

# 2分法
    ok = 0
    bad = N+1
    while abs(ok-bad)>1:
        mid = (ok+bad)//2
        
        if is_ok(mid,x):
            ok = mid
        else:
            bad = mid
    
    #print('---->',ok,bad)
    print(ok)


