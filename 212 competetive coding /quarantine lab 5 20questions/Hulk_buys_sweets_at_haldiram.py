def getMinimumOps(ar): 
      
    # Number of elements in the array 
    n = len(ar) 
  
    # Smallest element in the array 
    small = min(ar) 
  
    # Largest element in the array 
    large = max(ar) 

    dp = [[ 0 for i in range(large + 1)]  
              for i in range(n)] 
  
    # Fill the dp[]][ array for base cases 
    for j in range(small, large + 1): 
        dp[0][j] = abs(ar[0] - j) 

    for i in range(1, n): 
        minimum = 10**9
        for j in range(small, large + 1): 
   
            minimum = min(minimum, dp[i - 1][j]) 
            dp[i][j] = minimum + abs(ar[i] - j) 
    ans = 10**9
    for j in range(small, large + 1): 
        ans = min(ans, dp[n - 1][j]) 
  
    return ans 
  
# Driver code 
N = int(input())
S = list(map(int, input().split()))
  
print(getMinimumOps(S))
