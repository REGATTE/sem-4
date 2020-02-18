n=int(input())
l=[25,10,5,1]
i=0
while(n!=0):
    if(n//l[i]!=0):
        print(l[i],":",n//l[i])
        n=n%l[i]
    i+=1
