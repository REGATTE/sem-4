
(X,Y),data = map(int,input().split()),[]

def check(i,j,n,X,Y,data):
    for x in range(i,i+n):
        for y in range(j,j+n):
            if(data[x][y]==0):
                return False
    return True
            
sol = 0
n = 1
for x in range(X):
    data.append(list(map(int,input().split())))
    
while(n<((min(X,Y)+1))):
    for x in range(X):
        for y in range(Y):
            if((x+n)<=X and (y+n)<=Y):
                if(check(x,y,n,X,Y,data)):
                    sol+=1
            else:
                break
    n+=1

print(sol)