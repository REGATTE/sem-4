N,data = int(input()),list(map(int,input().split()))

X = 1
for i in range(N-X):
    for j in range(N-1,i,-1):
        if(j-i+1<X):
            break
        elif(data[i]>data[j]):
            if(X < j-i+1):
                X = j-i+1

print(X)