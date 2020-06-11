#Joker plans to give Diwali bonus to his employees

import sys 
  
MAX = 100
dp = [] 
  
for i in range(1000): 
    temp1 = [] 
    for j in range(MAX): 
        temp2 = [] 
          
        for k in range(MAX): 
            temp2.append(0) 
        temp1.append(temp2) 
          
    dp.append(temp1) 
def productDigitSum(x, y): 
    sumx = 0
    while x: 
        sumx += x % 10
        x = x // 10
          
    sumy = 0 
    while y: 
        sumy += y % 10
        y = y // 10
      
    return sumx * sumy 
def solve(arr, i, len, prev, n, k): 

    if len == k: 
        return 0

    if i == n: 
        return -sys.maxsize - 1

    if dp[i][len][prev]: 
        return dp[i][len][prev] 
    if len & 1: 
        inc = (productDigitSum(arr[prev], arr[i]) + 
               solve(arr, i + 1, len + 1, i, n, k)) 
    else: 
        inc = solve(arr, i + 1, len + 1, i, n, k) 

    exc = solve(arr, i + 1, len, prev, n, k) 

    dp[i][len][prev] = max(inc, exc) 
    return dp[i][len][prev] 



n=int(input())
arr = list(map(int, input().split()))
k=int(input())
print(solve(arr, 0, 0, 0, n, k)) 