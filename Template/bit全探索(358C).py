#bit

##358C
N,M = map(int,input().split())

S = [ input() for _ in range(N)]

def possible(bit):
    res=[False] * M
    ans=0
    for i in range(N):
        if (bit >> i) & 1: # i 桁目が0か１課を見て、i店舗にいくか判定する
            for j in range(M):
                if S[i][j] == 'o':
                    res[j] = True
            ans+=1
    if all(res):
        return ans
    else:
        return False

INF = float('inf')
ans = INF

for bit in range(1 << N):
    check = possible(bit) #bit の条件でポップコーンを全て食べられるか
    if check:
        ans = min(ans,check) # 答えの更新

print(ans) 

## 167C========
def check(learn_total):
    for i in range(m):
        if learn_total[i] < x:
            return False  # 1個でもx未満ならFalse
    return True # 全部x以上ならTrue



def calc_price(bit):
    price_total = 0  # 値段の合計
    learn_total = [0] * m  # 理解度

    for i in range(n):
        if (bit >> i) & 1:  # i桁目が0か1か見て、i冊目を買うか買わないか判定します
            price_total += c[i]  # 買うので、i冊目の値段を加算します
            learn = a[i]  # 「i冊目の参考書を読んで増える、各アルゴリズムの理解度」のリストです
            for j, la in enumerate(learn):  # 理解度を加算します enumerateを使うと、range(n)よりスマートです
                learn_total[j] += la

    # 条件を満たすか、check関数で確認します
    if check(learn_total):
        return price_total # 条件を満たすので、値段を返します
    else:
        return INF # 条件を満たさないので、INFを返します



if __name__ == '__main__':
    n, m, x = list(map(int, input().split()))

    # 空のリストを作って、appendで追加していきます
    c = []  # 参考書の値段です
    a = []  # 各参考書に入る理解度です

    for i in range(n):
        c_temp, *a_temp = map(int, input().split())# こうすると、2つ目以降をリストで受け取れます
        c.append(c_temp)
        a.append(a_temp)

    INF = float("inf")
    ans = INF

    for bit in range(1 << n):
        price = calc_price(bit)  # 条件を満たすならそのときの値段、満たさないならINFが返ってきます
        ans = min(ans, price)  # 答えを更新します

    if ans == INF:
        print(-1)  # どうやっても条件を満たせなかった
    else:
        print(ans)

