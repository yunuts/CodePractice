def dfs(v, seen, res):
    end = True
    # seen = [True, False, False]　各頂点を調べたかどうか
    for i in range(len(seen)):
        if not seen[i] and i != v:
            end = False
#もしすべての頂点が訪問されている場合
#、つまり探索が終了した場合は、res リストの最初の要素に1を加算し
#、関数を終了します。
    if end:
        res[0] += 1
        return

    seen[v] = True
    for nv in G[v]:
        if seen[nv]:
            continue
        dfs(nv, seen, res)
    seen[v] = False

if __name__ == "__main__":
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    seen = [False] * N
    res = [0]
    dfs(0, seen, res)
    print(res[0])



N,M = map(int,input().split())

G = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    if a == b:
        continue
    a -= 1
    b -= 1
    if a in G[b] and b in G[a]:
        continue
    G[a].append(b)
    G[b].append(a)

print(G)
G_0 = G[0]
ng_list = [0]
for g_0 in G[0]: 
    if any(g_0 in G[j] for j in range(N)):
        if j not in ng_list:
            


'''
N,Q = map(int,input().split())

G = [set() for i in range(N)]
ans = [[] for i in range(N)]
for i in range(Q):
    num, s_1, *s_2 = map(int,input().split())

    if num == 1:
        s_1 -= 1
        s_2[0] -= 1
        G[s_1].add(s_2[0])
    
    elif num == 2:
        s_1 -= 1
        for i in range(N):
            if s_1 in G[i]:
                G[s_1].add(i)
    else:
        s_1 -= 1
        temp = set()
        for x in G[s_1]:
           # print('x',x,G[s_1],s_1)
            for x_f in G[x]:
                if x_f != s_1:
                    temp.add(x_f)
        G[s_1].update(temp)
 #  print(i,G)
#print(G)

for i in range(N):
    for j in range(N):
        if j in G[i]:
            ans[i].append('Y')
        else:
            ans[i].append('N')

    print(''.join(ans[i]))
'''


'''def only(iterable):
    for element in iterable:
        if '''


'''
N,M = map(int,input().split())
H=list(map(int,input().split()))

G = [[] for i in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

#print(G)


cnt = 0
for i in range(N):
    is_greater = all( H[x] < H[i] for x in G[i])
    if is_greater:
        cnt += 1
print(cnt)
'''


'''
G = [[] for i in range (N)]


for i in range(M):
    a,b = map(int,input().split())
    
    a -= 1
    b -= 1

    G[a].append(b)
    G[b].append(a)

#print(G)
for G_i in G:
    print(len(G_i))

'''
'''
N,M,Q = map(int,input().split())

G = [[] for i in range(N)]

for i in range(M):
    u,v = map(int,input().split())

    #頂点番号を0始まりにする
    u -= 1
    v -= 1

    G[u].append(v)
    G[v].append(u)

col = list(map(int,input().split()))

for i in range(Q):
    t,x,*y =map(int,input().split())
 #   print('here',t,x,y)

#頂点番号を0始まりにする
    x -= 1
    

    print(col[x])

    if t == 1:
        for v in G[x]:
            col[v] = col[x]

    else:
        col[x] = y[0]

#print(G)

'''