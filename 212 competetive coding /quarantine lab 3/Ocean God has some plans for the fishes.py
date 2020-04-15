"""
Ocean God has some plans for the fishes

The Indian Ocean had N number of fishes each with a specific amount of gold with them G = [g1,g2,g3…gN]. Fishes usually spend these golds for buying cosmetics and snacks in the Ocean Mall. One day the Ocean God has drunk a bottle of juice and said “You know what…. Imma make them fishes very unique”. So, god decided to give any amount of gold to individual fishes in G so that no two fishes can have the same amount of gold. Now God is wondering what is the minimum amount of gold X that he/she has to spend to make the fishes unique in G. If G = [3, 2, 1, 2, 1, 7] then X = 6 as, the new Gold could be [3, 4, 1, 2, 5, 7]. If G = [1, 2, 2] then X = 1. I.e the G can be [1,2,3]

Input Format

6 3 2 1 2 1 7

Constraints

NA

Output Format

6

Sample Input 0

6
3 2 1 2 1 7
Sample Output 0

6
"""
def minSum(arr, n): 
      
    sum = arr[0]; prev = arr[0] 
  
    for i in range(1, n): 
        if arr[i] <= prev: 
            prev = prev + 1
            sum = sum + prev
        else : 
            sum = sum + arr[i] 
            prev = arr[i]
    return sum
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
sum1= 0
for i in range(n):
  sum1 += arr[i]

print(minSum(arr,n)-sum1)