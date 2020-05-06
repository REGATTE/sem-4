
N,data = int(input()),list(map(int,input().split()))

first,last = data.index(1),N-1-(data[::-1].index(1))
sol,girls = last-first+1,sum(data)

for i in range(first,last-girls+2):
    count = data[i:i+girls].count(0)
    if(count<sol):
        sol = count
        
print(sol)