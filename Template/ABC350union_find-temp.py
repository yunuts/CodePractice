class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:  # 1. 自分自身が親の場合（つまりルート）
            return x             # 2. 自分が属するグループのルートを返す
        else:
            # 3. 自分が親でない場合、再帰的に親をたどり、ルートを見つける
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮も行う
            return self.parent[x]  # 4. ルートを返す

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                #rootX が rootY の根になる
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]

    def get_size(self, x):
        return self.size[self.find(x)]

N,M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    uf.union(A, B)

# 連結成分ごとのサイズを数える
sizes = {}
for i in range(N):
    root = uf.find(i)  # 1. i の属するグループの代表元（ルート）を探す
    if root not in sizes:  # 2. まだルートが辞書に登録されていない場合
        sizes[root] = uf.get_size(i)  # 3. そのルートが属するグループのサイズを辞書に登録する


cnt = 0

# 各連結成分のペア数を計算
for size in sizes.values():
    cnt += (size * (size - 1)) // 2

print(cnt - M)


##################################3
import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())

class friend :
    def __init__(self,n) :
        self.n = n
        self.com = [-1]*n
    
    def find(self,x) :
        if self.com[x] < 0 :
            return x
        else :
            self.com[x] = self.find(self.com[x])
            return self.com[x]
    
    def connect(self,x,y) :
        Xroot = self.find(x)
        Yroot = self.find(y)
        
        if Yroot < Xroot :
            Xroot , Yroot = Yroot ,Xroot
        #合体 Xに
        self.com[Xroot] += self.com[Yroot]
        self.com[Yroot] = Xroot
        #print(self.com)
    
    def size(self):
        num = 0
        for i in self.com :
            if i >= -1:
                pass
            else : 
                i *= -1
                num += i*(i-1)/2
        return num
    
    def check(self,x,y) :
        return self.find(x) != self.find(y)
                
        
fr = friend(N)
for i in range(M) :
    a,b = map(int,input().split())
    if fr.check(a-1,b-1) :
        fr.connect(a-1,b-1)

ans = int(fr.size()-M)
print(ans)
#==============================================
n, m = map(int, input().split())
G=[[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.size[x] += self.size[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

tree = UnionFind(n)
d = {}
for i in range(n):
    for j in G[i]:
        tree.union(i, j)

for i in range(n):
    if tree.find(i) in d:
        d[tree.find(i)] += 1
    else:
        d[tree.find(i)] = 1
ans = 0
for i in d:
    ans += d[i]*(d[i]-1)//2
print(ans-m)



