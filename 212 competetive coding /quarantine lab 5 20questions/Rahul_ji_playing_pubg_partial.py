N,data = int(input()),list(map(int,input().split()))

data = list(set(data))
N = len(data)

data.sort()
count = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        if((data[i]+data[j]) in data[j+1:]):
            count+=1
            (data[i],data[j],count)
            
print(count)
