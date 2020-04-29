n,l,s=int(input()),list(map(int,input().split())),[]
for i in sorted(set(l)):
    l2=[j for j ,value in enumerate(l) if value==i]
    for j in range(len(l2)-1):
        sub=l[l2[j]:l2[j+1]+1]
        s.append(len(sub))
if(s==[]):
    print(-1)
else:
    print(min(s))
