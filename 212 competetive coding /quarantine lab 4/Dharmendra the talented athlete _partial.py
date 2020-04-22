"""

Ex2 Dharmendra the talented athlete

Dharmendra is a talented Athlete who is capable of jumping 1 meter, 2 meter and 3 meters distance. Now given a distance X, what is the count C of total number of ways to cover this distance X starting from 0. For example if N = 3 then output C = 4 as possibilities are [1,1,1], [1,2], [2,1], [3] If N = 4 then C = 7. Possibilities are [1,1,1,1], [1,2,1], [2,1,1], [1,1,2], [2,2], [3,1], [1,3]

Input Format

3

Constraints

NA

Output Format

4

"""
N = int(input())

data = [0]*(N+1)
data[:3] = 1,1,2

for i in range(3,N+1):
    data[i] = data[i-1] + data[i-2] + data[i-3]
    
print(data[N])