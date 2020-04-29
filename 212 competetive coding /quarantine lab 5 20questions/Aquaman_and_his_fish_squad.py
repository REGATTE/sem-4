c = int(input())  
a = list(map(int,input().strip().split()))[:c] 
def aqua(arr, n, k): 
    p = [[0 for x in range(5000)] for x in range(5000)] 
    k =k-1
    for x in range(n - 1, -1, -1): 
        for y in range(0, k + 1): 
            p[x][y] = 10**9
            m= -1
            s = 0
            for l in range(x, n): 
                m = max(m, arr[l]) 
                s+= arr[l]  
                d=(l - x + 1) * m - s 
                if (y > 0): 
                    p[x][y]= min(p[x][y], d + p[l+1][y - 1]) 
                else: 
                    p[x][y] = d 
    return p[0][k] 
n = len(a) 
k = int(input())
print(aqua(a, n, k))
