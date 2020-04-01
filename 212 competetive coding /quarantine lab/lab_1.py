#Leo Da Vinci at Trump's Casino

# One day Leo da Vinci goes for gambling at Trump’s Casino. He goes to a special game which requires lot of memorization power. 
# The game manager shows Leo N number of cards each of which has a number written on it.
# The numbers in the card are denoted as C = [c1,c2,c3,…cN]. The manager then packs the deck of cards and keeps it front of Leo.
# The manager then picks up any random number R. Now as per rules, Leo can take bulk of cards which are consequent to each other
# where the number of odd numbers in it is exactly equal to R. Now Leo has to choose a bulk with maximum number of cards X which
# has exactly R number of odd numbers in it. For example if C = {2, 3, 4, 11, 4, 12, 7}, R = 1 then Leo can choose bulk of cards 
# as {4, 11, 4, 12} so length of the bulk of cards is X = 4. If C = {3, 4, 6, 1, 9, 8, 2, 10}, R = 2 then X=7 as the cards bulk 
# is {4, 6, 1, 9, 8, 2, 10}.


# Solution:
n=int(input())
l=list(map(int,input().split()))
r=int(input())
mx=0
for i in range(n):
    rc=0
    c=0
    for j in range(i,n):
        if(l[j]%2==1):
            rc+=1
        if(rc<=r):
            c+=1
        else:
            break
    if(c>mx):
        mx=c
print(mx)




# Airtel comes to Bennett University

# Airtel is a very generous and humble mobile network. One day it chooses Bennett University as a venue to make free outgoing service for its customers. The university has N number of airtel students each of them have different balances in their mobile B = [b1,b2…bN]. These balances can be positive as well as negative. Now Airtel can choose a subsequence of students S who are adjacent to each other in B where the balance of the first guy in S should be greater than or equal to balance of the last guy in S. Now Airtel is sitting there and wondering that what is the maximum number of accounts X it can make outgoing free if it choses S in the aforementioned way. For example, if B = {-5, -1, 7, 5, 1, -2} then S can be {-1, 7, 5, 1, -2} so X = 5. If B = {1, 5, 7} then X = 1.


#solution

n=int(input())
c=list(map(int,input().split()))
def binarySearch(location, s, e, num): 
  
    while (s <= e): 
        mid = (s + e) // 2
  
        if location[mid] >= num : 
            ans = mid 
            e = mid - 1
          
        else: 
            s = mid + 1
  
    return ans 
  
def fun(c, n): 
    location = [None] * n 
    index = [None] * n 
    j = 0
    ans = 0
    for i in range(n):  
        if (j == 0 or location[j - 1] < c[i]) : 
            location[j] = c[i] 
            index[j] = i 
            j += 1
        idx = binarySearch(location, 0,  
                           j - 1, c[i]) 
        ans = max(ans, i - index[idx] + 1) 
    return ans 
print(fun(c, n))
