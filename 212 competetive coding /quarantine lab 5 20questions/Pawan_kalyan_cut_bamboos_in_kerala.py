t=int(input())
lis=list(map(int,input().split()))
m=int(input())
x=0
t=0
temp=[]
temp1=[]
x=min(lis)
lis.remove(x)
for i in lis:
    temp.append(int(i)-x)

for i in temp:
    if(i%m==0):
        temp1.append(i//m)
    else:
        t=-1
if(t==-1):
    print(-1)
else:
    print(sum(temp1))
