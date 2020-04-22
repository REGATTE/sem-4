"""
Ex2 Mukesh Ambani - the gypsy who has relatives all over india

Mukesh Ambani is a gypsy who travel to different places around India. From Kashmir to Kanyakumari there are N locations that he wants to visit. At each location, he has one relative who can give a specific number of golds G = [g1,g2,g3….gN]. With a specific X amount of gold, Ambani can travel to any location from i+1 to (i+x)th locations from his current ith location. If a current relative don’t have gold, then he cannot move anywhere. So now Mukesh is wondering that what are different ways to reach Nth location from every ith location. If Mukesh cannot move anywhere from ith location then print “-1”. For example, if G = [3, 2, 0, 1] then output is [2 1 -1 0]. I.e. from index 0 there are two ways to reach 3rd index. Option 1: he can go to index 1 then from index 1 he can go to index 3, Option 2: he can directly go to index 3 with 3 golds. From index 1 there is only one way. From index 2 there is no way to reach index 3 so it is marked as “-1”. For index 3 the options are 0. If G = [1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9] then Output is [52 52 28 16 8 -1 -1 4 2 1 0]

Input Format

4 3 2 0 1

Constraints

NA

Output Format

2 1 -1 0

Sample Input 0

4
3 2 0 1

Sample Output 0

2 1 -1 0

"""

def countWaysToJump(arr, n): 
    count_jump = [0 for i in range(n)] 
    for i in range(n - 2, -1, -1): 
        if (arr[i] >= n - i - 1): 
            count_jump[i] += 1
        j = i + 1
        while(j < n-1 and j <= arr[i] + i): 
            if (count_jump[j] != -1): 
                count_jump[i] += count_jump[j] 
            j += 1
        if (count_jump[i] == 0): 
            count_jump[i] = -1
    for i in range(n): 
        print(count_jump[i], end = " ") 
n=int(input())
arr = list(map(int,input().split(" "))) 
countWaysToJump(arr, n)

