N = int(input())

def check(data,i,j):

    for r in range(i,N):

        if(data[r][j]==0):

            return False

    for c in range(j,N):

        if(data[i][c]==0):

            return False

    return True

data = [0]*N

for i in range(N):

    data[i] = list(map(int,input().split()))

    

count = 0

for i in range(N):

    for j in range(N):

        if(data[i][j] and check(data,i,j)):

            count+=1

print(count)