/*
In Bennett University lecture hall H, there are N*N seats. Each seat is occupied by different students. Each of these students are denoted using one of the four numbers 0,1,2 and 3. Number 1 is only one student who is a snacks supplier, Number 2 is only one student who wants the snacks from 1. Number 3 is given to multiple people who can just pass the snacks to anyone next to them who is also number 3. Number 0 is given to people who does not cooperate in the whole process and does not pass the snacks to anyone. Given a hall H with a single source student 1, single destination student 2, 3s and 0s at random locations, you have to count what is the minimum number of moves X needed to move from the 1 to 2. If H = [[0 , 3 , 2 ], [3 , 3 , 0], [1 , 3 , 0 ]]; X=4

If H = [[3 , 3 , 1 , 0 ], [ 3 , 0 , 3 , 3 ], [ 2 , 3 , 0 , 3 ], [ 0 , 3 , 3 , 3 ]]; Then X=4

Input Format

3 0 3 2 3 3 0 1 3 0

Constraints

NA

Output Format

4

Sample Input 0

3
0 3 2
3 3 0
1 3 0 
Sample Output 0

4
*/


N = int(input())
                
data,one,two = [0]*N,[],[]

for i in range(N):
    data[i] = list(map(int,input().split()))
    if(1 in data[i]):
        one = [i,data[i].index(1)]
    elif(2 in data[i]):
        two = [i,data[i].index(2)]
        
print(abs(one[0]-two[0])+abs(one[1]-two[1]))

