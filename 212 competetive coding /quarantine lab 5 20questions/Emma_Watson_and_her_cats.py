N,data,X = int(input()),list(map(int,input().split())),int(input())

def check(N,data,X):
    data.sort(reverse=True)
    val,total = sum(data[:X]),data[0]*X
    if(val==total):
        return 0
    else:
        M = total-val
    for i in range(1,N-X+1):
        val,total = val-data[i-1]+data[i+X-1],data[i]*X
        if(val==total):
            return 0
        elif((total-val)<M):
            M = total-val
            
    return M

print(check(N,data,X))
