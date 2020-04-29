c= int(input()) 
a = list(map(int,input().strip().split()))[:c] 
def blu(a, n): 
    y= [[0 for x in range(2)]  for j in range(n+1)] 
    y[0][0] = 0; 
    y[0][1] = -999999; 
    for x in range(0, n): 
        y[x+1][0] = max(y[x][0] + a[x], y[x][1] - a[x]); 
        y[x+1][1] = max(y[x][0] - a[x], y[x][1] + a[x]); 
    return y[n][0]; 
if __name__ == '__main__': 
    n = len(a); 
    print(blu(a, n));
