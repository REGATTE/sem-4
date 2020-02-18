n=int(input())
k=list(map(int, input().split()))
while(n!=0):
    m=max(k)
    if(n//m!=0):
        print(m,":",n//m)
        n=n%m
        k[k.index(m)]=0
    else:
        k[k.index(m)]=0

#1200
#500 250 60 50 1