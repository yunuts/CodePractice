N = int(inpu())

left,right = 1,10**5

while 0.0001 < right - left: #left < right:
    middle = (left+right)/2
    
    value = middle ** 3 + middle
    
    if value >= N:
        #print(left)
        right = middle
    elif value < N:
        left = middle + 0.001

#print(left,right,value,middle)
print(middle)


## ABC 319 D

