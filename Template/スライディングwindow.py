N,M = map(int,input().split())
A= list(map(int,input().split()))

A.sort()

r = 0
ans = 0
for l in range(N):
    while r < N and A[r] < A[l] + M:
        r += 1

    cnt = r - l

    ans = max(ans,cnt)

print(ans)