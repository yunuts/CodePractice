#map(int,input().split())

N= int(input())

S=1500
coord = [[0] * (S+2)  for _ in range(S+2)]

for _ in range(N):
    A,B,C,D = map(int,input().split())

    coord[A][B] += 1
    coord[A][D] -= 1
    coord[C][B] -= 1
    coord[C][D] += 1

'''    if D +1 <= W:
        coord[A][D+1] -= 1
    if C+1 <= H:
        coord[C+1][B] -= 1
    if C+1 <= H and D+1 <= W:
        coord[C+1][D+1] += 1
'''
#print(*coord ,sep='\n')
#print('===')
summ= [[0] * (S+2)  for _ in range(S+2)] 
#横xに累積和
for i in range(S+1):
    for j in range(S+1):
        summ[i+1][j+1] = summ[i+1][j] + coord[i][j]

#縦に累積和
#print(*summ ,sep='\n')
#print('===')
for j in range(S+1):
    for i in range(S+1):
        summ[i+1][j+1] = summ[i][j+1] + summ[i+1][j+1]

#print(*summ , sep='\n')
#print('--')

#for row in summ[2:]:
#    print(*row[2:])
cnt=0
for row in summ:
    for num in row:
        if num !=0:
            cnt += 1
print(cnt)