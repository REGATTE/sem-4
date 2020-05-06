
M,B,N,C,(X,Y) = int(input()),list(map(int,input().split())),int(input()),list(map(int,input().split())),map(int,input().split())

B.sort(),C.sort(reverse=True)
if(B[X-1]<C[Y-1]):
    print("Yes")
else:
    print("No")