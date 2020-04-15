"""
VIRUS from University of Dabra

Veeru Sahastra Buddhi aka VIRUS is an angry old professor from university of Dabra. In his class there are N students where a student male student is represented as 0 and female as 1. One day he calls his students to stand on a line. Since students randomly stood on a line along with their friends, all male and female students mixed together in the line L = [l1,l2,l3….lN] where li represents 0 or 1 based on male or female. Now VIRUS is very angry that students ae mixed in the line L. He wanted all the female students together in the line. At a time, VIRUS can swap any two students from the L. So now what is the minimum number of swaps X required to group the female students together. If L = {1, 0, 1, 0, 1} then X = 1. Only 1 swap is required to group all females together by swapping index 1 with 4 will give us a new sequence {1, 1, 1, 0, 0} If L = {1, 0, 1, 0, 1, 1} then X=1.

Input Format

5 1 0 1 0 1

Constraints

NA

Output Format

1

Sample Input 0

5
1 0 1 0 1
Sample Output 0

1

"""

def minSwaps(arr, n) : 
  
    numberOfOnes = 0

    for i in range(0, n) : 
  
        if (arr[i] == 1) : 
            numberOfOnes = numberOfOnes + 1

    x = numberOfOnes 
      
    count_ones = 0
    maxOnes = 0

    for i in range(0, x) : 
  
        if(arr[i] == 1) : 
            count_ones = count_ones + 1
          
    maxOnes = count_ones 
 
    for i in range(1, (n - x + 1)) : 
 
        if (arr[i - 1] == 1) :  
            count_ones = count_ones - 1

        if(arr[i + x - 1] == 1) : 
            count_ones = count_ones + 1
          
        if (maxOnes < count_ones) : 
                maxOnes = count_ones 

    numberOfZeroes = x - maxOnes 
      
    return numberOfZeroes 
n=int(input())
a =list(map(int,input().split()))

print (minSwaps(a, n))