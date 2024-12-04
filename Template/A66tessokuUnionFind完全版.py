#Union find 完全版　ABC 333 D

#https://note.nkmk.me/python-union-find/

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n  # 最初は親がいない
        self.parents = [-1] * n  # 最初はグループの頂点数が-1

    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #要素x, yが同じグループに属するかどうかを返す
    def size(self, x):
        return -self.parents[self.find(x)]

    #要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    #すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    #グループの数を返す
    def group_count(self):
        return len(self.roots())

    #{ルート要素: [そのグループに含まれる要素のリスト], ...}
    # のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    #print()での表示用
    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# メイン関数
N = int(input())  # 頂点数

# 頂点 1 を取り除いた森について、Union-Find で連結成分を管理
forest = UnionFind(N)

# 辺の入力処理
for _ in range(N - 1):
    u, v = map(int, input().split())
    if u != 1:  # 頂点1に接続する辺でなければ
        forest.union(u - 1, v - 1)  # 辺を追加（0-indexedにしている）

# N から最大の連結成分のサイズを引いたものが答え
max_group_size = max(len(group) for group in forest.all_group_members().values())
print(N - max_group_size)


print(forest.roots())






N,Q = map(int,input().split())

#=============

class UnionFind:
    def __init__(self,n):
        self.parent = [-1] *(n+1) # 最初は親がいない
        self.size = [1] * (n+1)  # 最初はグループの頂点数が１

    #　頂点 x の値を返す関数
    def root(self,x):
        #while self.parent[x] != -1:
        #    x = self.parent[x]
        #return x
    
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    #　要素 u,v　を統合する
    def union(self,u,v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v　が異なるグループの時のみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.parent[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            
            else:
                self.parent[rootv] = rootu
                self.size[rootu] += self.size[rootv]

        
    def connected(self,u,v):

        return self.root(u) == self.root(v)


uf = UnionFind(N+1)
for _ in range(Q):
    num,u,v = map(int,input().split())
    if num == 1:
        # 辺を追加する ( 頂点 u , v を結合する)
        uf.union(u,v)

    elif num == 2:
        # ２つの頂点が同じ連結成分に属しているかをチェックする
        if uf.connected(u,v):
            print('Yes')
        else:
            print('No')
            