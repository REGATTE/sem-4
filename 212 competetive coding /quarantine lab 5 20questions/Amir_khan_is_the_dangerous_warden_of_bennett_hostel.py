c = int(input()) 
a = list(map(int,input().strip().split()))[:c] 
def gang(arr, n): 
    x= {i:0 for i in range(10)} 
    y = 0
    m= 0
    for i in range(n):  
        if arr[i] == 0: 
            y += -1
        else: 
            y += 1
        if (y== 1): 
            m= i + 1
        elif (y not in x): 
            x[y] = i 
        if ((y - 1) in x): 
            if (m < (i - x[y - 1])): 
                m = i - x[y - 1] 
    return m
n = len(a) 
print(gang(a, n))
