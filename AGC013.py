N = int(input())
A = list(map(int,input().split()))

i = 0
j = 1
cnt = 0
#if N % 2 != 0:
A.append(A[N-1])
N +=1
#print(A)
while i < N-1:
#    j = i + 1
    if A[i] < A[j]:  
        while j < N and A[i] <= A[j]:             
            i = j
            j += 1
 #       print(i,j,cnt)
        cnt += 1
        i = j
        j += 1
  #      print('a',i,j,A[i] , A[j] )  
        
    elif A[i] > A[j]:
        while j < N and A[i] >= A[j]:
 #           print('aa',i,j)
            i = j
            j += 1
 #       print(i,j,cnt)    
        cnt += 1
        i = j 
        j += 1
  #      print('b',i,j,A[i] )#, A[j] )  
    else:       
#        print('koko',i,j,N-1)
        if j ==  N-1:
            cnt += 1
        i = j
        j += 1    
#        print(i,j,cnt)       

print(cnt)