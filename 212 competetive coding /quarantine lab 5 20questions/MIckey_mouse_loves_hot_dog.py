n,l=int(input()),list(map(int,input().split()))
m1,m2=max(l),min(l)
while(m1!=m2):
    m1,m2,i,l[i]=max(l),min(l),l.index(m1),m1-m2
    m1,m2=max(l),min(l)
print(m2*n)
