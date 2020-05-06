N = int(input())

                

data,one,two = [0]*N,[],[]

for i in range(N):

    data[i] = list(map(int,input().split()))

    if(1 in data[i]):

        one = [i,data[i].index(1)]

    elif(2 in data[i]):

        two = [i,data[i].index(2)]

        

print(abs(one[0]-two[0])+abs(one[1]-two[1]))