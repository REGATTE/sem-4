
N,data,X = int(input()),list(map(int,input().split())),int(input())

Y = 0
for i in range(N-Y):
    x = sum(data[i:i+Y])
    for j in range(i+Y,N):
        x+=data[j]
        if(x<=X):
            Y = j-i +1
        else:
            break
            
print(Y)