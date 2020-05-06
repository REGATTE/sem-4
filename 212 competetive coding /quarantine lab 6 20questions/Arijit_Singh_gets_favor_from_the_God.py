import math
X,Y = map(int,input().split())

if(X>=Y):
    print(Y-X)
else:
    multiple = math.log(Y/X,2)
    if(int(multiple)==multiple):
        print(int(multiple))
    else:
        count = 0
        while(X!=Y):
            temp = Y
            while(X<temp):
                temp = temp / 2
            if(X<temp+1):
                X = X*2
            else:
                X-=1
            count+=1
        print(count)