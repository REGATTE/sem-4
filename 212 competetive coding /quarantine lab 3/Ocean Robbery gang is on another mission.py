"""
Ocean Robbery gang is on another mission

The great Ocean robber gang is planning on a new robber mission called “Ocean N” with N members in it. Members in the mission have ages A = [a1,a2,a3…aN]. Since the mission needed cooperation from members, they were already in the increasing order. Cooperation between any two neighbouring members is based on their absolute age difference. Due to some reason they have to relieve K number of members from the gang. But after the removal of the K members, the maximum age difference among the adjacent members in the A should become minimum. So they need to choose those K members in such a way that even the maximum age difference X among neighbours is minimum for the new gang with size N-K. If A = {3, 7, 8, 10, 14}, K = 2 then X = 2. After removing elements A[0] and A[4], the maximum difference between adjacent members is minimum. After removing 0th and 4th member, the remaining gang is [7, 8, 10] If A = [12, 16, 22, 31, 31, 38], K = 3 then X = 6. After removing indices 3,4 and 5 array becomes [12, 16, 22].

Input Format

5 3 7 8 10 14 2

Constraints

NA

Output Format

2

Sample Input 0

5
3 7 8 10 14
2
Sample Output 0

2

"""
import sys 
  
INT_MAX = sys.maxsize; 
INT_MIN = -(sys.maxsize - 1);
def minimumAdjacentDifference(a, n, k) :
    minDiff = INT_MAX;
    for i in range(k + 1) :
        maxDiff = INT_MIN; 
        for j in range( n - k - 1) :  
            for p in range(i, i + j + 1) : 
                maxDiff = max(maxDiff, a[p + 1] - a[p]);
        minDiff = min(minDiff, maxDiff); 
    return minDiff; 
n = int(input()) 
a =list(map(int,input().split())) 
k = int(input()) 
print(minimumAdjacentDifference(a, n, k));