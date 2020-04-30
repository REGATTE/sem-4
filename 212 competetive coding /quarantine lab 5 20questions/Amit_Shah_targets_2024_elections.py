N,l,k,t=int(input()),list(map(int,input().split())),1,0
s=sum(l)
s1=s//2
S=[1]+[0]*s1
for i in l:
    for j in range(s1,i-k,-k):
        if(S[j-i]==1):
            S[j]=k
for j in range(s1,0,-k):
    if(S[j]==1):
        t=j
        break
print(s-(2*t))
