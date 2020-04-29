n,l,m,s=int(input()),list(map(int,input().split())),int(input()),[]
for i in range(n):
    for j in range(i+1,n):
        if(sum(l[i:j])%m==0):
            s.append(len(l[i:j]))
print(max(s))
