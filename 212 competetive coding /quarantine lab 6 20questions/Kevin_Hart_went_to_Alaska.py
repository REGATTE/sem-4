
N,P,Q = map(int,input().split())

cost = 0

while(N>0):
    if(N%2==0 and ((N-N/2)*P > Q)):
        N,cost = N/2,cost + Q
        continue
    N,cost = N - 1,cost + P
        
print(cost)