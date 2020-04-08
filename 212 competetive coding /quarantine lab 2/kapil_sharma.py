
#Kapil Sharma is a famous astrologer in the city of Vikendi. One day manager of famous apartment group called Kapil and told that their residents are threatened by ghosts in their homes. The manager wanted Kapil to visit the apartment to solve this issue. The apartment has N*N grid of single villas. Kapil found that some villas have negative energy in it. 1 represents that villa has negative energy and 0 represents that no negative energy is present in a villa. This binary grid is represented as G. Kapil finds that a villa at ijth position will have ghost if the villas from i to N (single row elements starting from ijith position) and i to N (single column elements starting from ijith position) have negativity in it. In this manner Kapil has to count the number of villas X which have negative villas in the right side of the row and downside of the column. For example, G = [[1, 1, 1], [1, 1, 0], [1, 0, 1]] X=2 as the homes are at positions (0, 0) and (2, 2) If G = [[0, 1, 1], [0, 1, 1], [0, 1, 1]] X = 6

#Input Format

#3 1 1 1 1 1 0 1 0 1

#Constraints

#NA

#Output Format

#2

#Sample Input 0

#3
#1 1 1
#1 1 0
#1 0 1
#Sample Output 0

#2


Num = int(input())
def check(data,i,j):
        for r in range(i,Num):
            if(data[r][j]==0):
                return False
        for c in range(j,Num):
            if(data[i][c]==0):
                return False
        return True

data = [0]*Num
for i in range(Num):

    data[i] = list(map(int,input().split()))

    count = 0

for i in range(Num):
        for j in range(Num):
            if(data[i][j] and check(data,i,j)):
                count+=1
print(count)
