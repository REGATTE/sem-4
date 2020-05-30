# Marvel & DC Universes have something in common

def que(arr1, n, arr2, m, k): 
    c = 0
    a = arr2[0] 
    b = arr2[0] 
    for i in range(m): 
        a = max(a, arr2[i]) 
        b = min(b, arr1[i]) 

    for i in range(n): 
        if (abs(arr1[i] - a) > k 
            or abs(arr1[i] - b) > k): 
            c += 1
    print(c) 

n=int(input())
m=list(map(int,input().split()))
d=list(map(int,input().split()))
x=int(input())

que(m,len(m),d,len(d),x)

