#Jack Sparrow the fisherman wants maximum profit
minimum = -999999
val = []
def que(price, n): 
    for i in range(0,n+1):
      val.append(i)
    val[0] = 0
    for i in range(1, n+1): 
        maximum = minimum 
        for j in range(i): 
             maximum = max(maximum, price[j] + val[i-j-1]) 
        val[i] = maximum 
    return val[n] 
n = int(input())
arr = list(map(int,input().split()))
print(que(arr, n))