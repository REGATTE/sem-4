# Mickey Mouse loves Hot Dogs


# Mickey Mouse loves to eat hot dogs. After the work Mickey comes home and found that Minnie Mouse has cooked lot of hot dogs and arranged the dinner table with N number of plates each with different number of hot dogs H = [h1,h2,h3….hN]. Now Minnie gives a small mission to Mickey before having the dinner. Minnie tells Mickey the he can eat all the N plates only if all plates are having equal number of hot dogs. Now Mickey asks how? Minnie gives a solution that Mickey can choose any two plates i and j and replace the larger plate (i or j) with the absolute different between those plates |i-j|. In this way, Mickey can do the operation any number of times to finally arrive at N plates with equal number of hot dogs. Since Mickey loves to eat hot dog he was wondering what is the maximum number X of hot dogs he can have that night. If H = [9 12 3 6] then replacing 2nd plate 12 with |12-6| then H becomes [9 6 3 6] now replacing 4th plate with |6-3| H = [9 6 3 3]. Replacing 1st plate 9 with |9-6| then H = [3 6 3 3]. Replacing 2nd plate 6 with |6-3| then H becomes [3 3 3 3] so X = 12. If H = [4 8 6 10] then X = 8.


#solution:

n=int(input())
c=list(map(int,input().split()))
def fun(c,n): 
  for i in range(n):
    for j in range(n):
      if(c[i]>c[j]):
        c[i] = c[i]-c[j]
      if(c[j]>c[i]):
        c[j] = c[j] - c[i]
  return sum(c) 

print(fun(c,n))

# Popeye the part-time Scientist

# Popeye the sailor man is a full-time wanderer and a part time scientist also. He is known for his clinical work in DNA analysis. He recently found that he can find the similarity between DNAs of any two people. Popeye found that two people’s compatibility level will be high if both of their DNA sequences [a1,a2,a3…aN] and [b1,b2,b3…bN] contain some lengthy common subsequence. One day Homer Simpson and Bart Simpson goes to Popeye with DNA reports A = {1, 2, 8, 2, 1} and B= {8, 2, 1, 4, 7}. Now Popeye tells them that their compatibility level number X is 3 as the length of the longest sequence [8, 2, 1] which is common to both A and B is 3. If there is no such subsequence exist Popeye has to report X as 0. For example, A= {1, 2, 3, 2, 1} and B = {8, 7, 6, 4, 7} has no common subsequence in it.

# solution: 



def fun(A, B): 
    n = len(A) 
    m = len(B) 
    dp = [[0 for i in range(n + 1)] for i in range(m + 1)] 
    for i in range(n- 1, -1, -1): 
        for j in range(m- 1, -1, -1): 
            if A[i] == B[j]: 
                dp[i][j] = dp[i + 1][j + 1]+1
    maxm = 0
    for i in dp: 
        for j in i: 
          maxm = max(maxm, j) 
    return maxm 
z=int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(fun(A, B)) 
