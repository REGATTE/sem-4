
N,data = int(input()),list(map(int,input().split()))

data.sort()
sol = 0

for n in range(1,N):
    if(data[n]<=data[n-1]):
        sol += data[n-1] + 1 - data[n]
        data[n] = data[n-1] + 1

print(sol)