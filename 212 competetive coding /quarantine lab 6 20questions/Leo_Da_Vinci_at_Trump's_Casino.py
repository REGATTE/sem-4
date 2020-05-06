
N,data,R,ones = int(input()),list(map(int,input().split())),int(input()),[]

for i in range(N):
    data[i] = data[i]%2
    if(data[i]==1):
        ones.append(i)
        
X = data[R]
for i in range(N-X):
    count = sum(data[i:i+X])
    for j in range(i+X,N):
        count+=data[j]
        if(count==R):
            X = j-i+1

print(X)