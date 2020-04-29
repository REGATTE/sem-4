a = list(map(int,input().strip().split()))
def bomb(a, n): 
    if (n <= 2): 
        return 0
    c=0
    for i in range(n - 2): 
        if ((a[i] < a[i + 1] and a[i + 1] < a[i + 2]) or (a[i] > a[i + 1] and a[i + 1] > a[i + 2])): 
            c= c+1        
    return c 
n = len(a) 
print(bomb(a, n))
